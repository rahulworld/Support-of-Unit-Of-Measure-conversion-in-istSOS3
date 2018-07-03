import asyncio
from istsos.entity.rest.response import Response
from istsos.actions.action import CompositeAction


class UNIT_CON_POSTApi(CompositeAction):

    @asyncio.coroutine
    def before(self, request):
        json = request.get_json()
        # if 'message' in json:
        #     request['message'] = json['message']
                # Add filters
        request.set_filter(request.get_rest_data())
        # Adding action Offering retriever
        yield from self.add_retriever('Offerings')
        yield from self.add_retriever('Observations')
        # yield from self.add_plugin("unit_conversion", "Observations")

    @asyncio.coroutine
    def after(self, request):
        request['response'] = Response(
            json_source=Response.get_template({
                "data": request['observations'],
                "headers": request['headers']
            })
        )
        # request['response'] = Response(
        #     # json_source=Response.get_template({
        #     #     "message": request["message"]
        #     # })
        # )