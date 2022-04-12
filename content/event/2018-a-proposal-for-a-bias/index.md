---
title: 'A proposal for a bias correction metadata model in the framework of METACLIP (METAdata for CLImate Products)'

event: '2nd Workshop on Bias Correction in Climate Studies'
event_url: 'http://www.climate-bias-correction.org/'

#location: Venue
address:
#  street: 450 Serra Mall
  city: Santander
#  region: CA
#  postcode: '94305'
  country: Spain

summary: ''
#abstract: ''

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2018-05-14T00:00:00'
date_end: '2018-05-16T00:00:00'
all_day: false
# Schedule page publish date (NOT talk date).
publishDate: '2022-03-24T00:00:00Z'
authors: 
  - joaquin-bedia
  - daniel-san-martin
  - sixto-herrera
  - M. Iturbide
  - jose-manuel-gutierrez
tags: 
  - data provenance
  - metadata
  - bias adjustment
# Is this a featured talk? (true/false)
featured: false

# Image caption
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

url_code: ''
url_pdf: ''
url_slides: 'https://meteo.unican.es/files/posters/METACLIP_poster.pdf'
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
  - VALUE
  - QA4Seas
research_lines: 
  - 
collab_institutions: 
  - IFCA
  - Predictia
  - UC
# Extra metadata
#   Not in hugo/wowchemy templates
conf_type: 'workshop'
conf_deadline: ''
contrib_type: 'poster'
contrib_doi: ''
contrib_abstract_url: ''
contrib_abstract_urltitle: ''
---

Having an effective way of dealing with data provenance is a necessary condition to ensure the reproducibility of results in any scientific domain, and in particular in climate science, helping to build trust and credibility in research outcomes and data products delivered. METACLIP (METAdata for CLImate Products) is a language-independent framework envisaged to tackle the problem of climate product provenance description. The solution proposed is based on semantics exploiting web standard Resource Description Framework (RDF), through the design of domain-specific extensions of standard vocabularies (e.g. PROV-O) describing the different aspects involved in climate product generation. By introducing semantics in the metadata description, METACLIP ensures an effective communication of the information to a wide range of users with different levels of expertise. We present the METACLIP Framework through a bias correction example application within the open source R computing environment and in the context of climate4R, a bundle of climate-oriented R packages, in which a full RDF semantic description of the different elements composing a bias correction product (a climate index future climatology) is produced. A specific on-line application for metadata visualization and interactive exploration is also presented, helping all types of users to trace and understand the provenance of the climate data products. A conceptual framework for the development of a specific bias correction vocabulary is proposed, and a call is done to the community of bias correction experts for possible contributions.
