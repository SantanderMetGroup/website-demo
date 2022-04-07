import frontmatter
import glob

authors_keys = [i.split('/')[-1] for i in glob.glob(f'content/authors/*')]

def authorname(text):
  rval = text
  if text in authors_keys:
    fm = frontmatter.load(f'content/authors/{text}/_index.md')
    rval = fm['short_name'] if 'short_name' in fm else fm['title']
  return(rval)

def authors2bib(lst):
  rval = ' and '.join([authorname(i) for i in lst])
  return(rval)

content_types = ['event']

for ct in content_types:
  mdfiles = glob.glob(f'content/{ct}/*/index.md')
  for mdf in mdfiles:
    bib = mdf.replace('index.md', 'cite.bib')
    print(f'Writing {bib} ...')
    md = frontmatter.load(mdf)
    md['bibkey'] = mdf.split('/')[-2]
    md['bibauthor'] = authors2bib(md['authors'])
    md['bibyear'] = md['date'][0:4]
    with open(bib, 'w') as fp:
      fp.write(
'''
@misc{{{bibkey},
  title = "{title}",
  author = "{bibauthor}",
  year = "{bibyear}",
  type = "{event}",
  URL = "{contrib_abstract_url}",
}}
'''.format(**md)
      )
