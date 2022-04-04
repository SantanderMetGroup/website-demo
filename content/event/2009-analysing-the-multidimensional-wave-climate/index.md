---
title: 'Analysing the multidimensional wave climate with self  organizing maps'

event: 'OCEANS ´09 IEEE, Balancing technology with future needs '
event_url: http://www.oceans09ieeebremen.org/

#location: Venue
address:
#  street: 450 Serra Mall
  city: Bremen
#  region: CA
#  postcode: '94305'
  country: Germany

summary: ''
#abstract: ''

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2009-05-11T00:00:00
date_end: 2009-05-14T00:00:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2022-03-24T00:00:00Z'

authors: 
  - F. Méndez
  - P. Camus
  - R. Medina
  - antonio-s-cofino
tags: 
  - Data mining
  - Self-Organizing Maps
  - Wave Climate

# Is this a featured talk? (true/false)
featured: false

# Image caption
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

url_code: ''
url_pdf: 'files/private/2009_Oceans_Mendez.pdf'
url_slides: 'None'
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
conf_type: international
conf_deadline: 2009-01-11T00:00:00
contrib_type: oral
contrib_entities: ['UC', 'Instituto de Hidráulica de Cantabria (IHC)']
contrib_doi: None
contrib_abstract_url: 
contrib_abstract_urltitle: 
---

The  term  “wave  climate”  usually  refers  to  the  statistical  distribution  of  several oceanographical geophysical variables. Components of  the wave  climate are variables such as wind velocity, W, wind direction, θW, significant wave height, Hs, peak period, Tp,  and  mean  wave  direction,  θ.  Usually,  the  classical  analysis  of  the  long-term distribution  of  wave  climate  is  addressed  using  just  one  variable  (f.i.,  long-term distribution  of  significant  wave  height)  or  at  most  bidimensionally  (f.i.,  the bidimensional distribution of Hs and Tp). It is clear that the joint probability distribution of these five variables (Hs, Tp, θ, W, θW) is not easy to able to cope with. However, this problem  is  solved  applying  a  non-linear  clustering  algorithm,  namely  the  Self Organizing Maps  (SOM),  a  neural  network  technique  capable  of  classifying  the  high dimensional input reanalysis data in a low number of centroids (clusters) in an ordered sheet shape representation (Camus et al, 2007). The neurons are connected  to adjacent elements  by  a  neighbourhood  relation. A multidimensional  histogram  of  the  sea  state parameters is obtained allowing an easy further treatment of the classified sea states.  
 
Figure  1  shows  a  23x23  SOM  applied  to  a  particular  site  located  in Villano, Galicia (Spain). In this case, the original data space has been projected into a toroid lattice being the data  accommodated  in  a  circular way. This  toroid  shape has been  again projected into  the  plane  for  a  better  visualization,  separating  the  centroids  which  are  located together, the centroids located in the upper side of the sheet are joined with the centroids 
located on  the  lower  side of  the  sheet and with  the  lateral  sides  in  the 3D-dimension. Each cell of  the SOM  represents a cluster defined by  the  five parameters employed  in the classification. The significant wave height,  the wave period and  the wave direction are represented by the size, the colour intensity and the direction of the arrow; the pink arrow represents the wind vector. The background of each hexagon has been filled in a blue scale, function of the frequency of occurrence. As it can be seen in the figure, this classification  technique  is  capable  of  extracting  all  the  possible  sea  states  and  the transition between  them. The magnitudes of  the parameters which define  the centroids vary smoothly from one cell to another. The most energetic sea states present W-WNW 
directions  (i=17,  j=14).  The  higher  amount  of  data  is  grouped  in  clusters  with  low energy sea states (i=6, j=11). 
 
Figure 2 shows several SOMs for different locations along the northern coast of Spain. In this case, we are considering (Hs, Tp, θ)   and a 10x10 SOM. In the presentation, the theoretical  basis  and  some  examples  will  show  the  ability  of  this  methodology  to describe the multidimensional wave climate.
