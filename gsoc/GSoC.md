# istSOS-Support of Unit Of Measure conversion in istSOS3
> IstSOS is an OGC SOS 2.0 server implementation written in Python.

>Mentors : [@massimiliano-cannata](https://github.com/massimiliano-cannata), [@mantonovic](https://github.com/mantonovic)

## Summary

The aim of my project primarily is to add `plugins` conversion of the unit of measure in istSOS3. The user can convert unit in another specified unit. For Unit of measure conversion in `istSOS3` we added `postgresql-unit` and `pint` libraries which has a powerful feature of unit conversion along with many specified functions like `unit conversion` function instantly and all types operations supports to istsos3 data like `add`, `subtraction`, `multiplication` and `division` with `magnitude` and `units`.


[Download Plugins ans how to install](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/wiki/Wiki)

<!-- ![OAT Extension](images/quality1.png) -->

---
### istSOS3

istSOS3 is an OGC SOS server implementation written in Python. istSOS3 allows Multiple system type observation and sensor management.

[Developers docs](http://istsos.org/en/v3.0.0-Beta/index.html)

---
## Tools Used

1. [postgresql-unit](https://github.com/ChristophBerg/postgresql-unit)
2. [pint](https://github.com/hgrecco/pint)

### postgresql-unit

postgresql-unit implements a `PostgreSQL datatype` for SI units, plus byte. The eight base units can be combined to arbitrarily complex derived units using operators defined in the PostgreSQL type system. SI and IEC binary prefixes are used for input and output, and quantities can be converted to arbitrary scale. Unit and prefix definitions are retrieved from database tables, and new definitions can be added at run time. The extension comes with over 2500 units and over 100 prefixes found in the definitions.units file in GNU Units 2.16.

### pint

Pint is a `Python package` to define, operate and manipulate physical quantities: the product of a numerical value and a unit of measurement. It allows arithmetic operations between them and conversions from and to different units. It runs in Python 2.7 and 3.3+ with no other dependency. It supports a lot of numpy mathematical operations without monkey patching or wrapping numpy.

---


# Challenges
1. Understanding istSOS3 structure, postgresql-unit and pint.
2. Working with unit conversion tools in a concurrent environment.
3. Developing consistent plugins.

# Scope for future improvements
1. Need Modularity for every unit operations and improvement in exceptional units conversion.

# Commits

### Support of Unit Of Measure conversion in istSOS3 Pool

[pull request]()

[forked github Repo.](https://github.com/rahulworld/istsos3)

[Support of Unit Of Measure conversion in istSOS3](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commits/master)

### Support of Unit Of Measure conversion in istSOS3

[Fixing bug in pint temprature addition](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/d5461f4d2da3c6b897a6fe4bfc37faf6504094de)

[added download in pint](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/cf30cbc83fbf0faeff259349fec47388e1decab3)

[Added operation in pint](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/997f007a5dff5d57b51b6f463b4d9c61a7112a43)

[Added downlaod file with postgresql-unit](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/3be4ff154f8c53fbf0f90383c6317cedec6648cc)

[Added lookup table in postgresql plugin](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/7c5157ef8a38becc26553ed1a8acda4eb3f89ef6)

[Added operations in postgresql plugin](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/9c4d1840c8dff6e17307990e25bb6412db3187fe)

[Fixing ambigous issue in pint](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/0c449859be1844ce847b96d0d28637dea8b2b68a)

[Added lookup table](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/f119d901902f0212300f842271e43d6f6901e2db)

[Fixing error postgresql-unit conversion](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/d79a3680c88dd7f7bd75b76912b4b9ef3ad47420)

[Added unit coversion in all formats array, array2, vega and defualt data for post plugins](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/b3170f1d1a59a1a5ca41545ff2318a449d07333c)

[Added units in plugins](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/9c4d1840c8dff6e17307990e25bb6412db3187fe)

[Added units in lookup](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/11f032bfabfb49facefbd67f447912a8a116cf83)

[Added units in lookup in pint plugin](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/4cbea439693ba60156a0a5d4139163d72d4a5cc0)

[Added lookup](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commit/cf30cbc83fbf0faeff259349fec47388e1decab3)

##Other Links
* [documentation](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/wiki/Wiki)
* [Wiki](https://wiki.osgeo.org/wiki/GSoC_18:_istSOS-Support_of_Unit_Of_Measure_conversion_in_istSOS3)
* [Blog](https://rahulworld.github.io/GSoC18.html)
* [Github](https://github.com/rahulworld)