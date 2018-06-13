# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
# import pint
from istsos.actions.retrievers.unitConversionPint import UnitConversionPint
from pint import UnitRegistry, set_application_registry
ureg = UnitRegistry()
set_application_registry(ureg)
Q_ = ureg.Quantity

class UnitConversion_Pint(UnitConversionPint):
    @asyncio.coroutine
    def process(self, request):
        with (yield from request['state'].pool.cursor()) as cur:
            from_unit=request['json']['from']
            to_unit=request['json']['to']
            sql = """
                SELECT iso8601, rainfall, humidity, temperature, velocity
                FROM obs;
            """
            yield from cur.execute(sql)
            request['unit_conversion_pint'] = []
            recs = yield from cur.fetchall()
            for rec in recs:
                # change=rec[2]*ureg.kilometers
                # change1=change.to(ureg.meter)
                # change2=change1.magnitude
                change=str(rec[2])+"*"+from_unit+"to"+to_unit
                src, dst = change.split('to')
                change1=Q_(src).to(dst)
                change2=change1.magnitude
                # print(change1)
                request['unit_conversion_pint'].append({
                    "timestamp": str(rec[0]),
                    "rainfall": float(rec[1]),
                    "humidity": float(change2),
                    "temperature": float(rec[3]),
                    "velocity": float(rec[4])
                })
        print("aipog Unit Conversion in Database Query")
