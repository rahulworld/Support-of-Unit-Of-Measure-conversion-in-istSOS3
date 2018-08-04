# -*- coding: utf-8 -*-
# istSOS. See https://istsos.org/
# License: https://github.com/istSOS/istsos3/master/LICENSE.md
# Version: v3.0.0
lookups = {
    "°C":["°C", "C", "celcius", "degree Celsius", "degree-celsius", "degree-celsius", "degree", "degree centigrade", "degcelsius", "degC"],
    "°F":["°F", "F", "fahrenheit", "degfahrenheit", "degF", "degfahrenheit", "degree-fahrenheit", "degree fahrenheit"],
    "°K":["°K", "K", "kelvin", "degK", "tempK"],
    "°R":["°R", "R", "Rankine", "°Ra"],

    "mm":["mm", "millimeter", "milli-meter"],
    "cm":["cm", "centi-meter", "centi", "centimeter"],
    "m":["m", "meter"],
    "in":["in", "inch"],
    "ft":["ft", "feet", "foot"],
    "fathom":["fathom"],
    "mi":["mi", "miles", "mile"],

    "ns":["ns"],
    "ms":["ms","millisecond"],
    "s":["s"],
    "min":["min"],
    "h":["h","hour"],
    "d":["day"],
    "week":["week"],
    "month":["month"],
    "year":["year"],

    "Hz":["Hz"],
    "mHz":["mHz"],
    "kHz":["kHz"],
    "MHz":["MHz"],
    "GHz":["GHz"],
    "THz":["THz"],
    "rpm":["rpm"],
    "deg/s":["deg/s"],
    "radian/s":["radian/s", "rad/s"],

    "mm/s":["mm/s", "millimeter/s", "milli-meter/s"],
    "cm/s":["cm/s", "centi-meter/s", "centi/s", "centimeter/s"],
    "m/s":["m/s", "meter/s"],
    "m/h":["m/h", "meter/h"],
    "in/s":["in/s", "inch/s"],
    "ft/s":["ft/s", "feet/s", "foot/s"],
    "mi/h":["mi/h", "miles/h", "mile/h"],
    "knot":["knot"],

    "mm^2":["mm^2", "mm2", "millimeter-2", "millimeter2", "mm square" ],
    "cm^2":["cm^2", "cm2", "centimeter-2", "centimeter2", "cm square"],
    "m^2":["m^2", "m2","meter2", "meter square"],
    "ha":["ha", "hactare"],
    "km^2":["km^2", "km2", "kilometer2", "kilometer square"],
    "in^2":["in^2", "in2", "inch2", "inch^2", "inch-square", "inch square"],
    "ft^2":["ft^2" , "ft2", "feet2", "feetsquare"],
    "acre":["ac", "acre"],
    "mi^2":["mi^2", "miles square", "miles2", "miles^2"],

    "mm^3":["mm^3", "mm3", "millimeter-3", "millimeter3", "mm cube" ],
    "cm^3":["cm^3", "cm3", "centimeter-3", "centimeter3", "cm cube"],
    "m^3":["m^3", "m3","meter3", "meter cube"],
    "km^3":["km^3", "km3", "kilometer3", "kilometer cube"],
    "in^3":["in^3", "in3", "inch3", "inch^3", "inch-cube", "inch cube"],
    "ft^3":["ft^3" , "ft3", "feet3", "feetcube"],
    "mi^3":["mi^3", "miles cube", "miles3", "miles^3"],
    "ml":["ml", "milliliter"],
    "l":["l", "liter"],
    "kl":["kl", "kiloliter"],
    "tsp":["tsp", "teaspoon"],
    "in^3":["in^3"],
    "cup":["cup"],
    "qt":["qt"],
    "gal":["gal","gallon"],
    "yd^3":["yd^3","yd3"],

    "mcg":["mcg"],
    "mg":["mg"],
    "g":["g"],
    "kg":["kg"],
    "oz":["oz"],
    "lb":["lb"],
    "mt":["mt"],
    "t":["t"],

    "mm^3/s":["mm^3/s", "mm3/s", "millimeter-3/s", "millimeter3/s", "mm cube/s" ],
    "cm^3/s":["cm^3/s", "cm3/s", "centimeter-3/s", "centimeter3/s", "cm cube/s"],
    "m^3/s":["m^3/s", "m3/s","meter3/s", "meter cube/s"],
    "ml/s":["ml/s", "milliliter/s"],
    "kl/s":["kl/s", "kl/s", "kiloliter/s", "kiloliter/s"],
    "kl/min":["kl/min", "kiloliter/min", "kiloliter/min"],
    "kl/h":["kl/h", "kl/h", "kiloliter/h", "kiloliter/h"],
    "km^3/h":["km^3/h", "km3/h", "kilometer3/h", "kilometer cube/h"],
    "cl/s":["cl/s", "cl/s", "cl/s", "cl/s"],
    "dl/s":["dl/s"],
    "l/s":["l/s", "liter/s"],
    "l/min":["l/min", "liter/min"],
    "l/h":["l/h", "liter/h"],
    "ft^3/s":["ft^3/s" , "ft3/s", "feet3/s", "feetcube/s"],
    "mi^3/s":["mi^3/s", "miles cube/s", "miles3/s", "miles^3/s"],
    "tsp/s":["tsp/s", "teaspoon/s"],
    "in^3/s":["in^3/s"],
    "cup/s":["cup/s"],
    "qt/s":["qt/s"],
    "gal/s":["gal/s","gallon/s"],
    "gal/min":["gal/min","gallon/min"],
    "yd^3/s":["yd^3/s","yd3/s"],

    "s/m":["s/m"],
    "min/m":["min/m"],
    "s/ft":["s/ft"],
    "min/km":["min/km"],

    "Pa":["Pa"],
    "hPa":["hPa"],
    "kPa":["kPa"],
    "MPa":["MPa"],
    "bar":["bar"],
    "torr":["torr"],
    "psi":["psi"],
    "ksi":["ksi"],

    "byte":["byte"],
    "B":["B"],
    "kB":["kB"],
    "KB":["KB"],
    "MB":["MB"],
    "GB":["GB"],
    "TB":["TB"],

    "lx":["lx"],

    "ppm":["ppm"],
    "ppb":["ppb"],
    "ppt":["ppt"],

    "V":["V"],
    "mV":["mV"],
    "kV":["kV"],

    "A":["A"],
    "mA":["mA"],
    "kA":["kA"],

    "W":["W"],
    "mW":["mW"],
    "kW":["kW"],
    "MW":["MW"],
    "GW":["GW"],

    "VA":["VA"],
    "mVA":["mVA"],
    "kVA":["kVA"],
    "MVA":["MVA"],
    "GVA":["GVA"], 

    "Wh":["Wh"],
    "mWh":["mWh"],
    "MWh":["MWh"],
    "GWh":["GWh"],
    "J":["J"],
    "kJ":["kJ"],

    "deg":["deg"],
    "radian":["radian", "rad"],
    "arcmin":["arcmin"],
    "arcsec":["arcsec"],

    "C":["C"],
    "mC":["mC"],
    "μC":["μC"],
    "nC":["nC"],
    "pC":["pC"],

    "N":["N"],
    "kN":["kN"],
    "lbf":["lbf"],

    "gravity":["gravity", "gravity"],
    "m/s2":["m/s2"],

     }

import asyncio
import istsos
import json
import csv
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
        return(unit)

    @asyncio.coroutine
    def __download_file(self, request, data, headers=None):
        if request.get_filter("download_file") is not None:
            if 'file_name' in request.get_filter("download_file"):
                file_name=request.get_filter("download_file")['file_name']
            else:
                file_name=request.get_filter("offerings")

            if 'location' in request.get_filter("download_file"):
                download_location=request.get_filter("download_file")['location']
            else:
                download_location='istsos/plugins/unit_con_post/download_file/'

            file_detail = """%s%s.csv""" % (download_location, file_name)
            f = csv.writer(open(file_detail, "w"))
            if headers is not None:
                f.writerow(headers)
            for x in data:
                f.writerow(x)
            debug_detail = """%s.csv download location is %s""" % (file_name, download_location)
            istsos.debug(debug_detail)

    @asyncio.coroutine
    def __download_json(self, request, data):
        if request.get_filter("download_file") is not None:
            if 'file_name' in request.get_filter("download_file"):
                file_name=request.get_filter("download_file")['file_name']
            else:
                file_name=request.get_filter("offerings")

            if 'location' in request.get_filter("download_file"):
                download_location=request.get_filter("download_file")['location']
            else:
                download_location='istsos/plugins/unit_con_post/download_file/'

            file_detail = """%s%s.json""" % (download_location, file_name)
            with open(file_detail, 'w') as outfile:
                json.dump(data, outfile)
            # f = csv.writer(open(file_detail, "w"))
            # # f.writerow(rec[0])
            # for x in rec[0]:
            #     f.writerow([x])
            debug_detail = """%s.json download location is %s""" % (file_name, download_location)
            istsos.debug(debug_detail)


    @asyncio.coroutine
    def __get_array_2(self, offerings, request):

        dbmanager = yield from self.init_connection()
        cur = dbmanager.cur
        op_filter = request.get_filter('observedProperties')
        tables = {}
        columns = []
        ConvertUnit=''
        conversion_uom=''
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
                            "initial_uom": op['uom'],
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
                    ConvertUnit=yield from self.findLookUp(op['uom'])
                    headers.append({
                        "type": "number",
                        "name": op['name'],
                        "definition": op['definition'],
                        "offering": offering['name'],
                        "initial_uom": op['uom'],
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
                convert_unit=''
                if request.get_filter("in_unit") is not None:
                    To_unit=yield from self.findLookUp(request.get_filter("in_unit"))
                    if request.get_filter("operation") is not None:
                        if 'unit' in request.get_filter("operation"):
                            unit=yield from self.findLookUp(request.get_filter("operation")['unit'])
                            if 'qty' in request.get_filter("operation"):
                                qty=request.get_filter("operation")['qty']
                                if 'type' in request.get_filter("operation"):
                                    if request.get_filter("operation")['type']=='add':
                                        add=qty
                                        if qty=='':
                                            add=0
                                        convert_unit="""(%s::text||'%s')::unit + ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, add, unit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='sub':
                                        sub=qty
                                        if qty=='':
                                            sub=0
                                        convert_unit="""(%s::text||'%s')::unit - ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, sub, unit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='mul':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit * '%s %s' ::unit@@'%s*%s' """%(col, ConvertUnit, mul, unit, To_unit, unit)
                                        conversion_uom=""" %s*%s """%(To_unit,unit)
                                    elif request.get_filter("operation")['type']=='div':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit / '%s %s' ::unit@@'%s/%s' """%(col, ConvertUnit, mul, unit, To_unit, unit)
                                        conversion_uom=""" %s/%s """%(To_unit,unit)
                        else:
                            if 'qty' in request.get_filter("operation"):
                                qty=request.get_filter("operation")['qty']
                                if 'type' in request.get_filter("operation"):
                                    if request.get_filter("operation")['type']=='add':
                                        add=qty
                                        if qty=='':
                                            add=0
                                        convert_unit="""(%s::text||'%s')::unit + ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, add, ConvertUnit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='sub':
                                        sub=qty
                                        if qty=='':
                                            sub=0
                                        convert_unit="""(%s::text||'%s')::unit - ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, sub, ConvertUnit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='mul':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit * '%s %s' ::unit@@'%s*%s' """%(col, ConvertUnit, mul, ConvertUnit, To_unit, To_unit)
                                        conversion_uom=""" %s*%s """%(To_unit,To_unit)
                                    elif request.get_filter("operation")['type']=='div':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit / '%s %s' ::unit@@'%s/%s' """%(col, ConvertUnit, mul, ConvertUnit, To_unit, To_unit)
                                        conversion_uom=""" %s/%s """%(To_unit,To_unit)
                    else:
                        convert_unit="""(%s::text||'%s')::unit@@'%s' """%(col, ConvertUnit, To_unit)
                        conversion_uom=To_unit
                    cols[
                        columns.index(col)
                    ] = unionColumns[columns.index(col)].replace(
                        "NULL::double precision",
                        convert_unit
                    )
                elif request.get_filter("operation") is not None:
                    if 'unit' in request.get_filter("operation"):
                        unit=yield from self.findLookUp(request.get_filter("operation")['unit'])
                        if 'qty' in request.get_filter("operation"):
                            qty=request.get_filter("operation")['qty']
                            if 'type' in request.get_filter("operation"):
                                if request.get_filter("operation")['type']=='add':
                                    add=qty
                                    if qty=='':
                                        add=0
                                    convert_unit="""(%s::text||'%s')::unit + ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, add, unit, ConvertUnit)
                                    conversion_uom=ConvertUnit
                                elif request.get_filter("operation")['type']=='sub':
                                    sub=qty
                                    if qty=='':
                                        sub=0
                                    convert_unit="""(%s::text||'%s')::unit - ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, sub, unit, ConvertUnit)
                                    conversion_uom=ConvertUnit
                                elif request.get_filter("operation")['type']=='mul':
                                    mul=qty
                                    if qty=='':
                                        mul=1
                                    convert_unit="""(%s::text||'%s')::unit * '%s %s' ::unit@@'%s*%s' """%(col, ConvertUnit, mul, unit, ConvertUnit, unit)
                                    conversion_uom=""" %s*%s """%(ConvertUnit,unit)
                                elif request.get_filter("operation")['type']=='div':
                                    mul=qty
                                    if qty=='':
                                        mul=1
                                    convert_unit="""(%s::text||'%s')::unit / '%s %s' ::unit@@'%s/%s' """%(col, ConvertUnit, mul, unit, ConvertUnit, unit)
                                    conversion_uom=""" %s/%s """%(ConvertUnit,unit)
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

        headers.append({
            "type": "number",
            "name": op['name'],
            "definition": op['definition'],
            "offering": offering['name'],
            "final_uom": conversion_uom,
            "column": op['column']
        })

        yield from self.__download_file(request, rec, headers)

        request['headers'] = headers
        istsos.debug("Data is fetched!")

    @asyncio.coroutine
    def __get_array(self, offerings, request):
        # print("To PRINT REQUEST AT OBSERVATION")
        # print(request[0]['offerings']['observable_properties'])
        # To_unit=request['json']['in_unit']
        # print("################################3")
        conversion_uom=''
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
                convert_unit=''
                if request.get_filter("in_unit") is not None:
                    To_unit=yield from self.findLookUp(request.get_filter("in_unit"))
                    if request.get_filter("operation") is not None:
                        if 'unit' in request.get_filter("operation"):
                            unit=yield from self.findLookUp(request.get_filter("operation")['unit'])
                            if 'qty' in request.get_filter("operation"):
                                qty=request.get_filter("operation")['qty']
                                if 'type' in request.get_filter("operation"):
                                    if request.get_filter("operation")['type']=='add':
                                        add=qty
                                        if qty=='':
                                            add=0
                                        convert_unit="""(%s::text||'%s')::unit + ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, add, unit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='sub':
                                        sub=qty
                                        if qty=='':
                                            sub=0
                                        convert_unit="""(%s::text||'%s')::unit - ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, sub, unit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='mul':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit * '%s %s' ::unit@@'%s*%s' """%(col, ConvertUnit, mul, unit, To_unit, unit)
                                        conversion_uom=""" %s*%s """%(To_unit,unit)
                                    elif request.get_filter("operation")['type']=='div':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit / '%s %s' ::unit@@'%s/%s' """%(col, ConvertUnit, mul, unit, To_unit, unit)
                                        conversion_uom=""" %s/%s """%(To_unit,unit)
                        else:
                            if 'qty' in request.get_filter("operation"):
                                qty=request.get_filter("operation")['qty']
                                if 'type' in request.get_filter("operation"):
                                    if request.get_filter("operation")['type']=='add':
                                        add=qty
                                        if qty=='':
                                            add=0
                                        convert_unit="""(%s::text||'%s')::unit + ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, add, ConvertUnit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='sub':
                                        sub=qty
                                        if qty=='':
                                            sub=0
                                        convert_unit="""(%s::text||'%s')::unit - ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, sub, ConvertUnit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='mul':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit * '%s %s' ::unit@@'%s*%s' """%(col, ConvertUnit, mul, ConvertUnit, To_unit, To_unit)
                                        conversion_uom=""" %s*%s """%(To_unit,To_unit)
                                    elif request.get_filter("operation")['type']=='div':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit / '%s %s' ::unit@@'%s/%s' """%(col, ConvertUnit, mul, ConvertUnit, To_unit, To_unit)
                                        conversion_uom=""" %s/%s """%(To_unit,To_unit)
                    else:
                        convert_unit="""(%s::text||'%s')::unit@@'%s' """%(col, ConvertUnit, To_unit)
                        conversion_uom=To_unit
                    cols[
                        columns.index(col)
                    ] = unionColumns[columns.index(col)].replace(
                        "NULL::double precision",
                        convert_unit
                    )
                elif request.get_filter("operation") is not None:
                    if 'unit' in request.get_filter("operation"):
                        unit=yield from self.findLookUp(request.get_filter("operation")['unit'])
                        if 'qty' in request.get_filter("operation"):
                            qty=request.get_filter("operation")['qty']
                            if 'type' in request.get_filter("operation"):
                                if request.get_filter("operation")['type']=='add':
                                    add=qty
                                    if qty=='':
                                        add=0
                                    convert_unit="""(%s::text||'%s')::unit + ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, add, unit, ConvertUnit)
                                    conversion_uom=ConvertUnit
                                elif request.get_filter("operation")['type']=='sub':
                                    sub=qty
                                    if qty=='':
                                        sub=0
                                    convert_unit="""(%s::text||'%s')::unit - ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, sub, unit, ConvertUnit)
                                    conversion_uom=ConvertUnit
                                elif request.get_filter("operation")['type']=='mul':
                                    mul=qty
                                    if qty=='':
                                        mul=1
                                    convert_unit="""(%s::text||'%s')::unit * '%s %s' ::unit@@'%s*%s' """%(col, ConvertUnit, mul, unit, ConvertUnit, unit)
                                    conversion_uom=""" %s*%s """%(ConvertUnit,unit)
                                elif request.get_filter("operation")['type']=='div':
                                    mul=qty
                                    if qty=='':
                                        mul=1
                                    convert_unit="""(%s::text||'%s')::unit / '%s %s' ::unit@@'%s/%s' """%(col, ConvertUnit, mul, unit, ConvertUnit, unit)
                                    conversion_uom=""" %s/%s """%(ConvertUnit,unit)
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

        yield from self.__download_file(request, rec[0], headers)

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
        conversion_uom=''
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
                convert_unit=''
                if request.get_filter("in_unit") is not None:
                    To_unit=yield from self.findLookUp(request.get_filter("in_unit"))
                    if request.get_filter("operation") is not None:
                        if 'unit' in request.get_filter("operation"):
                            unit=yield from self.findLookUp(request.get_filter("operation")['unit'])
                            if 'qty' in request.get_filter("operation"):
                                qty=request.get_filter("operation")['qty']
                                if 'type' in request.get_filter("operation"):
                                    if request.get_filter("operation")['type']=='add':
                                        add=qty
                                        if qty=='':
                                            add=0
                                        convert_unit="""(%s::text||'%s')::unit + ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, add, unit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='sub':
                                        sub=qty
                                        if qty=='':
                                            sub=0
                                        convert_unit="""(%s::text||'%s')::unit - ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, sub, unit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='mul':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit * '%s %s' ::unit@@'%s*%s' """%(col, ConvertUnit, mul, unit, To_unit, unit)
                                        conversion_uom=""" %s*%s """%(To_unit,unit)
                                    elif request.get_filter("operation")['type']=='div':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit / '%s %s' ::unit@@'%s/%s' """%(col, ConvertUnit, mul, unit, To_unit, unit)
                                        conversion_uom=""" %s/%s """%(To_unit,unit)
                        else:
                            if 'qty' in request.get_filter("operation"):
                                qty=request.get_filter("operation")['qty']
                                if 'type' in request.get_filter("operation"):
                                    if request.get_filter("operation")['type']=='add':
                                        add=qty
                                        if qty=='':
                                            add=0
                                        convert_unit="""(%s::text||'%s')::unit + ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, add, ConvertUnit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='sub':
                                        sub=qty
                                        if qty=='':
                                            sub=0
                                        convert_unit="""(%s::text||'%s')::unit - ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, sub, ConvertUnit, To_unit)
                                        conversion_uom=To_unit
                                    elif request.get_filter("operation")['type']=='mul':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit * '%s %s' ::unit@@'%s*%s' """%(col, ConvertUnit, mul, ConvertUnit, To_unit, To_unit)
                                        conversion_uom=""" %s*%s """%(To_unit,To_unit)
                                    elif request.get_filter("operation")['type']=='div':
                                        mul=qty
                                        if qty=='':
                                            mul=1
                                        convert_unit="""(%s::text||'%s')::unit / '%s %s' ::unit@@'%s/%s' """%(col, ConvertUnit, mul, ConvertUnit, To_unit, To_unit)
                                        conversion_uom=""" %s/%s """%(To_unit,To_unit)
                    else:
                        convert_unit="""(%s::text||'%s')::unit@@'%s' """%(col, ConvertUnit, To_unit)
                        conversion_uom=To_unit
                    cols[
                        columns.index(col)
                    ] = unionColumns[columns.index(col)].replace(
                        "NULL::double precision",
                        convert_unit
                    )
                elif request.get_filter("operation") is not None:
                    if 'unit' in request.get_filter("operation"):
                        unit=yield from self.findLookUp(request.get_filter("operation")['unit'])
                        if 'qty' in request.get_filter("operation"):
                            qty=request.get_filter("operation")['qty']
                            if 'type' in request.get_filter("operation"):
                                if request.get_filter("operation")['type']=='add':
                                    add=qty
                                    if qty=='':
                                        add=0
                                    convert_unit="""(%s::text||'%s')::unit + ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, add, unit, ConvertUnit)
                                    conversion_uom=ConvertUnit
                                elif request.get_filter("operation")['type']=='sub':
                                    sub=qty
                                    if qty=='':
                                        sub=0
                                    convert_unit="""(%s::text||'%s')::unit - ('%s'::text||'%s')::unit@@'%s' """%(col, ConvertUnit, sub, unit, ConvertUnit)
                                    conversion_uom=ConvertUnit
                                elif request.get_filter("operation")['type']=='mul':
                                    mul=qty
                                    if qty=='':
                                        mul=1
                                    convert_unit="""(%s::text||'%s')::unit * '%s %s' ::unit@@'%s*%s' """%(col, ConvertUnit, mul, unit, ConvertUnit, unit)
                                    conversion_uom=""" %s*%s """%(ConvertUnit,unit)
                                elif request.get_filter("operation")['type']=='div':
                                    mul=qty
                                    if qty=='':
                                        mul=1
                                    convert_unit="""(%s::text||'%s')::unit / '%s %s' ::unit@@'%s/%s' """%(col, ConvertUnit, mul, unit, ConvertUnit, unit)
                                    conversion_uom=""" %s/%s """%(ConvertUnit,unit)
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

        yield from self.__download_json(request, rec[0])

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

        if request.get_filter("in_unit") is not None:                
            To_unit=request.get_filter("in_unit")
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

        yield from self.__download_json(request, rec[0])

        # recs = yield from cur.fetchall()
        istsos.debug("Data is fetched!")
