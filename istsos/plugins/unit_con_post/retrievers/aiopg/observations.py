# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0
lookups = {
    "°C":["°C", "celcius", "degree Celsius", "degree-celsius", "degree-celsius", "degree", "degree centigrade", "degcelsius", "degC"],
    "°F":["°F", "fahrenheit", "degfahrenheit", "degF", "degfahrenheit", "degree-fahrenheit", "degree fahrenheit"],
    "°K":["°K", "kelvin", "degK", "tempK"],
     }

import asyncio
import istsos
import json
from istsos import setting
from istsos.actions.retrievers.observations import Observations
from istsos.entity.observation import Observation
from istsos.entity.observedProperty import (
    ObservedProperty, ObservedPropertyComplex)



class Observations(Observations):
    """Query an SOS to retrieve observation data structured according to the
O&M specification.

istSOS supports this filters:

temporalFilter:
- during: om:phenomenonTime,
          2012-11-19T14:00:00+01:00/2012-11-19T14:15:00+01:00
- equals: om:phenomenonTime,
          2012-11-19T14:00:00.000+01:00
    """

    @asyncio.coroutine
    def process(self, request):
        """Depending on the selected procedures call its specific retriever to
        query the relatives observed data.

        :param dict state: must contain an object with the queried procedures
        """

        if 'offerings' not in request:
            # A request can also lead to an empty response
            return

        # @todo check if this helps
        if False:  # len(request['offerings']) > 1:
            istsos.debug("Running retrieval in parallel")
            funcs = [
                self.__get_data(
                    offering, request
                ) for offering in request['offerings']
            ]
            yield from asyncio.gather(*funcs)

        else:
            istsos.debug("Running retrieval sequentially")
            if request.get_filter(
                    "responseFormat") in setting._responseFormat['vega']:
                yield from self.__get_kvp(
                    request['offerings'], request)
            elif request.get_filter(
                    "responseFormat") in setting._responseFormat['array']:
                yield from self.__get_array(
                    request['offerings'], request)
            elif request.get_filter(
                    "responseFormat") in setting._responseFormat['array2']:
                yield from self.__get_array_2(
                    request['offerings'], request)
            else:
                for offering in request['offerings']:
                    yield from self.__get_data(offering, request)

        # istsos.debug(request['observations'])
    @asyncio.coroutine
    def findLookUp(self, unit):
        for key, value in lookups.items():
            if str(unit).lower() in (n.lower() for n in value):
                return key

    @asyncio.coroutine
    def __get_array_2(self, offerings, request):

        dbmanager = yield from self.init_connection()
        cur = dbmanager.cur
        op_filter = request.get_filter('observedProperties')
        tables = {}
        columns = []
        ConvertUnit=''
        headers = [{
            "type": "datetime",
            "name": "Phenomenon Time",
            "column": "e"
        }]

        for offering in request['offerings']:
            tName = "_%s" % offering['name'].lower()
            if offering.is_complex():
                tables[tName] = []
                for op in offering['observable_properties']:
                    if op['type'] == setting._COMPLEX_OBSERVATION:
                        continue
                    else:
                        # observedProperty filters are applied here excluding
                        # the observed properties columns from the query
                        if op_filter is not None and (
                                op['definition'] not in op_filter):
                            continue
                        columns.append(op['column'])
                        # columns_qi.append('%s_qi' % op['column'])
                        tables[tName].append(op['column'])
                        ConvertUnit=op['uom']
                        headers.append({
                            "type": "number",
                            "name": op['name'],
                            "definition": op['definition'],
                            "offering": offering['name'],
                            "uom": op['uom'],
                            "column": op['column']
                        })

            elif offering.is_array():
                raise Exception("Not implemented yet")
            else:
                tables[tName] = []
                for op in offering['observable_properties']:
                    # observedProperty filters are applied here excluding
                    # the observed properties columns from the query
                    if op_filter is not None and (
                            op['definition'] not in op_filter):
                        continue
                    columns.append(op['column'])
                    # columns_qi.append('%s_qi' % op['column'])
                    tables[tName].append(op['column'])
                    ConvertUnit=findLookUp(op['uom'])
                    headers.append({
                        "type": "number",
                        "name": op['name'],
                        "definition": op['definition'],
                        "offering": offering['name'],
                        "uom": op['uom'],
                        "column": op['column']
                    })

        unions = []
        unionSelect = []
        jsonKeys = [
            "array_agg(to_char(end_time, 'YYYY-MM-DD\"T\"HH24:MI:SSZ'))"
        ]
        unionColumns = []
        for idx in range(0, len(columns)):
            unionSelect.append(
                "SUM(c%s) as c%s" % (idx, idx)
            )
            unionColumns.append(
                "NULL::double precision as c%s" % (idx)
            )
            jsonKeys.append(
                "array_agg(c%s)" % (idx))

        unionSelect = ", ".join(unionSelect)

        temporal = []
        where = []
        params = []
        if request.get_filters() is not None:
            keys = list(request.get_filters())
            for key in keys:
                fltr = request.get_filters()[key]
                if key == 'temporal':
                    if fltr['fes'] == 'during':
                        temporal.append("""
                            begin_time >= %s::timestamp with time zone
                        AND
                            end_time <= %s::timestamp with time zone
                        """)
                        params.extend(fltr['period'])

                    elif fltr['fes'] == 'equals':
                        temporal.append("""
                            begin_time = end_time
                        AND
                            begin_time = %s::timestamp with time zone
                        """)
                        params.append(fltr['instant'])

                    where.append(
                        "(%s)" % (' OR '.join(temporal))
                    )

        for table in tables.keys():
            off_cols = tables[table]
            cols = unionColumns.copy()
            for col in off_cols:
                if 'in_unit' in request['json']:                
                    To_unit=request['json']['in_unit']
                    convert_unit="""(%s::text||'%s')::unit@@'%s' """%(col,ConvertUnit,To_unit)
                    cols[
                        columns.index(col)
                    ] = unionColumns[columns.index(col)].replace(
                        "NULL::double precision",
                        convert_unit
                    )
                else:
                    cols[
                        columns.index(col)
                    ] = unionColumns[columns.index(col)].replace(
                        "NULL::double precision",
                        col
                    )

            uSql = """
                SELECT
                    end_time, %s
                FROM
                    data.%s
            """ % (
                ", ".join(cols), table
            )
            if len(where) > 0:
                uSql += "WHERE %s" % (
                    'AND'.join(where)
                )
            unions.append("(%s)" % uSql)

        jsonSql = """
            SELECT %s
            FROM
        """ % (
            ", ".join(jsonKeys),
        )

        sql = """
            SET enable_seqscan=false;
            SET SESSION TIME ZONE '+00:00';
            %s
            (
                SELECT end_time, %s
                FROM (
                    %s
                ) a
                GROUP BY end_time
                ORDER BY end_time
            ) b
        """ % (
            jsonSql,
            unionSelect,
            " UNION ".join(unions)
        )

        istsos.debug(
            (
                yield from cur.mogrify(sql, tuple(params*len(unions)))
            ).decode("utf-8")
        )

        sqlExtensionUnit="""CREATE EXTENSION IF NOT EXISTS unit;"""
        yield from cur.execute(sqlExtensionUnit)

        yield from cur.execute(sql, tuple(params*len(unions)))
        rec = yield from cur.fetchone()
        request['observations'] = {}
        for idx in range(0, len(headers)):
            header = headers[idx]
            request['observations'][header['column']] = rec[idx]
        request['headers'] = headers
        istsos.debug("Data is fetched!")

    @asyncio.coroutine
    def __get_array(self, offerings, request):
        # print("To PRINT REQUEST AT OBSERVATION")
        # print(request[0]['offerings']['observable_properties'])
        # To_unit=request['json']['in_unit']
        # print("################################3")
        ConvertUnit=''
        dbmanager = yield from self.init_connection()
        cur = dbmanager.cur
        op_filter = request.get_filter('observedProperties')
        # print('Print Unit of observations line 250')
        # print(op_filter)
        tables = {}
        columns = []
        headers = [{
            "type": "time",
            "name": "Phenomenon Time",
            "column": "datetime"
        }]

        for offering in request['offerings']:
            tName = "_%s" % offering['name'].lower()
            if offering.is_complex():
                tables[tName] = []
                for op in offering['observable_properties']:
                    if op['type'] == setting._COMPLEX_OBSERVATION:
                        continue
                    else:
                        # observedProperty filters are applied here excluding
                        # the observed properties columns from the query
                        if op_filter is not None and (
                                op['definition'] not in op_filter):
                            continue
                        columns.append(op['column'])
                        # columns_qi.append('%s_qi' % op['column'])
                        tables[tName].append(op['column'])
                        ConvertUnit=yield from self.findLookUp(op['uom'])
                        headers.append({
                            "type": "number",
                            "name": op['name'],
                            "definition": op['definition'],
                            "offering": offering['name'],
                            "uom": op['uom']
                        })

            elif offering.is_array():
                raise Exception("Not implemented yet")
            else:
                tables[tName] = []
                for op in offering['observable_properties']:
                    # observedProperty filters are applied here excluding
                    # the observed properties columns from the query
                    if op_filter is not None and (
                            op['definition'] not in op_filter):
                        continue
                    columns.append(op['column'])
                    # columns_qi.append('%s_qi' % op['column'])
                    tables[tName].append(op['column'])
                    ConvertUnit=op['uom']
                    headers.append({
                        "type": "number",
                        "name": op['name'],
                        "definition": op['definition'],
                        "offering": offering['name'],
                        "uom": op['uom']
                    })
        # print('IT Is Unit IN OFFERING')
        # print(ConvertUnit)
        unions = []
        unionSelect = []
        jsonKeys = []
        unionColumns = []
        # for idx in range(0, len(columns)):
        #     unionSelect.append(
        #         "SUM(c%s)::text as c%s" % (idx, idx)
        #     )
        #     unionColumns.append(
        #         "NULL::double precision"
        #     )
        #     jsonKeys.append("COALESCE(c%s, 'null')" % (idx))
        # for idx in range(0, len(columns)):
        #     unionSelect.append(
        #         "SUM(c%s)::text as c%s" % (idx, idx)
        #     )
        #     unionColumns.append(
        #         "NULL::double precision as c%s" % (idx)
        #     )
        #     jsonKeys.append("COALESCE(c%s, 'null')" % (idx))

        for idx in range(0, len(columns)):
            unionSelect.append(
                "SUM(c%s)::text as c%s" % (idx, idx)
            )
            unionColumns.append(
                "NULL::double precision as c%s" % (idx)
            )
            jsonKeys.append("COALESCE(c%s, 'null')" % (idx))

        unionSelect = ", ".join(unionSelect)

        temporal = []
        where = []
        params = []
        if request.get_filters() is not None:
            keys = list(request.get_filters())
            for key in keys:
                fltr = request.get_filters()[key]
                if key == 'temporal':
                    if fltr['fes'] == 'during':
                        temporal.append("""
                            begin_time >= %s::timestamp with time zone
                        AND
                            end_time <= %s::timestamp with time zone
                        """)
                        params.extend(fltr['period'])

                    elif fltr['fes'] == 'equals':
                        temporal.append("""
                            begin_time = end_time
                        AND
                            begin_time = %s::timestamp with time zone
                        """)
                        params.append(fltr['instant'])

                    where.append(
                        "(%s)" % (' OR '.join(temporal))
                    )

        # print('Print Unit of Measurement')
        # print(headers)

        for table in tables.keys():
            off_cols = tables[table]
            cols = unionColumns.copy()
            # print('Print col in observations')
            # print(cols)
            # print(off_cols)
            for col in off_cols:
                # ConvertScript="""np.ting from(select SUBSTRING(CAST(tmp.num as varchar),'[0-9]+') as ting from(select %s *'m'::unit@ 'mm' as num)as tmp)as np"""% (", ",col)
                # ConvertScript="""
                # c0.ting as c0 
                # from
                # (
                # select SUBSTRING(CAST(tmp.num as varchar),'[0-9]+') as ting 
                # from
                # (
                # select """+col+ """*'m'::unit@ 'mm' as num from data._belin
                # )as tmp)"""
                ##################################
                # ConvertScript="""np.ting as c0 
                #     from
                #     (
                #     select SUBSTRING(CAST(tmp.num as varchar),'[0-9]+') as ting 
                #     from
                #     (
                #     select """+col+ """*'m'::unit@ 'mm' as num
                #     )as tmp) as np"""
                # # ConvertScript="np.ting from(select SUBSTRING(CAST(tmp.num as varchar),'[0-9]+') as ting from(select" +col+ "*'m'::unit@ 'mm' as num)as tmp)as np"
                # print('Printing ConvertScript')
                # print(ConvertScript)
                ###################################
                # cols[
                #     columns.index(col)
                # ] = unionColumns[columns.index(col)].replace(
                #     "NULL::double precision", ConvertScript
                # )
                ####################################3
                # convert_unit="""%s*'%s'::unit@@'%s' """%(col,ConvertUnit,To_unit)
                # print('Print convert query for postgresql-unit')
                # print(convert_unit)
                # cols[
                #     columns.index(col)
                # ] = unionColumns[columns.index(col)].replace(
                #     "NULL::double precision",
                #     convert_unit
                # )
                #############################
                # cols[
                #     columns.index(col)
                # ] = unionColumns[columns.index(col)].replace(
                #     "NULL::double precision",
                #     col+"*'m'::unit@@'mm' "
                # )
                if 'in_unit' in request['json']:                
                    To_unit=yield from self.findLookUp(request['json']['in_unit'])
                    convert_unit="""(%s::text||'%s')::unit@@'%s' """%(col,ConvertUnit,To_unit)
                    cols[
                        columns.index(col)
                    ] = unionColumns[columns.index(col)].replace(
                        "NULL::double precision",
                        convert_unit
                    )
                else:
                    cols[
                        columns.index(col)
                    ] = unionColumns[columns.index(col)].replace(
                        "NULL::double precision",
                        col
                    )

            # print('Print col in observations 1')
            # print(cols)
            # print(off_cols)
            # uSql = """
            #     SELECT
            #         end_time, %s
            #     FROM
            #         data.%s
            # """ % (
            #     ", ".join(cols), table
            # )

            uSql = """
                SELECT
                    end_time, %s
                FROM
                    data.%s
            """ % (
                ", ".join(cols), table
            )

            # print('Query Printing uSql')
            # print(uSql)
            # uSql = """
            #     SELECT
            #         end_time, %s '*' %s ::unit@ %s
            #     FROM
            #         data.%s
            # """ % (
            #     ", ".join(cols), ConvertUnit, To_unit, table
            # )
            if len(where) > 0:
                uSql += "WHERE %s" % (
                    'AND'.join(where)
                )
            unions.append("(%s)" % uSql)
            # print('Query Printing uSql')
            # print(uSql)

        jsonSql = """
            SELECT array_agg(
                ARRAY[
                    to_char(end_time, 'YYYY-MM-DD"T"HH24:MI:SSZ'),
                    %s
                ]
            )
            FROM
        """ % (
            ", ".join(jsonKeys),
        )
        # print('Query Printing jsonSql')
        # print(jsonSql)
        # print('Query Printing unionSelect')
        # print(unionSelect)
        # print('union')
        # print(unions)

        # sql = """
        #     SET enable_seqscan=false;
        #     SET SESSION TIME ZONE '+00:00';
        #     %s
        #     (
        #         SELECT end_time, %s
        #         FROM (
        #             %s
        #         ) a
        #         GROUP BY end_time
        #         ORDER BY end_time
        #     ) b
        # """ % (
        #     jsonSql,
        #     unionSelect,
        #     " UNION ".join(unions)
        # )

        sql = """
            SET enable_seqscan=false;
            SET SESSION TIME ZONE '+00:00';
            %s
            (
                SELECT end_time, %s
                FROM (
                    %s
                ) a
                GROUP BY end_time
                ORDER BY end_time
            ) b
        """ % (
            jsonSql,
            unionSelect,
            " UNION ".join(unions)
        )

        # sql = """
        #     SET enable_seqscan=false;
        #     SET SESSION TIME ZONE '+00:00';
        #     %s
        #     (
        #         SELECT end_time, %s*%s::unit@%s 
        #         FROM (
        #             %s
        #         ) a
        #         GROUP BY end_time
        #         ORDER BY end_time
        #     ) b
        # """ % (
        #     jsonSql,
        #     unionSelect,
        #     ConvertUnit,
        #     To_unit,
        #     " UNION ".join(unions)
        # )

        istsos.debug(
            (
                yield from cur.mogrify(sql, tuple(params*len(unions)))
            ).decode("utf-8")
        )        
        sqlExtensionUnit="""CREATE EXTENSION IF NOT EXISTS unit;"""
        yield from cur.execute(sqlExtensionUnit)
        yield from cur.execute(sql, tuple(params*len(unions)))
        # yield from cur.execute(sql, tuple(params*0))
        rec = yield from cur.fetchone()
        request['observations'] = rec[0]
        request['headers'] = headers
        # recs = yield from cur.fetchall()
        istsos.debug("Data is fetched!")

    @asyncio.coroutine
    def __get_kvp(self, offerings, request):

        dbmanager = yield from self.init_connection()
        cur = dbmanager.cur
        op_filter = request.get_filter('observedProperties')
        tables = {}
        columns = []
        ConvertUnit=''

        for offering in request['offerings']:
            tName = "_%s" % offering['name'].lower()
            if offering.is_complex():
                tables[tName] = []
                for op in offering['observable_properties']:
                    if op['type'] == setting._COMPLEX_OBSERVATION:
                        continue
                    else:
                        # observedProperty filters are applied here excluding
                        # the observed properties columns from the query
                        if op_filter is not None and (
                                op['definition'] not in op_filter):
                            continue
                        columns.append(op['column'])
                        # columns_qi.append('%s_qi' % op['column'])
                        tables[tName].append(op['column'])
                        ConvertUnit=op['uom']

            elif offering.is_array():
                raise Exception("Not implemented yet")
            else:
                tables[tName] = []
                for op in offering['observable_properties']:
                    # observedProperty filters are applied here excluding
                    # the observed properties columns from the query
                    if op_filter is not None and (
                            op['definition'] not in op_filter):
                        continue
                    columns.append(op['column'])
                    # columns_qi.append('%s_qi' % op['column'])
                    tables[tName].append(op['column'])
                    ConvertUnit=op['uom']

        unions = []
        unionSelect = []
        jsonKeys = []
        unionColumns = []
        for idx in range(0, len(columns)):
            unionSelect.append(
                "SUM(c%s)::text as c%s" % (idx, idx)
            )
            unionColumns.append(
                "NULL::double precision as c%s" % (idx)
            )
            jsonKeys.append("""
                "%s": ' || COALESCE(c%s, 'null') || '
            """ % (
                columns[idx],
                idx
            ))

        unionSelect = ", ".join(unionSelect)

        temporal = []
        where = []
        params = []
        if request.get_filters() is not None:
            keys = list(request.get_filters())
            for key in keys:
                fltr = request.get_filters()[key]
                if key == 'temporal':
                    if fltr['fes'] == 'during':
                        temporal.append("""
                            begin_time >= %s::timestamp with time zone
                        AND
                            end_time <= %s::timestamp with time zone
                        """)
                        params.extend(fltr['period'])

                    elif fltr['fes'] == 'equals':
                        temporal.append("""
                            begin_time = end_time
                        AND
                            begin_time = %s::timestamp with time zone
                        """)
                        params.append(fltr['instant'])

                    where.append(
                        "(%s)" % (' OR '.join(temporal))
                    )

        for table in tables.keys():
            off_cols = tables[table]
            cols = unionColumns.copy()
            for col in off_cols:
                if 'in_unit' in request['json']:                
                    To_unit=request['json']['in_unit']
                    convert_unit="""(%s::text||'%s')::unit@@'%s' """%(col,ConvertUnit,To_unit)
                    cols[
                        columns.index(col)
                    ] = unionColumns[columns.index(col)].replace(
                        "NULL::double precision",
                        convert_unit
                    )
                else:
                    cols[
                        columns.index(col)
                    ] = unionColumns[columns.index(col)].replace(
                        "NULL::double precision",
                        col
                    )

                # cols[
                #     columns.index(col)
                # ] = unionColumns[columns.index(col)].replace(
                #     "NULL::double precision",
                #     col
                # )
            uSql = """
                SELECT
                    end_time, %s
                FROM
                    data.%s
            """ % (
                ", ".join(cols), table
            )
            if len(where) > 0:
                uSql += "WHERE %s" % (
                    'AND'.join(where)
                )
            unions.append("(%s)" % uSql)

        jsonSql = """
            SELECT array_to_json(
                array_agg(('{
                    "e": "' || to_char(
                        end_time, 'YYYY-MM-DD"T"HH24:MI:SSZ')
                        || '",
                    %s
                }')::json)
            )
            FROM
        """ % (
            ", ".join(jsonKeys),
        )

        sql = """
            SET enable_seqscan=false;
            SET SESSION TIME ZONE '+00:00';
            %s
            (
                SELECT end_time, %s
                FROM (
                    %s
                ) a
                GROUP BY end_time
                ORDER BY end_time
            ) b
        """ % (
            jsonSql,
            unionSelect,
            " UNION ".join(unions)
        )
        # print('Length of Uninons')
        # print(len(unions))
        # print(unions)
        istsos.debug(
            (
                yield from cur.mogrify(sql, tuple(params*len(unions)))
            ).decode("utf-8")
        )
        # print('observation.py')
        # print(sql)
        # yield from cur.execute(sql, tuple(params*2)
        sqlExtensionUnit="""CREATE EXTENSION IF NOT EXISTS unit;"""
        yield from cur.execute(sqlExtensionUnit)
        yield from cur.execute(sql, tuple(params*len(unions)))
        rec = yield from cur.fetchone()
        # print(rec)
        # print('This is successful')
        request['observations'] = rec[0]
        # recs = yield from cur.fetchall()
        istsos.debug("Data is fetched!")

    @asyncio.coroutine
    def __get_data(self, offering, request):

        dbmanager = yield from self.init_connection()
        cur = dbmanager.cur

        table_name = "data._%s" % offering['name'].lower()

        columns = []
        ConvertUnit=''
        convert_unit=''
        # columns_qi = []
        op_filter = request.get_filter('observedProperties')

        observation = Observation.get_template({
            "offering": offering['name'],
            "procedure": offering['procedure']
        })

        if offering.is_complex():
            observation["type"] = setting._COMPLEX_OBSERVATION
            op = offering.get_complex_observable_property()
            observation["observedProperty"] = \
                ObservedPropertyComplex.get_template({
                    "def": op['definition'],
                    "name": op['name'],
                    "type": op['type'],
                    "uom": op['uom']
                })
            for op in offering['observable_properties']:
                if op['type'] == setting._COMPLEX_OBSERVATION:
                    continue
                else:
                    # observedProperty filters are applied here excluding
                    # the observed properties columns from the query
                    if op_filter is not None and (
                            op['definition'] not in op_filter):
                        continue

                    observation["observedProperty"]['fields'].append(
                        ObservedProperty.get_template({
                            "def": op['definition'],
                            "name": op['name'],
                            "type": op['type'],
                            "uom": op['uom']
                        })
                    )
                    columns.append(op['column'])
                    ConvertUnit=op['uom']
                    # columns_qi.append('%s_qi' % op['column'])

        elif offering.is_array():
            raise Exception("Not implemented yet")

        else:
            for op in offering['observable_properties']:
                observation["type"] = op['type']
                # observedProperty filters are applied here excluding
                # the observed properties columns from the query
                if op_filter is not None and (
                        op['definition'] not in op_filter):
                    continue

                observation["observedProperty"] = \
                    ObservedProperty.get_template({
                        "def": op['definition'],
                        "name": op['name'],
                        "type": op['type'],
                        "uom": op['uom']
                    })
                columns.append(op['column'])
                ConvertUnit=op['uom']
                # columns_qi.append('%s_qi' % op['column'])

        if 'in_unit' in request['json']:                
            To_unit=request['json']['in_unit']
            convert_unit="(%s::text||'%s')::unit@@'%s' as %s "%(", ".join(columns), ConvertUnit, To_unit, ", ".join(columns))
        else :
            convert_unit="%s"%(", ".join(columns))

        observation["phenomenonTime"] = {
            "timePeriod": {
                "begin": "",
                "end": ""
            }
        }

        if request.get_filter(
                "responseFormat") in setting._responseFormat['vega']:
            fastSql = """
                SELECT array_to_json(
                    array_agg(('{
                        "o": "%s",
                        "b": "' || to_char(
                            begin_time, 'YYYY-MM-DD"T"HH24:MI:SS+02:00')
                            || '",
                        "e": "' || to_char(
                            end_time, 'YYYY-MM-DD"T"HH24:MI:SS+02:00')
                            || '",
                        "r": "' || to_char(
                            result_time, 'YYYY-MM-DD"T"HH24:MI:SS+02:00')
                            || '",
                        "a": "' || %s || '"
                    }')::json)
                )
                FROM (
            """ % (
                offering['name'],
                columns[0],
            )

        else:
            fastSql = """
                SELECT
                    array_to_json(
                        array_agg(('{
                            "offering": "%s",
                            "procedure": "%s",
                            "type": %s,
                            "featureOfInterest": "ciao",
                            "phenomenonTime": {
                                "timePeriod": {
                                    "begin": "' || begin_time || '",
                                    "end": "' || end_time || '"
                                }
                            },
                            "resultTime": {
                                "timeInstant": {
                                    "instant": "' || result_time || '"
                                }
                            },
                            "result": "' || %s || '",
                            "observedProperty": %s
                        }')::json)
                )
                FROM (
                """ % (
                offering['name'],
                offering['procedure'],
                json.dumps(observation["type"]),
                columns[0],
                json.dumps(observation["observedProperty"])
            )
        
        # convert_unit=''
        # if 'in_unit' in request['json']:                
        #     To_unit=request['json']['in_unit']
        #     convert_unit="%s*'%s'::unit@@'%s' as %s "%(", ".join(columns), ConvertUnit, To_unit, ", ".join(columns))
        # else
        #     convert_unit="%s"%(", ".join(columns))
        # print('print convert unit'%convert_unit)
        # convert_unit="*'m'::unit@@'cm' as _9"
        sql = """
            SELECT
                begin_time,
                end_time,
                result_time,
                %s""" % (
                             convert_unit
                ) + """
            FROM %s
            """ % table_name
        print('GetData Called')
        print(sql)
        temporal = []
        where = []
        params = []
        if request.get_filters() is not None:
            keys = list(request.get_filters())
            for key in keys:
                fltr = request.get_filters()[key]
                if key == 'temporal':
                    if fltr['fes'] == 'during':
                        temporal.append("""
                            begin_time >= %s::timestamp with time zone
                        AND
                            end_time <= %s::timestamp with time zone
                        """)
                        params.extend(fltr['period'])

                    elif fltr['fes'] == 'equals':
                        temporal.append("""
                            begin_time = end_time
                        AND
                            begin_time = %s::timestamp with time zone
                        """)
                        params.append(fltr['instant'])

                    where.append(
                        "(%s)" % (' OR '.join(temporal))
                    )

        if len(where) > 0:
            sql += "WHERE %s" % (
                'AND'.join(where)
            )

        sql = """
            SET enable_seqscan=false;
            SET SESSION TIME ZONE '+02:00';
            %s
            %s
             ORDER BY begin_time ) t
        """ % (
            fastSql,
            sql
        )

        istsos.debug(
            (
                yield from cur.mogrify(sql, tuple(params))
            ).decode("utf-8")
        )

        sqlExtensionUnit="""CREATE EXTENSION IF NOT EXISTS unit;"""
        yield from cur.execute(sqlExtensionUnit)

        yield from cur.execute(sql, tuple(params))
        rec = yield from cur.fetchone()
        request['observations'] += rec[0]
        # recs = yield from cur.fetchall()
        istsos.debug("Data is fetched!")
