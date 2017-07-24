import requests, time
import numpy as np
import pandas as pd

WS_END_POINT_URL = "https://example.com/osb/FWB_PS"
WS_USERNAME = "user@example.com"
WS_PASSWORD = "Pwd12345"
WS_HEADER = {'Content-Type': 'application/xml'}

# data_file = "test-1.csv"
data_file = "test-2.csv"

df = pd.read_csv(data_file)

# prepare request XML first to avoid ws exception
for n in range(0,len(df)):
    REQUEST_ID = df['REQUEST_ID'][n]
    req_XML = df['FIRST_PAYLOAD'][n]

    try:
        # write out request
        fi = open("req-{}.xml".format(REQUEST_ID), "w")
        fi.write(req_XML)
        fi.close()
    except UnicodeEncodeError as e:
        fie = open("req-{}.err".format(REQUEST_ID), "w")
        fie.write("Error: {}".format(e))
        fie.close()

# invoke ws for each request
for n in range(0,len(df)):
    REQUEST_ID = df['REQUEST_ID'][n]
    req_XML = df['FIRST_PAYLOAD'][n]
    print("n={}: REQUEST_ID={}".format(n,REQUEST_ID))

    try:
        # call ws
        res1 =  requests.post(WS_END_POINT_URL, auth=(WS_USERNAME, WS_PASSWORD), \
                              headers=WS_HEADER, data=req_XML.encode('utf-8'))

        # write out response
        if res1:
            try:
                fo = open("res-{}.xml".format(REQUEST_ID), "w")
                fo.write(res1.text)
                fo.close()
            except UnicodeEncodeError as e:
                foe = open("res-{}.err".format(REQUEST_ID), "w")
                foe.write("Error: {}".format(e))
                foe.close()

    except requests.exceptions.RequestException as e:
        fe = open("res-{}.err".format(REQUEST_ID), "w")
        fe.write("Error: {}".format(e))
        fe.close()
    
    # wait 5 sec before next call
    time.sleep(5)