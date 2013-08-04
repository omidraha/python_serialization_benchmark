#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple python serialization benchmark script, sample output:

    Benchmark result:

    Serializer               Time(sorted)        Size
    marshal                  0.0351901054382     267
    ujson                    0.0465569496155     362
    yajl                     0.0733790397644     352
    cjosn                    0.0747971534729     371
    tnetstring               0.0766470432281     261
    bson                     0.0918030738831     242
    cpickle version 2        0.0973179340363     263
    cpickle version 1        0.0986309051514     264
    msgpack                  0.122428178787      204
    json                     0.155917167664      375
    django simplejson        0.199804782867      375
    simple json              0.200035095215      375
    cpickle version 0        0.215695858002      340
    jsonpickle               0.993372917175      375
    pickle version 0         1.11252117157       338
    pickle version 1         1.12831997871       264
    pickle version 2         1.13715100288       263
    yaml `libYAML(True)`     18.1359300613       318

    Serializer               Size(sorted)        Time
    msgpack                  204                 0.122428178787
    bson                     242                 0.0918030738831
    tnetstring               261                 0.0766470432281
    pickle version 2         263                 1.13715100288
    cpickle version 2        263                 0.0973179340363
    cpickle version 1        264                 0.0986309051514
    pickle version 1         264                 1.12831997871
    marshal                  267                 0.0351901054382
    yaml `libYAML(True)`     318                 18.1359300613
    pickle version 0         338                 1.11252117157
    cpickle version 0        340                 0.215695858002
    yajl                     352                 0.0733790397644
    ujson                    362                 0.0465569496155
    cjosn                    371                 0.0747971534729
    json                     375                 0.155917167664
    simple json              375                 0.200035095215
    django simplejson        375                 0.199804782867
    jsonpickle               375                 0.993372917175


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
import jsonpickle
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
           'pickle version 0': lambda data: pickle.dumps(data, protocol=0),
           'pickle version 1': lambda data: pickle.dumps(data, protocol=1),
           'pickle version 2': lambda data: pickle.dumps(data, protocol=2),
           'cpickle version 0': lambda data: c_pickle.dumps(data, protocol=0),
           'cpickle version 1': lambda data: c_pickle.dumps(data, protocol=1),
           'cpickle version 2': lambda data: c_pickle.dumps(data, protocol=2),
           'jsonpickle': lambda data: jsonpickle.encode(data),
           'cjosn': lambda data: cjson.encode(data),
           'ujson': lambda data: ujson.dumps(data),
           'simple json': lambda data: simplejson.dumps(data),
           'django simplejson': lambda data: dj_simplejson.dumps(data),
           'yajl': lambda data: yajl.dumps(data),
           'tnetstring': lambda data: tnetstring.dumps(data, "utf8"),
           'yaml `libYAML({})`'.format(yaml.__with_libyaml__): lambda data: yaml.dump(data)
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
print '\n{:<25}{:<20}{}'.format('Serializer', 'Time(sorted)', 'Size')

for dumper in sorted(result.keys(),key=lambda x:result[x][0]):
    print "{:<25}{:<20}{}".format(dumper, result[dumper][0], result[dumper][1])

print '\n{:<25}{:<20}{}'.format('Serializer', 'Size(sorted)', 'Time')
for dumper in sorted(result.keys(),key=lambda x:result[x][1]):
    print "{:<25}{:<20}{}".format(dumper, result[dumper][1], result[dumper][0])
print
