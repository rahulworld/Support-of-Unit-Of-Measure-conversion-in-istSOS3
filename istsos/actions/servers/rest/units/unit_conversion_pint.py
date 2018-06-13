# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction



class UnitConversionPint(CompositeAction):
    @asyncio.coroutine
    def before(self, request):
        yield from self.add_retriever('UnitConversion_Pint')

    @asyncio.coroutine
    def after(self, request):
        request['response'] = Response(
            Response.get_template({
                "data": request['unit_conversion_pint']
                # "data" : data1
                # "data": request['uoms']
            })
        )
