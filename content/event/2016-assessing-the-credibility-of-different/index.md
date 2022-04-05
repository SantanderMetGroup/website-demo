---
title: 'Assessing the credibility of different species distribution models to project changes under future climate conditions'

event: 'EcoSummit 2016 Ecological Sustainability: Engineering Change'
event_url: 'http://www.ecosummit2016.org/'

#location: Venue
address:
#  street: 450 Serra Mall
  city: Montpellier
#  region: CA
#  postcode: '94305'
  country: France

summary: ''
#abstract: ''

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2016-08-29T00:00:00'
date_end: '2016-09-01T00:00:00'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2022-03-24T00:00:00Z'

authors: 
  - M. Iturbide
  - joaquin-bedia
  - jose-manuel-gutierrez
tags: 
  - species distribution models

# Is this a featured talk? (true/false)
featured: false

# Image caption
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

url_code: ''
url_pdf: 'https://meteo.unican.es/files/pdfs/ecosummit_iturbide.pdf'
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
conf_deadline: '2016-02-01T00:00:00'
contrib_type: 'oral'
contrib_institutions: 
  - IFCA
contrib_research_lines: 
  - Climate change and regional scenarios
contrib_doi: ''
contrib_abstract_url: ''
contrib_abstract_urltitle: ''
---

Species Distribution Models (SDMs) are widely applied to estimate future impacts on species distributions and assess key topics in environmental conservation. Future projections vary significantly depending on model algorithms and parameterizations, however, the evaluation of SDMs under future climate change is problematic, as events being predicted have yet not occurred. In front of the lack of an objective basis to perform a selection of various alternatives,  we propose a method incorporating niche overlap metrics, for the selection of credible future projections under an ecologically meaningful basis. This method allows the discrimination of useful SDMs from ill-performing ones. In addition, given that the pseudo-absences used to train the model are known to have a significant impact on the results obtained, we analyse this source of uncertainty in future projections for each tested SDM. 

We apply the developed method on three phylogenies of pedunculate oak (Quercus robur L.) in Europe, considering three different modelling algorithms and a set of four state of the art regional-global climate model couplings , thus accounting for the main sources of uncertainty of future SDM projections. Finally, we calculate the range of probabilities of future projections obtained from models built for 10 runs of pseuso-absence data generation. Two pseudo-absence generation methods are compared, the commonly used random sampling (RS) and the improved Three-step method (TS).

The niche overlap metric approach enabled an objective quality assessment of each individual SDM. The less complex algorithm (GLM) produced the most credible future projections. Contrarily, MARS (and to a lesser extent also MAXENT) projected the less credible future distributions due to model overfitting. The uncertainty related to pseudo-absence data was also lower for GLM, specially when the TS method was used. Therefore, we conclude that the use of a parsimonious algorithm is the best option in the context of future predictions.
