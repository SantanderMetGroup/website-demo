---
title: 'Assessing the drift of seasonal forecasts'

event: 'EGU General Assembly 2014'
event_url: 'http://www.egu2014.eu/'

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
date: '2014-04-27T00:00:00'
date_end: '2014-05-02T00:00:00'
all_day: false
# Schedule page publish date (NOT talk date).
publishDate: '2022-03-24T00:00:00Z'
authors: 
  - rodrigo-manzanas
  - jesus-fernandez
  - m-eugenia-magarino
  - jose-manuel-gutierrez
  - F.J. Doblas-Reyes
  - G. Nikulin
  - C. Buontempo
tags: 
  - Drift
  - Seasonal climate prediction
# Is this a featured talk? (true/false)
featured: false

# Image caption
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

url_code: ''
url_pdf: 'https://meteo.unican.es/files/pdfs/2014_Manzanas_EGU_Viena_abstract.pdf'
url_slides: 'https://meteo.unican.es/files/posters/2014_Manzanas_EGU_Viena_poster.pdf'
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
  - EUPORIAS
  - SPECS
research_lines: 
  - Seasonal forecasting
collab_institutions: 
  - IFCA
  - UC
  - IC3
  - SMHI
  - UK Met Office
# Extra metadata
#   Not in hugo/wowchemy templates
conf_type: ''
conf_deadline: '2014-01-16T00:00:00'
contrib_type: 'poster'
contrib_doi: ''
contrib_abstract_url: ''
contrib_abstract_urltitle: ''
---

The systematic drift (bias dependence on the forecast lead-time) present in state-of-the-art coupled general circulation models is an inherent feature of global seasonal forecasts. Usually, anomalies (relative to the model climatology) obtained from an ensemble of hindcasts are used to correct this drift. However, this procedure has not been systematically explored across different forecasting systems so far. Moreover, costly approaches for seasonal impacts forecasting, such as dynamical downscaling, would benefit from  drift removal strategies involving smaller ensemble sizes.

The full thirty-year (1981-2010) hindcast of the System 4 ECWMF (in particular the 15-members seasonal experiment) was considered to address these issues over two regions of interest for the EU project EUPORIAS, Europe and East Africa. The mean climatology for each calendar month was computed at seven different lead-times (each member was initialized the first of each month and was run for seven months). For instance,the climatology of January was computed considering the forecasts initialized the first of January (lead-month 0), December (lead-month 1) and so on until July (lead-month 6). Results show important drifts for some cases. Moreover, the differences between members are statistically not significant in general, what suggests that considering a single member may be enough to robustly remove the drift.

In the near future, additional forecasting systems involved in EUPORIAS will be compared with System 4 in order to unveil possible commonalities in the drift climatology.
