---
title: 'A cloud-computing system on the grid through virtualization'

event: 'First EELA-2 Conference'
event_url: 'http://indico.eu-eela.eu/conferenceDisplay.py?confId=132'

#location: Venue
address:
#  street: 450 Serra Mall
  city: Bogotá
#  region: CA
#  postcode: '94305'
  country: COLOMBIA

summary: ''
#abstract: ''

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2009-02-25T00:00:00'
date_end: '2009-02-27T00:00:00'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2022-03-24T00:00:00Z'

authors: 
  - valvanuz-fernandez
  - antonio-s-cofino
  - jesus-fernandez
  - M.A Diaz
  - R Ramos
  - F Prieta
  - M Rubio
  - R Priego
  - F Rodriguez
  - J.J Alba
tags: 
  - GRID computing
  - Virtualization
  - Cloud computing

# Is this a featured talk? (true/false)
featured: false

# Image caption
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

url_code: ''
url_pdf: 'files/private/cloud-computing-on-the-grid.pdf'
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

# Extra metadata
#   Not in hugo/wowchemy templates
conf_type: 'international'
conf_deadline: ''
contrib_type: 'oral'
contrib_institutions: 
  - UC
contrib_research_lines: 
  - GRID computing in Earth Sciences
contrib_doi: ''
contrib_abstract_url: 'http://indico.eu-eela.eu/materialDisplay.py?contribId=14&amp;sessionId=0&amp;materialId=paper&amp;confId=132'
contrib_abstract_urltitle: 'A cloud-computing system on the grid through virtualization'
---

Nowadays, scientists who make use of the grid are experiencing incompatibility problems between the scientific application that is executed on Working Nodes (WN) and the software installed on them; such as operating system, libraries, and grid middleware. On the other hand, scientists have problems to submit their jobs to different grid sites, because of the grid does not provide a software installation standard on them. This work presents the integration of virtualization technology on grid WN\'s. This way, users can introduce an application into a virtual machine (VM) with different software to the one installed on the WN. Thus, the job submitted by the user, will cause the VM to start on a WN of some site and to automatically execute a scientific application that may have been previously prepared in a user friendly environment. This work, which is based on the cloud computing notion, lets the users to execute applications on the grid, in isolation from lower software layers. Results have achieved the expected objective: to let users submit scientific applications to the grid, isolating application dependences from the grid software environment.
