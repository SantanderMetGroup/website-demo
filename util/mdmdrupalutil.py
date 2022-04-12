#!/usr/bin/env python3
import unidecode
import yaml
from pyprojroot import here

def get_maps(mapfiles):
  maps = {}
  for map_name in mapfiles:
    m = here() / f'util/{map_name}_map.yml'
    with open(m) as fp:
      maps[map_name] = yaml.load(fp, Loader=yaml.FullLoader)
    # Drop None's from name dictionary
    maps[map_name] = {k: v for k, v in maps[map_name].items() if v is not None}
  return maps

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
