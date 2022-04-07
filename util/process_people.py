#!/usr/bin/env python3
import mdmdrupalutil as mdu
import os
import textwrap
import urllib.request

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
    - name: IFCA
      url: 'https://ifca.unican.es'
  
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
  #  - icon: google-scholar
  #    icon_pack: ai
  #    link: https://scholar.google.com/citations?hl=en&user=otvNU1UAAAAJ&view_op=list_works&sortby=pubdate
  #  - icon: github
  #    icon_pack: fab
  #    link: https://github.com/jesusff
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

maps = mdu.get_maps(['author_map.yml', 'keyword_map.yml'])

ug_map = {
 'former': 'Former group members',
 'mstudent': 'MSc Students',
 'permanent': 'Permanent staff',
 'phdstudent': 'PhD Students',
 'postdoc': 'Post-doc Researchers',
 'student': 'Grad Students',
 'support': 'Support staff'
}

for author in STAFF():
  #clean_text_entries(author)
  author['short_name'] = author['staff_name'][0] + '. ' + mdu.remove_odd_chars(author['staff_surname'])
  author['user_group'] = ug_map[author['staff_stafftype']]
  dirname = mdu.remove_odd_chars(
    '-'.join(' '.join([author['staff_name'], author['staff_surname']]).split(' '))
  ).strip().lower()
  pathname = '../content/authors/' + dirname
  print(f'Creating content in {pathname}')
  os.makedirs(pathname, exist_ok = True)
  # get pic
  if author['staff_personal_picture_file']:
    pic_url = 'http://meteo.unican.es/' + author['staff_personal_picture_file']
    try:
      urllib.request.urlretrieve(pic_url, f'{pathname}/avatar.jpg')
    except:
      print('Pic retreval failed')
  with open(pathname+'/_index.md', 'w', errors='surrogateescape') as f:
    f.write( AUTHOR_TEMPLATE.format(**author) )
