import csv
import os

def tolist(text):
  items = text.split(' | ')
  items = [' '.join(list(reversed(i.split(',')))) for i in items]
  return('\n  - '+'\n  - '.join(text.split(' | ')))

def render_dates(text):
  dates = [x[3:]+'-'+x[0:2] for x in text.split(' - ')]
  return(dates[0] + '-01T00:00:00')

with open("projects.tsv") as f:
  tsv_file = csv.reader(f, delimiter="\t")
  rows = list(tsv_file)

header = rows[0]

for line in rows[1:]:
  data = dict(zip(header, line))
  data['People'] = tolist(data['People'])
  data['Keywords'] = tolist(data['Keywords'])
  data['CollabEntitites'] = tolist(data['CollabEntitites'])
  data['Institutions'] = tolist(data['Institutions'])
  data['Period'] = render_dates(data['Period'])
  if not data['Description']:
    data['Description'] = 'TBC'
  dirname = data['Title'].lower().replace(' ','-')
  pathname = 'content/project/' + dirname
  os.makedirs(pathname, exist_ok = True)
  with open(pathname+'/index.md', 'w') as f:
    f.write('''---
title: '{Title} | {ShortDescription}'
summary: >
  {Description}  
tags: {Keywords}
date: {Period}
external_link: {WebUrl}
authors: {People}
# extra tags:
id: {ProjectCode}
status: {ProjectStatus}
category: {ProjectCategory}
type: {ProjectType}
funder: {FundingInstitution}
funder_program: {Program}
collab_entities: {CollabEntitites}
institution: {Institutions}
---'''.format(**data)
  )
