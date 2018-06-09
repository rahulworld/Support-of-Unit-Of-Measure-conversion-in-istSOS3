# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction

#!/usr/bin/python
import psycopg2
from configparser import ConfigParser
import json

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        db = {}
        db["host"]="localhost"
        db["database"]="ist3"
        db["user"]="postgres"
        db["password"]="postgres"
        # read connection parameters
        params = db
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_parts():
    """ query parts from the parts table """
    conn = None
    try:
        db = {}
        db["host"]="localhost"
        db["database"]="ist3"
        db["user"]="postgres"
        db["password"]="postgres"
        # read connection parameters
        params = db
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # cur.execute("SELECT open*'MB/min'::unit@ 'GB/d',close*'m'::unit@ 'km' from bitprice")
        # cur.execute("SELECT array_to_json(array_agg(humidity*'m'::unit@ 'mi')) from obs")
        # cur.execute("SELECT array_to_json(array_agg(obs)) from obs")
        # cur.execute("SELECT array_to_json(array_agg(row(iso8601, humidity))) from obs")
        cur.execute("select row_to_json(t) from (select iso8601, humidity*'m'::unit@ 'mi' from obs) t")
        rows = cur.fetchall()
        # print("The number of parts: ", cur.rowcount)
        # for row in rows:
        #     print(row)
        # print(rows[0])
        # print(type(rows[0]))
        # print(type(rows[0][0]))
        # print(rows[0][0])
        # print("apoov")
        # data_ch = dict(rows[0])
        # print(data_ch)
        cur.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


class UnitConversion(CompositeAction):
    

    @asyncio.coroutine
    def before(self, request):
        yield from self.add_retriever('Uoms')

    @asyncio.coroutine
    def after(self, request):
        connect()
        rows = get_parts()
        # row=rows[0]
        all_data = []
        for i in rows:
            tu = i[0]
            all_data.append(tu)
        # print(get_parts())
        # print(rows)
            # print(tu)
            # print("*"*20)
        # final_dict = get_parts()
        # all_keys = final_dict.keys()
        # new_dict = dict()
        # for key in all_keys:
        #     new_dict[key.strip()] = final_dict[key].strip()

        request['response'] = Response(
            Response.get_template({
                # "data": request['uoms']
                "data" : json.dumps(all_data[0])
                # "data": request['uoms']
            })
        )
