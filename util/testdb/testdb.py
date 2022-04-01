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

import sqlite3

SQLITE_FILE = '../mdmdrupal.sqlite'

conn = sqlite3.connect(SQLITE_FILE)
conn.row_factory = sqlite3.Row  

sql = '''
    SELECT 
        n1.nid                            AS nid     ,
        n1.type                           AS type    ,
        datetime(n1.created, 'unixepoch') AS created ,   
        datetime(n1.changed, 'unixepoch') AS changed ,   
        u1.name                           AS user    ,
        u2.name                           AS user2   ,
        n1.title                          AS contrib_title ,
        r1.body                           AS contrib_body  ,
        t1.field_conf_contrib_type_value  AS contrib_type         ,
        t1.field_urlabstract_url          AS contrib_abstract_url ,
        t1.field_urlabstract_title        AS contrib_abstract_urltitle ,
        f4.field_doi_value                AS contrib_doi, 
        n2.title                          AS conf_title ,
        t2.field_conf_type_value          AS conf_type , 
        f1.field_city_value               AS conf_city ,
        t2.field_country_value            AS conf_country ,
        f2.field_subdeadline_value        AS conf_deadline ,
        t2.field_timeperiod_value         AS conf_startdate ,
        t2.field_timeperiod_value2        AS conf_enddate,
        f3.field_web_url                  AS conf_web ,
        r2.body                           AS conf_body
    FROM 
        node                      n1 
            INNER JOIN
        node_revisions            r1 
            INNER JOIN
        users                     u1
            INNER JOIN
        users                     u2
            INNER JOIN
        content_type_conf_contrib t1
            INNER JOIN
        node                      n2
            INNER JOIN
        node_revisions            r2
            INNER JOIN
        content_type_conference   t2
            INNER JOIN
        content_field_city        f1
            INNER JOIN
        content_field_subdeadline f2
            INNER JOIN
        content_field_web         f3
            LEFT JOIN
        content_field_doi         f4
    ON
        n1.nid                    = r1.nid AND
        n1.uid                    = u1.uid AND
        r1.uid                    = u2.uid AND
        n1.nid                    = t1.nid AND
        t1.field_noderef_conf_nid = n2.nid AND
        t1.field_noderef_conf_nid = r2.nid AND
        t1.field_noderef_conf_nid = t2.nid AND
        t1.field_noderef_conf_nid = f1.nid AND
        t1.field_noderef_conf_nid = f2.nid AND
        t1.field_noderef_conf_nid = f3.nid AND
        t1.field_noderef_conf_nid = f4.nid
    WHERE 
        n1.type = 'conf_contrib'
'''

cur = conn.cursor()
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    print(dict(row))
