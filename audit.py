"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values


The type() function returns a type object describing the argument given to the 
function. You can also use examples of objects to create type objects, e.g.
type(1.1) for a float: see the test function below for examples.

Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should note be included
when processing data types. Be sure to include functionality in your code to
skip over or detect these rows.
"""

import codecs
import csv
import json

CITIES = "cities.csv"

FIELDS = [
    "name",
    "timeZone_label",
    "utcOffset",
    "homepage",
    "governmentType_label",
    "isPartOf_label",
    "areaCode",
    "populationTotal",
    "elevation",
    "maximumElevation",
    "minimumElevation",
    "populationDensity",
    "wgs84_pos#lat",
    "wgs84_pos#long",
    "areaLand",
    "areaMetro",
    "areaUrban",
]


def checknumber(number):
    """Takes as argument the value of a field. Returns 'int' if value can be cast into an interger,
    Returns 'float' if value can be casted into a float, Returns False if neither is possible
    """
    try:
        int(number)
        return "int"
    except ValueError:
        try:
            float(number)
            return "float"
        except ValueError:
            return False


def audit_file(filename, fields):
    """
    The audit_file function should return a dictionary containing fieldnames and a
    SET of the types that can be found in the field. e.g.
    {"field1": set([type(float()), type(int()), type(str())]),
    "field2": set([type(str())]),
    ....
    }
    """
    fieldtypes = {
        FIELD: set() for FIELD in FIELDS
    }  # Initializing the fieldtypes to an empty set in other to add non-duplicate values

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            next(reader)

        for row in reader:
            for field in fields:
                if row[field] == "NULL":
                    fieldtypes[field].add(type(None))
                elif checknumber(row[field]) == "int":
                    fieldtypes[field].add(type(int()))
                elif checknumber(row[field]) == "float":
                    fieldtypes[field].add(type(float()))
                elif row[field][0] == "{":
                    fieldtypes[field].add(type(list()))
                else:
                    fieldtypes[field].add(type(str()))

    return fieldtypes


print(audit_file(CITIES, FIELDS))
