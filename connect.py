#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:13:54 2019

@author: ZiyingZhang
"""

import logging
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement


log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)


KEYSPACE = "mykeyspace"
def createKeySpace():
   cluster = Cluster(contact_points=['127.0.0.1'],port=9042)
   #定义cluster函数 连接的点为本地，端口9042
   session = cluster.connect() 
   #把程序与cassandra容器连接在一起
   log.info("Creating keyspace...")
   try:       
       session.execute("""
           CREATE KEYSPACE %s
           WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
           """ % KEYSPACE)
       log.info("setting keyspace...")
       session.set_keyspace(KEYSPACE)
       
       log.info("creating table...")
       session.execute("""
           CREATE TABLE mytable (
              filename text,
              result text,
              uploadtime timestamp,
              PRIMARY KEY (filename,result)
           )
           """)
           
   except Exception as err:
       log.error("Unable to create table")
       log.error(err)



def insertData(filename, result, uploadtime):
    cluster = Cluster(contact_points=['127.0.0.1'], port=9042)
    session = cluster.connect(KEYSPACE)
    
    try:
        log.info("Inserting data...")
        session.execute(""" 
            INSERT INTO mytable (filename, result, uploadtime)
            VALUES(%s, %s, %s);
            """, (filename, result, uploadtime))
    except Exception as err:
        log.error("Unable to insert table")
        log.error(err)
        
createKeySpace();