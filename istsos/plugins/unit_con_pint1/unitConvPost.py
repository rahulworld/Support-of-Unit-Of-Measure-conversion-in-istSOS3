import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction


class UnitConvPost(CompositeAction):

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
        yield from self.add_plugin("unit_con_post", "Postgresql_unit")

    @asyncio.coroutine
    def after(self, request):
        request['response'] = Response(
            json_source=Response.get_template({
                "data": request['observations'],
                "headers": request['headers']
            })
        )