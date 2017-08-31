# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:20:49 2017

@author: nguyenb
"""
import pandas as pd
import cx_Oracle

connection = cx_Oracle.connect('unidb/fnRjn5LLuuZLAJLQLuQr@//amz-p-ora20.dbrs.local:1521/BRAPP')
cursor = connection.cursor()

def runscript(script):
    try:
        cursor.execute(script)
        x = pd.DataFrame(cursor.fetchall())
        x.columns = [x[0] for x in cursor.description]
        return x
    except:
        print('FAILED')
        pass


script1 = 'select distinct action from all_rating_event_report_vw'
x = runscript(script1)

print(x)