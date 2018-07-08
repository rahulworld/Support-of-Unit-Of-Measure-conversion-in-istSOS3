# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0

import asyncio
import istsos
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction
from pint import UnitRegistry, set_application_registry
ureg = UnitRegistry()
set_application_registry(ureg)
Q_ = ureg.Quantity


class UnitConversionPint(CompositeAction):

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
        print('Unit Conversion PostgreSQL unit called')
        print(request.get_rest_data())
        request.set_filter(request.get_rest_data())
        # Adding action Offering retriever
        yield from self.add_retriever_unit_conversion('Offerings')
        # yield from self.add_retriever('Offerings')
        yield from self.add_retriever_unit_conversion('Observations')

    @asyncio.coroutine
    def after(self, request):
        # from_unit=request['json']['from']
        # to_unit=request['json']['to']
        # print(request['observations'])
        recs=request['observations'].copy()
        for rec in recs:
            print('REC Value')
            print(rec[1])
            # change=rec[2]*ureg.kilometers
            # change1=change.to(ureg.meter)
            # change2=change1.magnitude
            # change=rec[1]+"*"+from_unit+"to"+to_unit
            change=str(rec[1])+"*mtocm"
            src, dst = change.split('to')
            change1=Q_(src).to(dst)
            change2=change1.magnitude
            # print(change1)
            ConvertUnit=[]
            ConvertUnit.append({
                "timestamp": str(rec[0]),
                "rainfall": change2
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

    @asyncio.coroutine
    def add_retriever_unit_conversion(self, action, filter=None):
        self.add((yield from get_retrievers_unit_conversion(action, filter=filter)))



@asyncio.coroutine
def get_retrievers_unit_conversion(name, **kwargs):
    action = yield from __get_plugin_proxy(
        'plugins.unit_con_pint.retrievers', name, **kwargs)
    return action


@asyncio.coroutine
def __get_plugin_proxy(istsos_package, action_module, **kwargs):
    from istsos import setting
    import importlib
    state = yield from setting.get_state()
    fileName = action_module[0].lower() + action_module[1:]
    module = 'istsos.%s.%s.%s' % (
        istsos_package,
        state.config["loader"]["type"],
        fileName
    )

    istsos.debug("Importing %s.%s" % (module, action_module))
    try:
        m = importlib.import_module(module)
    except Exception:
        module = 'istsos.%s.%s' % (
            istsos_package,
            fileName
        )
        m = importlib.import_module(module)

    m = getattr(m, action_module)
    if kwargs is not None:
        return m(**kwargs)
    return m()

# @asyncio.coroutine
# def __get_plugin_proxy(istsos_package, action_module, **kwargs):
#     from istsos import setting
#     import importlib
#     state = yield from setting.get_state()
#     fileName = action_module[0].lower() + action_module[1:]
#     module = 'istsos.%s.%s.%s' % (
#         istsos_package,
#         state.config["loader"]["type"],
#         fileName
#     )

#     istsos.debug("Importing %s.%s" % (module, action_module))
#     try:
#         m = importlib.import_module(module)
#     except Exception:
#         module = 'istsos.%s.%s' % (
#             istsos_package,
#             fileName
#         )
#         m = importlib.import_module(module)

#     m = getattr(m, action_module)
#     if kwargs is not None:
#         return m(**kwargs)
#     return m()
