#!/usr/bin/env python3
import mdmdrupalutil as mdu
import os
import shutil
import textwrap

from pyprojroot import here
from mdmdrupaldb import STAFF

AUTHOR_TEMPLATE=textwrap.dedent('''\
  ---
  # Display name
  title: {staff_name} {staff_surname}
  
  # Custom keyword (e.g. to be used by md2bib.py)
  short_name: {short_name}
  
  # Is this the primary user of the site?
  superuser: false
  
  # Role/position
  role: '{staff_position}'
  
  # Organizations/Affiliations
  organizations:
    - name: {organization_name}
      url: '{organization_url}'
  
  # Short bio (displayed in user profile at end of posts)
  bio: My research interests include ...
  
  interests:
    - Interest 1
    - Interest 2
    - ...
  
  education:
    courses:
      - course: PhD in 
        institution: Universidad 
        year: 2004
      - course: MSc in 
        institution: Universidad 
        year: 2000
  
  # Social/Academic Networking
  # For available icons, see: https://wowchemy.com/docs/getting-started/page-builder/#icons
  #   For an email link, use "fas" icon pack, "envelope" icon, and a link in the
  #   form "mailto:your-email@example.com" or "#contact" for contact widget.
  social:
    - icon: envelope
      icon_pack: fas
      link: 'mailto:{staff_emailuser}@{staff_emaildomain}'
  #  - icon: twitter
  #    icon_pack: fab
  #    link: https://twitter.com/jfernandez_uc
  #  - icon: orcid
  #    icon_pack: ai
  #    link: https://orcid.org/0000-0001-7719-979X
  #  - icon: google-scholar
  #    icon_pack: ai
  #    link: https://scholar.google.com/citations?hl=en&user=otvNU1UAAAAJ&view_op=list_works&sortby=pubdate
  #  - icon: publons
  #    icon_pack: ai
  #    link: https://publons.com/researcher/2820263/antonio-s-cofino/
  #  - icon: scopus
  #    icon_pack: ai
  #    link:  https://www.scopus.com/authid/detail.uri?authorId=6505838419
  #  - icon: zotero
  #    icon_pack: ai
  #    link: https://www.zotero.org/cofinoa
  #  - icon: zenodo
  #    icon_pack: ai
  #    link:  https://zenodo.org/communities/cofinoa
  #  - icon: github
  #    icon_pack: fab
  #    link: https://github.com/jesusff
  #  - icon: stack-overflow
  #    icon_pack: fab
  #    link: https://stackoverflow.com/users/2565896/
  # Link to a PDF of your resume/CV from the About widget.
  # To enable, copy your resume/CV to `static/files/cv.pdf` and uncomment the lines below.
  # - icon: cv
  #   icon_pack: ai
  #   link: files/cv.pdf
  
  # Enter email to display Gravatar (if Gravatar enabled in Config)
  email: ''
  
  # Highlight the author in author lists? (true/false)
  highlight_name: true
  
  # Organizational groups that you belong to (for People widget)
  #   Set this to `[]` or comment out if you are not using People widget.
  user_groups:
    - {user_group}
  ---
  
  {staff_body}
''')

maps = mdu.get_maps(['author', 'keyword'])

ug_map = {
 'former'     : 'Former group members',
 'mstudent'   : 'MSc Students',
 'permanent'  : 'Permanent staff',
 'phdstudent' : 'PhD Students',
 'postdoc'    : 'Post-doc Researchers',
 'student'    : 'Grad Students',
 'support'    : 'Support staff'
}

org_urls = {
 'UC'        : 'https://web.unican.es',
 'IFCA'      : 'https://ifca.unican.es',
 'AEMET'     : 'https://www.aemet.es',
 'Predictia' : 'https://www.predictia.es'
}

#PIC_BASEURL = 'http://meteo.unican.es/'
PIC_BASEURL = 'util/mdmdrupal'
CONTENT_BASEPATH = './content/'

for author in STAFF():
  alias = ''.join(author['staff_alias'])
  author['short_name'] = ' '.join(alias.replace(',','').split(' ')[::-1])
  author['user_group'] = ug_map[author['staff_stafftype']]
  author['organization_name'] = author['staff_institutions'][0]
  author['organization_url'] = org_urls[author['organization_name']]
  if alias in maps['author'] and not ' ' in maps['author'][alias]:
    dirname = maps['author'][alias]
  else:
    dirname = mdu.remove_odd_chars(
      '-'.join(' '.join([author['staff_name'], author['staff_surname']]).split(' '))
    ).strip().lower()
  
  pathname = here() / 'content/authors' / dirname
  print(f'Creating content in {pathname}')
  os.makedirs(pathname, exist_ok = True)
  # get pic
  if author['staff_personal_picture_file']:
    pic_url = here() / PIC_BASEURL / author['staff_personal_picture_file'] 
    print(f'  Pic retrieval: {pic_url}')
    try:
      shutil.copy2(pic_url, pathname/'avatar.jpg')
      print('    SUCCEED')
    except:
      shutil.copy2(here() / PIC_BASEURL / 'files/personal_pictures/default.jpg', pathname/'avatar.jpg')
      print('    FAILED')
  with open(pathname / '_index.md', 'w', errors='surrogateescape') as f:
    f.write( AUTHOR_TEMPLATE.format(**author) )
