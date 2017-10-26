from __future__ import print_function

import cx_Oracle

connection = cx_Oracle.connect("test", "test", "localhost/orcl")

cursor = connection.cursor()
cursor.execute("""
    SELECT ADMINIST_ZONE_SE, ADMINIST_ZONE_CODE
    FROM COMTCADMINISTCODE
    WHERE ADMINIST_ZONE_SE = :did AND ADMINIST_ZONE_CODE = :eid""",
               did='1',
               eid='3171031022')
for fname, lname in cursor:
    print("Values:", fname, lname)
