---
title: 'Aplicación de Métodos de Clasificación al Downscaling Estadístico'

event: 'V Simposio Nacional de Predicción'
event_url: ''

#location: Venue
address:
#  street: 450 Serra Mall
  city: Madrid
#  region: CA
#  postcode: '94305'
  country: Spain

summary: ''
#abstract: ''

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2001-11-20T00:00:00'
date_end: '2001-11-23T00:00:00'
all_day: false
# Schedule page publish date (NOT talk date).
publishDate: '2022-03-24T00:00:00Z'
authors: 
  - R. Ancell
  - antonio-s-cofino
  - jose-manuel-gutierrez
  - M.A. Rodríguez
tags: 
  - Statistical downscaling
# Is this a featured talk? (true/false)
featured: false

# Image caption
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
#  focal_point: Right

url_code: ''
url_pdf: 'https://meteo.unican.es/files/private/2001_Ancell_Vsimp.pdf'
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
projects: 
  - Statistical downscaling techniques for different forecast ranges
research_lines: 
  - Statistical downscaling and local weather forecast
collab_institutions: 
  - AEMET
  - UC
# Extra metadata
#   Not in hugo/wowchemy templates
conf_type: 'national'
conf_deadline: ''
contrib_type: 'oral'
contrib_doi: ''
contrib_abstract_url: ''
contrib_abstract_urltitle: ''
---

En este artículo se analizan diversas alternativas para la predicción probabilística de meteoros utilizando el método de análogos, y se presentan resultados de validación en la red principal de estaciones del INM en las diversas cuencas peninsulares. En primer lugar se comparan distintas especificaciones (tamaño de la rejilla y rango horario) del vector 4D que define el “estado de la atmósfera” en base a las predicciones de un modelo numérico. Seguidamente, se describe la forma más conveniente de comprimir esta información, eliminando redundancias, utilizando componentes principales. A continuación, se analizan distintas técnicas de clasificación para obtener un conjunto de estados de la atmósfera análogos a uno dado, de entre aquellos disponibles en una base de datos de estados históricos (reanálisis). Finalmente, se muestra la forma de mejorar la resolución de una predicción realizada por el modelo numérico a partir de la estadística de los meteoros locales observados en las fechas correspondientes a los análogos hallados para el estado definido por la predicción.
