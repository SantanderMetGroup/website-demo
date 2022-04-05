---
title: 'Aggregation of Grid and HPC resources for running huge experiments in climate and weather prediction'

event: 'EGU General Assembly 2011'
event_url: 'http://meetingorganizer.copernicus.org/EGU2011/sessionprogramme'

#location: Venue
address:
#  street: 450 Serra Mall
  city: Vienna
#  region: CA
#  postcode: '94305'
  country: Austria

summary: ''
#abstract: ''

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2011-04-03T00:00:00'
date_end: '2011-04-08T00:00:00'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2022-03-24T00:00:00Z'

authors: 
  - antonio-s-cofino
  - carlos-blanco
  - valvanuz-fernandez
tags: 
  - Grid computing
  - GridWay
  - LRMS
  - high-performance computing

# Is this a featured talk? (true/false)
featured: false

# Image caption
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

url_code: ''
url_pdf: 'https://meteo.unican.es/files/pdfs/EGU2011-13194-1.pdf'
url_slides: 'https://meteo.unican.es/files/posters/2011_CofinoAS_EGU.pdf'
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
projects: 
  - 
research_lines: 
  - GRID computing in Earth Sciences
collab_institutions: 
  - UC

# Extra metadata
#   Not in hugo/wowchemy templates
conf_type: 'international'
conf_deadline: '2011-01-10T00:00:00'
contrib_type: 'poster'
contrib_doi: ''
contrib_abstract_url: ''
contrib_abstract_urltitle: ''
---

The explosion of computer power during the last two decades has increased the number and types of computational resources a researcher has access to. The heterogeneity of architectures and systems along with the different configuration schemas has led to a situation where users find very complicated taking advantage of all the resources available.

In order to solve this problem, a new computing paradigm called “Grid Computing” appeared as an alternative for flexible access to heterogeneous and geographically distributed computing resources. Typically, creating a Grid infrastructure requires coordination among cluster administrators and the installation of a middleware to unify the access to them. 

Nowadays, users have access to some resources, like HPC infrastructures, which are not shared using any Grid middleware. Under this situation, the user has to manage separately the access to each non-Grid infrastructure, which is quite cumbersome.

The challenge of this work is to unify the access to Grid and non-Grid resources, allowing researchers to perform huge experiments making use of all the available resources. To achieve this goal, common LRMs used in HPC infrastructures: PBS/Torque, SGE and SLURM and Grid middleware: gLite, GT2.4 and GT4/5 has been considered.

Although nowadays there are several Grid meta-schedulers, none of them has the capabilities needed. To solve the problem of unified access to Grid and non-Grid resources, the GridWay meta-scheduler and his plugin oriented architecture has been used.

Moreover, as Gridway doesn’t provide access to non Grid resources, new GridWay plugins which grant access to non-Grid resources (PBS/Torque, SGE and SLURM) have been developed. These plugins are based on the raw access to clusters provided to the users; typically a ssh account and LRM’s CLI.

As an application of this tool it has been integrated into the WRF4G framework. WRF is high demanding application of HPC resources. WRF4G is a framework that allows the management of the execution of huge experiments, consisting in thousands of jobs (HTC). With this tool we are providing a homogeneous access to Grid and non-Grid resources to the WRF4G users. 

The Earth Sciences community, in particular Climate & Weather community, is high demanding HPC user community, therefore it will benefit from this unification of Grid and non-Grid resources.
