# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.actions.retrievers.unitConversion import UnitConversion


# class UnitConversion(UnitConversion):
#     @asyncio.coroutine
#     def process(self, request):
#         with (yield from request['state'].pool.cursor()) as cur:
#             sql = """
#                 SELECT rainfall, humidity, temperature, velocity
#                 FROM obs;
#             """
#             yield from cur.execute(sql)
#             request['unit_conversion'] = []
#             recs = yield from cur.fetchall()
#             for rec in recs:
#                 request['unit_conversion'].append({
#                     "rainfall": rec[0],
#                     "humidity": rec[1],
#                     "temperature": rec[2],
#                     "velocity": rec[3]
#                 })
#         print("aipog Unit Conversion in Database Query")


# class UnitConversion(UnitConversion):
#     @asyncio.coroutine
#     def process(self, request):
#         with (yield from request['state'].pool.cursor()) as cur:
#             sql = """
#                 SELECT iso8601, rainfall, humidity, temperature, velocity
#                 FROM obs;
#             """
#             yield from cur.execute(sql)
#             request['unit_conversion'] = []
#             recs = yield from cur.fetchall()
#             for rec in recs:
#                 request['unit_conversion'].append({
#                     "timestamp": str(rec[0]),
#                     "rainfall": float(rec[1]),
#                     "humidity": float(rec[2]),
#                     "temperature": float(rec[3]),
#                     "velocity": float(rec[4])
#                 })
#         print("aipog Unit Conversion in Database Query")

class UnitConversion(UnitConversion):
    @asyncio.coroutine
    def process(self, request):
        with (yield from request['state'].pool.cursor()) as cur:
            from_unit=request['json']['from']
            to_unit=request['json']['to']
            sql1="""CREATE EXTENSION IF NOT EXISTS unit;"""
            yield from cur.execute(sql1)
            sql = """
                SELECT iso8601, rainfall, humidity*'"""+from_unit+"""'::unit@ '"""+to_unit+"""', temperature, velocity
                FROM obs;
            """
            yield from cur.execute(sql)
            request['unit_conversion'] = []
            recs = yield from cur.fetchall()
            for rec in recs:
                request['unit_conversion'].append({
                    "timestamp": str(rec[0]),
                    "rainfall": float(rec[1]),
                    "humidity": rec[2],
                    "temperature": float(rec[3]),
                    "velocity": float(rec[4])
                })
        print("aipog Unit Conversion in Database Query")
