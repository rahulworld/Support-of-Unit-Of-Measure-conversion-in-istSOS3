# istSOS-Support of Unit Of Measure conversion in istSOS3
> IstSOS is an OGC SOS 2.0 server implementation written in Python.

>Mentors : [@massimiliano-cannata](https://github.com/massimiliano-cannata), [@mantonovic](https://github.com/mantonovic)

## Summary

The primary goal of my project was to create `OAT(Data analysis and statistics)` extension in RESTFull Web api and `OAT extension` having data analysis and statistical tools for `istSOS` which is be used to automate the creation of statisticate documents using OAT library and harvesting the data from an istSOS server.

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
1. Understanding istSOS structure and OAT package
2. Working with extjs tools in a concurrent environment.
3. Developing consistent suits.

# Scope for future improvements
1. fuctionality add sensor through (CSV, istSOS, Raw)data in `Add sensor name` GUI in `OAT extenstion`.
![Add sensor name](images/addSensorName.png)
2. fuctionality add in `Mangae sensor`.
3. functionalty add in `Compare sensor`.

# Commits

### Support of Unit Of Measure conversion in istSOS3 Pool

[pull request]()

[forked github Repo.](https://github.com/rahulworld/istsos3)

[Data analysis and statistics tools suit commits](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/commits/master)

### Support of Unit Of Measure conversion in istSOS3

[Updated OAT methods](https://github.com/rahulworld/Data-analysis/commit/8ab10fbb74331fe5ad85237e14996a2b207be79d)

[Added multiple y-axis in Dygraph](https://github.com/rahulworld/Data-analysis/commit/d6b25967fd46c4c7c4f371376089f8d9f212d0a0)

[Added download result](https://github.com/rahulworld/Data-analysis/commit/dfa2c7e131c3b1a899ddd1a25291fe2e9c5a339d)

[Added tabulation](https://github.com/rahulworld/Data-analysis/commit/bd434114a6c6bf66031de56d067f00e09fa41ff1)

[Added usage of period](https://github.com/rahulworld/Data-analysis/commit/c61b096af2f8dc12257caa0d20279584e1dffbf0)

[Added usage of time](https://github.com/rahulworld/Data-analysis/commit/d3ba63b7ab9fd7011b66903c85b4dcf2af723b41)

[Added hargreaves oat method](https://github.com/rahulworld/Data-analysis/commit/2972711b9db4ed50d840cb7862bcd4743b804683)

[Added data_values oat method](https://github.com/rahulworld/Data-analysis/commit/a681def7a961d243e4bcef6d8634c81d21a47eb5)

[Added quality oat method](https://github.com/rahulworld/Data-analysis/commit/655069f461243cfd96774bc1cd85ad8192867d02)

[Added fill oat method](https://github.com/rahulworld/Data-analysis/commit/15bf91e0a7a7338813fed5f014125b6b4ac583da)

[Added statistics oat method](https://github.com/rahulworld/Data-analysis/commit/8e380f6f0b1acf38ac85beeea8ed97cf696fe610)

[Added hydro_indicies oat method](https://github.com/rahulworld/Data-analysis/commit/8f8795257dbc399d93ad1eb20f7d3c60c41f9319)

[Added intgrate oat method](https://github.com/rahulworld/Data-analysis/commit/ccf52ee83a4cc445c5774c3599f7e36cc38a170e)

[Added hydro_events oat method](https://github.com/rahulworld/Data-analysis/commit/2b7b36ea0efe0d22b02c95b19e33826982bf545a)

[Added hydro_separation oat method](https://github.com/rahulworld/Data-analysis/commit/4a347d800660ccd612f8493ce2f38b14491ae286)

[Added exeedance oat method](https://github.com/rahulworld/Data-analysis/commit/dde68648c26928d27d728a793ffd8cf946adfddd)

[Added resample oat method](https://github.com/rahulworld/Data-analysis/commit/1083c47c0ded0e7aaf285ea14041ae194b72aa27)

[Added some OAT methods GUI](https://github.com/rahulworld/Data-analysis/commit/7096bc88ceb2ab493ce915f6420b8855cfcfba43)

[Added page Add Sensor GUI](https://github.com/rahulworld/Data-analysis/commit/48173aa5ed562987bc5d0dee429bb060845181a0)

[Added page Process time series GUI](https://github.com/rahulworld/Data-analysis/commit/b9269e911eab22a36dbfffc653abb7efcbebbba8)

##Other Links
* [documentation](https://github.com/rahulworld/Support-of-Unit-Of-Measure-conversion-in-istSOS3/wiki/Wiki)
* [Wiki](https://wiki.osgeo.org/wiki/GSoC_18:_istSOS-Support_of_Unit_Of_Measure_conversion_in_istSOS3)
* [Blog](https://rahulworld.github.io/GSoC18.html)
* [Github](https://github.com/rahulworld)