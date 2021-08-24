#!/#!/usr/bin/python3

import shodan
import sys

API_KEY = 'h9qw0xeTqxSb4myUzrlre0Ivf68JnsL8'
if len(sys.argv) == 1:
    print('example : python3 simple-shodan.py apache')
    sys.exit()
try:
        #Setting up the api key
        api = shodan.Shodan(API_KEY)

        #Searching Phase 
        query = sys.argv[1]
        result = api.search(query)

        #locating the matching IP addresses
        for service in result['matches']:
                print(service['ip_str'])
except Exception as e:
        print('Error: {}'.format(e))
        sys.exit(1)

