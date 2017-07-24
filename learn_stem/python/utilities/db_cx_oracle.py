# oracle technet blog : Mastering Oracle+Python
# http://www.oracle.com/technetwork/articles/dsl/prez-python-queries-101587.html

import cx_Oracle

# create db connection
db = cx_Oracle.connect('user/pwd@svcname')

# get a cursor
cur=db.cursor()

# run a query
cur.execute("select count(*) from my_table")


# get query result
r = cur.fetchall()
r
# [(15523444,)]

quit()