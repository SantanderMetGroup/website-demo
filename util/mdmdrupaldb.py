#!/usr/bin/env python3

# https://sqlite.org/lang_datefunc.html


# CREATE TABLE "content_type_conf_contrib" (
#	"vid" INTEGER NOT NULL DEFAULT '0' ,
#	"nid" INTEGER NOT NULL DEFAULT '0' ,
#	"field_conf_contrib_type_value" TEXT NULL  ,
#	"field_urlabstract_url" VARCHAR(255) NOT NULL DEFAULT '' ,
#	"field_urlabstract_title" VARCHAR(255) NOT NULL DEFAULT '' ,
#	"field_urlabstract_attributes" TEXT NULL  ,
#	"field_noderef_conf_nid" INTEGER NOT NULL DEFAULT '0' ,
#	"field_posterpdf_fid" INTEGER NOT NULL DEFAULT '0' ,
#	"field_posterpdf_description" VARCHAR(255) NOT NULL DEFAULT '' ,
#	"field_posterpdf_list" INTEGER NOT NULL DEFAULT '0' ,
#	"field_nodepublication_nid" INTEGER NOT NULL DEFAULT '0' ,
#	"field_citadetalles_value" TEXT NULL  ,
#	"field_conference_computed_value" TEXT NULL  ,
#	PRIMARY KEY ("vid")
#)

#SELECT field_name,widget_type FROM node_field_instance WHERE type_name='conf_contrib'
#    field_noderef_conf	nodereference_select
#    field_authors             cck_taxonomy_2
#    field_conf_contrib_type   options_select
#    field_year                number
#    field_urlabstract         link
#    field_pdf_file            file
#    field_posterpdf           file
#    field_nodepublication     nodereference_autocomplete
#    field_citadetalles        text
#    field_noderef_proj        nodereference_select
#    field_noderef_resact      nodereference_select
#    field_conference_computed computed
#    field_doi                 text

#SELECT field_name,widget_type FROM node_field_instance WHERE type_name='conference'
#    field_country       text
#    field_city          text
#    field_web	         link
#    field_subdeadline   date_select
#    field_conf_type     options_select
#    field_timeperiod    date_select
#    field_contributions computed
#    field_noderef_proj  nodereference_select

SQLITE_FILE = './mdmdrupal.sqlite'

CONTRIB_SQL = '''
  SELECT 
    n1.nid                            AS nid     ,
    n1.type                           AS type    ,
    datetime(n1.created, 'unixepoch') AS created ,   
    datetime(n1.changed, 'unixepoch') AS changed ,   
    u1.name                           AS user    ,
    n1.title                          AS contrib_title ,
    r1.body                           AS contrib_body  ,
    t1.field_conf_contrib_type_value  AS contrib_type         ,
    t1.field_urlabstract_url          AS contrib_abstract_url ,
    t1.field_urlabstract_title        AS contrib_abstract_urltitle ,
    f5.field_year_value               AS contrib_year,
    f4.field_doi_value                AS contrib_doi,
    f6.filepath                       AS 'contrib_poster-talk_file',
    f8.filepath                       AS 'contrib_pdf_file',
    n2.title                          AS conf_title ,
    t2.field_conf_type_value          AS conf_type , 
    f1.field_city_value               AS conf_city ,
    t2.field_country_value            AS conf_country ,
    f2.field_subdeadline_value        AS conf_deadline ,
    t2.field_timeperiod_value         AS conf_startdate ,
    t2.field_timeperiod_value2        AS conf_enddate,
    f3.field_web_url                  AS conf_web ,
    r2.body                           AS conf_body
  
  FROM      node                      n1 
  LEFT JOIN node_revisions            r1 
    ON n1.nid = r1.nid
  LEFT JOIN users                     u1
    ON n1.uid = u1.uid
  LEFT JOIN content_type_conf_contrib t1
    ON n1.nid = t1.nid
  LEFT JOIN node                      n2
    ON t1.field_noderef_conf_nid = n2.nid
  LEFT JOIN node_revisions            r2
    ON t1.field_noderef_conf_nid = r2.nid
  LEFT JOIN content_type_conference   t2
    ON t1.field_noderef_conf_nid = t2.nid
  LEFT JOIN content_field_city        f1
    ON t1.field_noderef_conf_nid = f1.nid
  LEFT JOIN content_field_subdeadline f2
    ON t1.field_noderef_conf_nid = f2.nid
  LEFT JOIN content_field_web         f3
    ON t1.field_noderef_conf_nid = f3.nid
  LEFT JOIN content_field_doi         f4
    ON n1.nid = f4.nid
  LEFT JOIN content_field_year        f5
    ON n1.nid = f5.nid
  LEFT JOIN files                     f6
    ON t1.field_posterpdf_fid = f6.fid
  LEFT JOIN content_field_pdf_file    f7
    ON n1.nid = f7.nid
  LEFT JOIN files                     f8
    ON f7.field_pdf_file_fid = f8.fid
  WHERE 
    n1.type = 'conf_contrib'
'''

#field_authors
# vid=2 -> author vocabulary
AUTHORS_SQL='''
	SELECT t.tid,name
	FROM term_node t LEFT JOIN term_data d
    ON t.tid=d.tid
  WHERE 
    d.vid = 2    AND
    nid   = :nid
  ORDER BY t.orden
'''
#field_entities
# vid=3  -> Institutions vocabulary
# vid=12 -> Collab. entities vocabulary
ENTITIES_SQL='''
	SELECT t.tid,name
	FROM term_node t LEFT JOIN term_data d
    ON t.tid=d.tid
  WHERE 
    ( d.vid = 3 OR d.vid = 12 ) AND
    nid   = :nid
  ORDER BY d.vid, t.orden
'''

#field_keywords
# vid=8 -> keywords vocabulary
KEYWORDS_SQL='''
	SELECT t.tid,name
	FROM term_node t LEFT JOIN term_data d
    ON t.tid=d.tid
  WHERE 
    d.vid = 8    AND
    nid   = :nid
  ORDER BY t.orden
'''

#field_projects
PROJECTS_SQL='''
  SELECT n1.nid, n1.title AS name
  FROM content_field_noderef_proj p INNER JOIN node n1
    ON p.field_noderef_proj_nid = n1.nid
  WHERE 
    p.nid = :nid
'''

#field_research
RESEARCH_SQL='''
  SELECT n1.nid, n1.title AS name
  FROM content_field_noderef_resact p INNER JOIN node n1
    ON p.field_noderef_resact_nid = n1.nid
  WHERE 
    p.nid = :nid
'''


#SELECT field_name,widget_type FROM node_field_instance WHERE type_name='staff'
#field_name	            text
#field_personal_picture	image
#field_telephone	        text
#field_mobile	          text
#field_position	        text
#field_emailuser	        text
#field_surname	          text
#field_emaildomain	      text
#field_web	              link
#field_stafftype	        options_select

#STAFF_SQL
STAFF_SQL = '''
  SELECT 
    n1.nid                            AS nid     ,
    n1.type                           AS type    ,
    datetime(n1.created, 'unixepoch') AS created ,   
    datetime(n1.changed, 'unixepoch') AS changed ,   
    u1.name                           AS user    ,
    n1.title                          AS staff_title ,
    t1.field_name_value               AS staff_name ,
    t1.field_surname_value            AS staff_surname ,
    t1.field_position_value           AS staff_position ,
    t1.field_stafftype_value          AS staff_stafftype ,
    f6.filepath                       AS staff_personal_picture_file,
    t1.field_emaildomain_value        AS staff_emaildomain,
    t1.field_emailuser_value          AS staff_emailuser,
    t1.field_telephone_value          AS staff_telephone,
    f3.field_web_url                  AS staff_web,
    r1.body                           AS staff_body  
  FROM      node                      n1 
  LEFT JOIN node_revisions            r1 
    ON n1.nid = r1.nid
  LEFT JOIN users                     u1
    ON n1.uid = u1.uid
  LEFT JOIN content_type_staff        t1
    ON n1.nid = t1.nid
  LEFT JOIN content_field_web         f3
    ON n1.nid = f3.nid
  LEFT JOIN files                     f6
    ON t1.field_personal_picture_fid = f6.fid
  WHERE 
    n1.type = 'staff'
'''




import sqlite3

CONN = sqlite3.connect(SQLITE_FILE)
CONN.row_factory = sqlite3.Row  

def populate_from_query(contrib, sql, field):
  # Empty list just in case there is not values
  contrib[field] = [] 
  for row in CONN.execute(sql, contrib):
    dic = dict(row)
    contrib[field].append(dic['name'])

def CONTRIBUTIONS():
  for contrib_row in CONN.execute(CONTRIB_SQL):
    contrib = dict(contrib_row)
    ## Populate authors
    populate_from_query(contrib, AUTHORS_SQL,  'contrib_authors' )
    ## Populate entities and institutions
    populate_from_query(contrib, ENTITIES_SQL, 'contrib_entities')
    ## Populate KEYWORDS
    populate_from_query(contrib, KEYWORDS_SQL, 'contrib_keywords')
    ## Populate projects
    populate_from_query(contrib, PROJECTS_SQL, 'contrib_projects')
    ## Populate research activities
    populate_from_query(contrib, RESEARCH_SQL, 'contrib_research')
    yield contrib

def STAFF():
  for staff_row in CONN.execute(STAFF_SQL):
    person = dict(staff_row)
    ## Populate authors
    yield person


## Example
if __name__ == '__main__':
  import pprint
  
  for contrib in CONTRIBUTIONS():
    pprint.pprint(contrib)
  
  for person in STAFF():
    pprint.pprint(person)

