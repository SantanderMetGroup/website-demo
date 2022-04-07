#!/usr/bin/env python3
import os
import re
import sqlite3
import unidecode
import yaml
import textwrap

from mdmdrupaldb import CONTRIBUTIONS

EVENT_TEMPLATE=textwrap.dedent('''\
  ---
  title: '{contrib_title}'
  
  event: '{conf_title}'
  event_url: '{conf_web}'
  
  #location: Venue
  address:
  #  street: 450 Serra Mall
    city: {conf_city}
  #  region: CA
  #  postcode: '94305'
    country: {conf_country}
  
  summary: ''
  #abstract: ''
  
  # Talk start and end times.
  #   End time can optionally be hidden by prefixing the line with `#`.
  date: '{conf_startdate}'
  date_end: '{conf_enddate}'
  all_day: false
  # Schedule page publish date (NOT talk date).
  publishDate: '2022-03-24T00:00:00Z'
  authors: {authors}
  tags: {tags}
  # Is this a featured talk? (true/false)
  featured: false
  
  # Image caption
  #image:
  #  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  #  focal_point: Right
  
  url_code: ''
  url_pdf: '{contrib_pdf_file}'
  url_slides: '{contrib_poster-talk_file}'
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
  projects: {projects}
  research_lines: {research_lines}
  collab_institutions: {institutions}
  # Extra metadata
  #   Not in hugo/wowchemy templates
  conf_type: '{conf_type}'
  conf_deadline: '{conf_deadline}'
  contrib_type: '{contrib_type}'
  contrib_doi: '{contrib_doi}'
  contrib_abstract_url: '{contrib_abstract_url}'
  contrib_abstract_urltitle: '{contrib_abstract_urltitle}'
  ---
  
  {contrib_body}
''')
maps = {}
for m in ['author_map.yml', 'keyword_map.yml']:
  map_name = m.split('/')[-1].split('_')[0]
  with open(m) as fp:
    maps[map_name] = yaml.load(fp, Loader=yaml.FullLoader)
  # Drop None's from name dictionary
  maps[map_name] = {k: v for k, v in maps[map_name].items() if v is not None}

def tolist(text):
  return('\n  - '+'\n  - '.join(text))

def tomappedlist(lst, mapdict):
  rval = ''
  for i in lst:
    fullname = mapdict[i] if i in mapdict else i
    if ',' in fullname: # is an author name
      surn, name = tuple(fullname.split(',')[:2])
      rval += '\n  - ' + name.strip() + ' ' + surn.strip()
    elif fullname == '': # skip empty entries (e.g. mapped to blank string)
      continue
    else:
      rval += '\n  - ' + fullname
  return(rval)

def clean_text_entries(dic):
  for key in dic:
    if type(dic[key]) == type('string'):
      dic[key] = dic[key].replace("'", "\\'").strip()
    if dic[key] is None:
      dic[key] = ''

def remove_odd_chars(text, odd_chars='.,:()'):
  rval = unidecode.unidecode(text)
  for char in odd_chars:
    rval = rval.replace(char, '')
  return(rval)
  
for contrib in CONTRIBUTIONS():
  clean_text_entries(contrib)

  if not contrib['contrib_title'].startswith('A'):
    continue

  contrib['authors'] = tomappedlist(contrib['contrib_authors'], maps['author'])
  contrib['tags'] = tomappedlist(contrib['contrib_keywords'], maps['keyword'])
  contrib['research_lines'] = tolist(contrib['contrib_research'])
  contrib['institutions'] = tolist(contrib['contrib_entities'])
  contrib['projects'] = tolist(contrib['contrib_projects'])
  for tag in ['contrib_pdf_file','contrib_poster-talk_file']:
    contrib[tag] = 'https://meteo.unican.es/' + contrib[tag] if contrib[tag] else ''
  dirname = str(contrib['contrib_year']) + '-' + remove_odd_chars('-'.join(contrib['contrib_title'].strip().lower().split(' ')[:5]))
  pathname = '../content/event/' + dirname
  os.makedirs(pathname, exist_ok = True)

  with open(pathname+'/index.md', 'w', errors='surrogateescape') as f:
    f.write( EVENT_TEMPLATE.format(**contrib) )
