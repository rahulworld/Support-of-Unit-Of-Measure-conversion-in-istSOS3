# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction

#!/usr/bin/python
import psycopg2
# from config import config

#!/usr/bin/python
from configparser import ConfigParser

# def config(filename='database.ini', section='postgresql'):
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)
 
#     # get section, default to postgresql
    
#     if parser.has_section(section):
        
#         # params = parser.items(section)
#         # for param in params:
#         #     db[param[0]] = param[1]
#     else:
#         raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
#     return db

REST_API = {

    #  FETCH API
    "FETCH_OFFERINGS": (
        'list.offerings',
        'Offerings'
    ),
    "FETCH_SENSORS": (
        'list.offerings',
        'Offerings'
    ),
    "FETCH_OBSERVABLE_PROPERTIES": (
        'list.observableProperties',
        'ObservableProperties'
    ),
    "FETCH_OBSERVATION_TYPES": (
        'list.observationTypes',
        'ObservationTypes'
    ),
    "FETCH_UOMS": (
        'list.uoms',
        'Uoms'
    ),
    "FETCH_SAMPLING_TYPES": (
        'list.samplingTypes',
        'SamplingTypes'
    ),
    "FETCH_FOIS": (
        'list.featureOfInterests',
        'FeatureOfInterests'
    ),
    "FETCH_DOMAINS": (
        'list.domains',
        'Domains'
    ),
    "FETCH_CATEGORIES": (
        'list.categories',
        'Categories'
    ),
    "FETCH_MATERIALS": (
        'list.materials',
        'Materials'
    ),
    "FETCH_SAMPLING_METHODS": (
        'list.samplingMethods',
        'SamplingMethods'
    ),
    "FETCH_HUMANS": (
        'list.humans',
        'Humans'
    ),
    "FETCH_PROCESSING_DETAILS": (
        'list.processingDetails',
        'ProcessingDetails'
    ),
    "FETCH_OBSERVATIONS": (
        'list.observations',
        'Observations'
    )
}

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        db = {}
        db["host"]="localhost"
        db["database"]="rahul"
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
        db["database"]="rahul"
        db["user"]="postgres"
        db["password"]="postgres"
        # read connection parameters
        params = db
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # cur.execute("SELECT open*'MB/min'::unit@ 'GB/d',close*'m'::unit@ 'km' from bitprice")
        cur.execute("SELECT open*'m'::unit@ 'mi' from bitprice")
        rows = cur.fetchall()
        # print("The number of parts: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
        # return rows
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
        print(get_parts())
        request['response'] = Response(
            Response.get_template({
                # "data": request['uoms']
                # data1 = jsonify(result = json_data)
                "data": request['uoms']
            })
        )










curl -d '{"action":"UNIT_CONVERSION","from":"m","to":"mi"}' -H "Content-Type: application/json" -X POST http://localhost:8887/rest














# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction

#!/usr/bin/python
import psycopg2
# from config import config

#!/usr/bin/python
from configparser import ConfigParser

# def config(filename='database.ini', section='postgresql'):
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)
 
#     # get section, default to postgresql
    
#     if parser.has_section(section):
        
#         # params = parser.items(section)
#         # for param in params:
#         #     db[param[0]] = param[1]
#     else:
#         raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
#     return db

REST_API = {

    #  FETCH API
    "FETCH_OFFERINGS": (
        'list.offerings',
        'Offerings'
    ),
    "FETCH_SENSORS": (
        'list.offerings',
        'Offerings'
    ),
    "FETCH_OBSERVABLE_PROPERTIES": (
        'list.observableProperties',
        'ObservableProperties'
    ),
    "FETCH_OBSERVATION_TYPES": (
        'list.observationTypes',
        'ObservationTypes'
    ),
    "FETCH_UOMS": (
        'list.uoms',
        'Uoms'
    ),
    "FETCH_SAMPLING_TYPES": (
        'list.samplingTypes',
        'SamplingTypes'
    ),
    "FETCH_FOIS": (
        'list.featureOfInterests',
        'FeatureOfInterests'
    ),
    "FETCH_DOMAINS": (
        'list.domains',
        'Domains'
    ),
    "FETCH_CATEGORIES": (
        'list.categories',
        'Categories'
    ),
    "FETCH_MATERIALS": (
        'list.materials',
        'Materials'
    ),
    "FETCH_SAMPLING_METHODS": (
        'list.samplingMethods',
        'SamplingMethods'
    ),
    "FETCH_HUMANS": (
        'list.humans',
        'Humans'
    ),
    "FETCH_PROCESSING_DETAILS": (
        'list.processingDetails',
        'ProcessingDetails'
    ),
    "FETCH_OBSERVATIONS": (
        'list.observations',
        'Observations'
    )
}

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
        print(rows)
        cur.close()
        # return rows
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
        print(get_parts())
        request['response'] = Response(
            Response.get_template({
                # "data": request['uoms']
                # data1 = jsonify(result = json_data)
                "data": request['uoms']
            })
        )
