import json
import os
import re
import unidecode

def tolist(text):
  items = text.split(' | ')
  items = [' '.join(list(reversed(i.split(',')))) for i in items]
  return('\n  - '+'\n  - '.join(text.split(' | ')))

def render_dates(text):
  dates = [x[3:]+'-'+x[0:2] for x in text.split(' - ')]
  return(dates[0] + '-01T00:00:00')

def cleanxml(text):
  return(re.sub('.*>(.*)<.*', '\\1', text))

# http://meteo.unican.es/en/view/contributions_conf_export/%2A/json_exhibit/%2A/%2A/%2A

with open('util/event/conferencias.json', encoding='utf-8-sig', errors='surrogateescape') as f:
  data = json.load(f)

d = dict(
  authors = 'drupal_txn_people',
  title = 'drupal_node_title',
  summary = 'drupal_node_title',
  abstract = 'drupal_node_body',
  event = 'drupal_field_noderef_conf',
  date = 'drupal_field_year',
  tags = 'drupal_txn_keywords',
)

for item in data['items']:
  item['authors'] = tolist(item[d['authors']])
  item['title'] = cleanxml(item[d['title']])
  item['summary'] = cleanxml(item[d['summary']])
  item['abstract'] = item[d['abstract']]
  item['event'] = cleanxml(item[d['event']])
  item['date'] = item[d['date']]
  item['tags'] = tolist(item[d['tags']])
  dirname = unidecode.unidecode('-'.join(item['title'].lower().split(' ')[:5])).replace(':','').replace('.','')
  pathname = 'content/event/' + dirname
  os.makedirs(pathname, exist_ok = True)

  with open(pathname+'/index.md', 'w', errors='surrogateescape') as f:
    f.write('''---
title: '{title}'

event: '{event}'
#event_url: https://example.org

location: Virtual event
#address:
#  street: 450 Serra Mall
#  city: Stanford
#  region: CA
#  postcode: '94305'
#  country: United States

summary: '{summary}'
#abstract: ''

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: {date}
#date_end: '2030-06-01T15:00:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2022-03-24T00:00:00Z'

authors: {authors}
tags: {tags}

# Is this a featured talk? (true/false)
featured: false

image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  focal_point: Right

url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides:

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

{abstract}
'''.format(**item)
  )
