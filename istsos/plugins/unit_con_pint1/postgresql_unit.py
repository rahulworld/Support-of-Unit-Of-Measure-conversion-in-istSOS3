# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction


class Postgresql_unit(CompositeAction):

    @asyncio.coroutine
    def process(self, request):
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
        # Add filters
        request.set_filter(request.get_rest_data())
        # Adding action Offering retriever
        yield from self.add_retriever('Offerings')
        yield from self.add_retriever('Observations')

    @asyncio.coroutine
    def after(self, request):
        request['response'] = Response(
            json_source=Response.get_template({
                "data": request['observations'],
                "headers": request['headers']
            })
        )
