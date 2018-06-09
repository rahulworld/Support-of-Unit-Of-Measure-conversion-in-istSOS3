# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.actions.retrievers.unitConversion import UnitConversion


class UnitConversion(UnitConversion):
    @asyncio.coroutine
    def process(self, request):
        with (yield from request['state'].pool.cursor()) as cur:
            sql = """
                SELECT rainfall, humidity, temperature, velocity
                FROM obs;
            """
            yield from cur.execute(sql)
            request['unit_conversion'] = []
            recs = yield from cur.fetchall()
            for rec in recs:
                request['unit_conversion'].append({
                    "rainfall": rec[0],
                    "humidity": rec[1],
                    "temperature": rec[2],
                    "velocity": rec[3]
                })
        print("aipog Unit Conversion in Database Query")


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
#                     "timestamp": rec[0],
#                     "rainfall": rec[1],
#                     "humidity": rec[2],
#                     "temperature": rec[3],
#                     "velocity": rec[4]
#                 })
#         print("aipog Unit Conversion in Database Query")
