#!python3
# -*- coding: utf-8 -*-
import urllib.request
import ssl
import json

user = 'my_user'
password = 'my_password'

context = ssl._create_unverified_context()
https_handler = urllib.request.HTTPSHandler(context=context)

pass_mgr = urllib.request.HTTPPasswordMgrWithPriorAuth()
pass_mgr.add_password(None, 'https://api.github.com/repos', user, password, is_authenticated=True)
auth_handler = urllib.request.HTTPBasicAuthHandler(pass_mgr)

opener = urllib.request.build_opener(https_handler, auth_handler)

resp = opener.open('https://api.github.com/users/' + user + '/repos')
repos = json.loads(resp.read())
for repo in repos:
#    print(json.dumps(repo, indent=2))
    print(repo['name'])

    resp = opener.open(repo['url']+'/traffic/views?per=week')
    data = json.loads(resp.read())
    print(' views:', data['uniques'])

    resp = opener.open(repo['url']+'/traffic/clones?per=week')
    data = json.loads(resp.read())
    print(' clones:', data['uniques'])

    resp = opener.open(repo['url']+'/traffic/popular/referrers')
    refs = json.loads(resp.read())
    for ref in refs:
        print(' ref:', ref['referrer'], ref['uniques'])

    resp = opener.open(repo['url']+'/traffic/popular/paths')
    paths = json.loads(resp.read())
    for path in paths:
        print(' path:', path['path'], path['uniques'])
