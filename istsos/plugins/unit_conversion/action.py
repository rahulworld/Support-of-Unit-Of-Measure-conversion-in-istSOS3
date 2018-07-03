import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction


class UNIT_CON_POSTApi(CompositeAction):

    @asyncio.coroutine
    def before(self, request):
        json = request.get_json()
        # if 'message' in json:
        #     request['message'] = json['message']
        yield from self.add_plugin("unit_conversion", "UnitConversion")

    @asyncio.coroutine
    def after(self, request):
        request['response'] = Response(
            # json_source=Response.get_template({
            #     "message": request["message"]
            # })
        )