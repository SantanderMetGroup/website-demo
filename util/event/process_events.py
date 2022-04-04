#!/usr/bin/env python3
import os
import re
import sqlite3
import unidecode

SQLITE_FILE = 'util/mdmdrupal.sqlite'

namedict = {
  'Cofiño, A.S.': 'antonio-s-cofino',
  'Fernández, J.': 'jesus-fernandez',
  'Fernández-Quiruelas, V.': 'valvanuz-fernandez',
  'Gutiérrez, J.M.': 'jose-manuel-gutierrez',
}

def tolist(text):
  return('\n  - '+'\n  - '.join(text))

def tonamelist(text):
  items = text
  rval = ''
  for i in items:
    if i in namedict:
      rval += '\n  - ' + namedict[i]
    else:
      if ',' in i:
        surn, name = tuple(i.split(',')[:2])
        rval += '\n  - ' + name.strip() + ' ' + surn.strip()
      else:
        rval += '\n  - ' + i
  return(rval)

CONTRIB_SQL = '''
  SELECT 
    n1.nid                            AS nid     ,
    n1.type                           AS type    ,
    datetime(n1.created, 'unixepoch') AS created ,   
    datetime(n1.changed, 'unixepoch') AS changed ,   
    u1.name                           AS user    ,
    n1.title                          AS contrib_title ,
    r1.body                           AS contrib_body  ,
    t1.field_conf_contrib_type_value  AS contrib_type         ,
    t1.field_urlabstract_url          AS contrib_abstract_url ,
    t1.field_urlabstract_title        AS contrib_abstract_urltitle ,
    f5.field_year_value               AS contrib_year,
    f4.field_doi_value                AS contrib_doi,
    f6.filepath                       AS 'contrib_poster-talk_file',
    f8.filepath                       AS 'contrib_pdf_file',
    n2.title                          AS conf_title ,
    t2.field_conf_type_value          AS conf_type , 
    f1.field_city_value               AS conf_city ,
    t2.field_country_value            AS conf_country ,
    f2.field_subdeadline_value        AS conf_deadline ,
    t2.field_timeperiod_value         AS conf_startdate ,
    t2.field_timeperiod_value2        AS conf_enddate,
    f3.field_web_url                  AS conf_web ,
    r2.body                           AS conf_body
  
  FROM      node                      n1 
  LEFT JOIN node_revisions            r1 
    ON n1.nid = r1.nid
  LEFT JOIN users                     u1
    ON n1.uid = u1.uid
  LEFT JOIN content_type_conf_contrib t1
    ON n1.nid = t1.nid
  LEFT JOIN node                      n2
    ON t1.field_noderef_conf_nid = n2.nid
  LEFT JOIN node_revisions            r2
    ON t1.field_noderef_conf_nid = r2.nid
  LEFT JOIN content_type_conference   t2
    ON t1.field_noderef_conf_nid = t2.nid
  LEFT JOIN content_field_city        f1
    ON t1.field_noderef_conf_nid = f1.nid
  LEFT JOIN content_field_subdeadline f2
    ON t1.field_noderef_conf_nid = f2.nid
  LEFT JOIN content_field_web         f3
    ON t1.field_noderef_conf_nid = f3.nid
  LEFT JOIN content_field_doi         f4
    ON n1.nid = f4.nid
  LEFT JOIN content_field_year        f5
    ON n1.nid = f5.nid
  LEFT JOIN files                     f6
    ON t1.field_posterpdf_fid = f6.fid
  LEFT JOIN content_field_pdf_file    f7
    ON n1.nid = f7.nid
  LEFT JOIN files                     f8
    ON f7.field_pdf_file_fid = f8.fid
  WHERE 
    n1.type = 'conf_contrib'
'''

#field_authors
# vid=2 -> author vocabulary
AUTHORS_SQL='''
	SELECT t.tid,name
	FROM term_node t LEFT JOIN term_data d
    ON t.tid=d.tid
  WHERE 
    d.vid = 2    AND
    nid   = :nid
  ORDER BY t.orden
'''
#field_entities
# vid=3  -> Institutions vocabulary
# vid=12 -> Collab. entities vocabulary
ENTITIES_SQL='''
	SELECT t.tid,name
	FROM term_node t LEFT JOIN term_data d
    ON t.tid=d.tid
  WHERE 
    ( d.vid = 3 OR d.vid = 12 ) AND
    nid   = :nid
  ORDER BY d.vid, t.orden
'''

#field_keywords
# vid=8 -> keywords vocabulary
KEYWORDS_SQL='''
	SELECT t.tid,name
	FROM term_node t LEFT JOIN term_data d
    ON t.tid=d.tid
  WHERE 
    d.vid = 8    AND
    nid   = :nid
  ORDER BY t.orden
'''

#field_projects
PROJECTS_SQL='''
  SELECT n1.nid, n1.title AS name
  FROM content_field_noderef_proj p INNER JOIN node n1
    ON p.field_noderef_proj_nid = n1.nid
  WHERE 
    p.nid = :nid
'''

#field_research
RESEARCH_SQL='''
  SELECT n1.nid, n1.title AS name
  FROM content_field_noderef_resact p INNER JOIN node n1
    ON p.field_noderef_resact_nid = n1.nid
  WHERE 
    p.nid = :nid
'''

def populate_from_vocabularies(contrib, sql, field):
  # Empty list just in case there is not values
  contrib[field] = [] 
  for row in conn.execute(sql, contrib):
    dic = dict(row)
    contrib[field].append(dic['name'])

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
  
conn = sqlite3.connect(SQLITE_FILE)
conn.row_factory = sqlite3.Row  

for contrib_row in conn.execute(CONTRIB_SQL):
  contrib = dict(contrib_row)
  ## Populate authors
  populate_from_vocabularies(contrib, AUTHORS_SQL, 'contrib_authors')
  ## Populate entities and institutions
  populate_from_vocabularies(contrib, ENTITIES_SQL, 'contrib_entities')
  ## Populate KEYWORDS
  populate_from_vocabularies(contrib, KEYWORDS_SQL, 'contrib_keywords')
  ## Populate projects
  populate_from_vocabularies(contrib, PROJECTS_SQL, 'contrib_projects')
  ## Populate research activities
  populate_from_vocabularies(contrib, RESEARCH_SQL, 'contrib_research')

  clean_text_entries(contrib)

  if not contrib['contrib_title'].startswith('A'):
    continue

  contrib['authors'] = tonamelist(contrib['contrib_authors'])
  contrib['tags'] = tolist(contrib['contrib_keywords'])
  contrib['research_lines'] = tolist(contrib['contrib_research'])
  contrib['institutions'] = tolist(contrib['contrib_entities'])
  contrib['projects'] = tolist(contrib['contrib_projects'])
  dirname = str(contrib['contrib_year']) + '-' + remove_odd_chars('-'.join(contrib['contrib_title'].strip().lower().split(' ')[:5]))
  pathname = 'content/event/' + dirname
  os.makedirs(pathname, exist_ok = True)

  with open(pathname+'/index.md', 'w', errors='surrogateescape') as f:
    f.write('''---
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
projects: []

# Extra metadata
#   Not in hugo/wowchemy templates
conf_type: '{conf_type}'
conf_deadline: '{conf_deadline}'
contrib_type: '{contrib_type}'
contrib_institutions: {institutions}
contrib_research_lines: {research_lines}
contrib_doi: '{contrib_doi}'
contrib_abstract_url: '{contrib_abstract_url}'
contrib_abstract_urltitle: '{contrib_abstract_urltitle}'
---

{contrib_body}
'''.format(**contrib)
  )
