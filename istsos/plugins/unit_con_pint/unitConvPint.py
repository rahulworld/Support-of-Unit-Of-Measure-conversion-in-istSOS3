import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction
from pint import UnitRegistry, set_application_registry
ureg = UnitRegistry(autoconvert_offset_to_baseunit = True)
set_application_registry(ureg)
Q_ = ureg.Quantity



class UnitConvPint(CompositeAction):

    @asyncio.coroutine
    def before(self, request):
        """
        Request example: {
            "action": "UNIT_CON_POST",
            "data": {
                "offerings": ["belin","belin"],
                "observedProperties": [
                    "urn:ogc:def:parameter:x-istsos:1.0:temperature"
                ],
                "temporal": {
                    "reference": "om:phenomenonTime",
                    "fes": "during",
                    "period": [
                        "2015-05-03T16:30:00.000000+0200",
                        "2015-06-03T16:30:00.000000+0200"
                    ]
                },
                "responseFormat": "application/json;subtype='array'"
            },
            "in_unit":"°F"
        }
        """
        yield from self.add_plugin("unit_con_pint", "UnitConversionPint")

    @asyncio.coroutine
    def after(self, request):
        from_unit=request['json']['data']['from_unit']
        to_unit=request['json']['data']['to_unit']
        # time=request['json']['headers'][0]['column']
        # value=request['json']['headers'][1]['name']
        # from_unit=request['headers'][1]['uom']
        # to_unit=request['json']['to']
        # print(request['observations'])
        recs=request['observations'].copy()
        ConvertUnit=[]
        for rec in recs:
            # change=rec[1]*ureg.kilometers
            # change1=change.to(ureg.meter)
            # change2=change1.magnitude
            change=str(rec[1])+"*"+from_unit+"to"+to_unit
            # change=Q_(str(rec[1]), ureg.degC).to(ureg.kelvin)
            # change=str(rec[1])+"*degC"+"to"+"degF"
            # change=str(rec[1])+"*ureg.degC"+"to"+"ureg.degF"
            # change=rec[1]*ureg.degC
            # change=str(rec[1])+"* kelvin to degF"
            src, dst = change.split('to')
            change1=Q_(src).to(dst)
            # home = Q_(rec[1], ureg.degC)
            # change1=home.to('degF')
            # change1=Q_(rec[1], ureg.degC).to(ureg.kelvin).magnitude
            change2=change1.magnitude
            # print(change2)
            # print(change1)
            ConvertUnit.append({
                "datetime" : rec[0],
                "value": change2
            })
            # request['observations1'].append({
            #     "timestamp": str(rec[0]),
            #     "rainfall": change2
            # })
        request['response'] = Response(
            json_source=Response.get_template({
                "data": ConvertUnit,
                "headers": request['headers']
            })
        )