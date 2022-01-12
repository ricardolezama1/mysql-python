
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:15:07 2021

@author: Ricardo Lezama

"""


import requests
import os
import json 

import sys

import pymysql
from pymysql.converters import escape_string


  
def inserta( data1, data2 ):
    """
    The function 'inserta' is a manner in which to upload
    """
    from datetime import datetime
        #datetime object containing current date and time
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        conn = pymysql.connect(host='MYSQLHOST.com', user='username', passwd='password', db='somedb')
        cur = conn.cursor()
        #Inserta en tabla posts
        b
        query = "INSERT INTO somedb VALUES('"+ timestamp +"','"+ data1+"','"+ data2 +"');"
        print (query )
        #printing confirms the value of the result. 
        cur.execute(query)
        conn.commit() 
    except pymysql.Error as e:
        print("No se pudo conectar a testdb: ", e)
        sys.exit(1)
