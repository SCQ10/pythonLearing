# -*- coding: utf-8 -*-

import requests

BASE_URL = 'https://api.github.com'

# 构建完整的URL
def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])

# 基本认证
def basic_auth():
    response = requests.get(construct_url('users'), auth=('shfanzie', '**********'))
    print response.status_code
    print response.text
    print response.request.headers

# 利用token的基本认证
def basic_oauth():
    headers = {'Authorization': 'token 2ddadfb38e7168520544687aa0598321814944e1'}
    response = requests.get(construct_url('user/emails'), headers=headers)
    print response.request.headers
    print response.text
    print response.status_code

from requests.auth import AuthBase

class GithubAuth(AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        # request加headers信息
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r

def oauth_advanced():
    auth = GithubAuth('2ddadfb38e7168520544687aa0598321814944e1')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print response.request.headers
    print response.text
    print response.status_code

basic_oauth()
print  
oauth_advanced()