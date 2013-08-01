#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple python serialization benchmark script, sample output:

Benchmark result:

    Tech           Time(sorted)        Size
    marshal        0.0370650291443     267
    ujson          0.0481259822845     362
    yajl           0.0740070343018     352
    cjosn          0.0746648311615     371
    tnetstring     0.0764350891113     261
    bson           0.0895049571991     242
    msgpack        0.118673801422      204
    json           0.156835079193      375
    dj_simplejson  0.202381849289      375
    simple_json    0.204254150391      375
    c_pickle       0.210531949997      340
    pickle         1.11316609383       338
    yaml           18.1256849766       318

    Tech           Size(sorted)        Time
    msgpack        204                 0.118673801422
    bson           242                 0.0895049571991
    tnetstring     261                 0.0764350891113
    marshal        267                 0.0370650291443
    yaml           318                 18.1256849766
    pickle         338                 1.11316609383
    c_pickle       340                 0.210531949997
    yajl           352                 0.0740070343018
    ujson          362                 0.0481259822845
    cjosn          371                 0.0746648311615
    dj_simplejson  375                 0.202381849289
    json           375                 0.156835079193
    simple_json    375                 0.204254150391
"""

from time import time
import sys
import marshal
import json
import pickle
import cPickle as c_pickle
import msgpack
import bson
import cjson
import ujson
import yaml
import simplejson
import tnetstring
import yajl
from django.utils import simplejson as dj_simplejson


record = {'id': '4a9b87def1c2a2daf1c2e20d',
          'username': 'omidraha',
          'first_name': 'Omid',
          'last_name': 'Raha',
          'date': 1372760951.178409,
          'active': True,
          'email': 'me@example.com',
          'key': u'\xe2\x0c\x9a\x88\xcd\xfa\xfb\xa1\xe0h\x8aT?\xe8\x1b%DRh\xfe\xf3\xf5\x0es)\xa0\xdb\xdf\xf9\xd4rb',
          'signature': u'امید رها'
}

dumpers = {'marshal': lambda data: marshal.dumps(data, 2),
           'bson': lambda data: bson.BSON.encode(data),
           'msgpack': lambda data: msgpack.packb(data),
           'json': lambda data: json.dumps(data),
           'pickle': lambda data: pickle.dumps(data),
           'c_pickle': lambda data: c_pickle.dumps(data),
           'cjosn': lambda data: cjson.encode(data),
           'ujson': lambda data: ujson.dumps(data),
           'simple_json': lambda data: simplejson.dumps(data),
           'dj_simplejson': lambda data: dj_simplejson.dumps(data),
           'yajl': lambda data: yajl.dumps(data),
           'tnetstring': lambda data: tnetstring.dumps(data, "utf8"),
           'yaml': lambda data: yaml.dump(data)
}

s = 0
result = {}
for dumper in dumpers.iterkeys():
    sys.stdout.write('* Benchmark in progress for {} ...               \r'.format(dumper))
    sys.stdout.flush()
    t = time()
    for _ in xrange(10000):
        size = len(dumpers[dumper](record))
    d = time() - t
    result[dumper] = [d, size]

print ' '* 60
print 'Benchmark result:'
print '\n{:<15}{:<20}{}'.format('Tech', 'Time(sorted)', 'Size')
for dumper in sorted(result.keys(),key=lambda x:result[x][0]):
    print "{:<15}{:<20}{}".format(dumper, result[dumper][0], result[dumper][1])

print '\n{:<15}{:<20}{}'.format('Tech', 'Size(sorted)', 'Time')
for dumper in sorted(result.keys(),key=lambda x:result[x][1]):
    print "{:<15}{:<20}{}".format(dumper, result[dumper][1], result[dumper][0])
