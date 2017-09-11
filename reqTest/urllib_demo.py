# -*- coding: utf-8 -*-

import urllib
import urllib2

URL_IP = "http://httpbin.org/ip"
URL_GET = 'http://httpbin.org/get'

def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print('>>>>Response Headers:')
    print(response.info())
    print('>>>>Response body:')
    print(''.join([line for line in response.readlines()]))
    
def use_params_urllib2():
    params = urllib.urlencode({'param1': 'hello', 'param2': 'world'})
    response = urllib2.urlopen('?'.join([URL_GET, '%s']) % params)
    print('>>>>Response Headers:')
    print(response.info())
    print('>>>>Status Code:')
    print(response.info())
    print('>>>request body:')
    print(''.join([line for line in response.readlines()]))

if __name__ == '__main__':
    print('>>>use simple urllib3')
    use_simple_urllib2()
    print('')
    print('>>>use params urllib3')
    use_params_urllib2()