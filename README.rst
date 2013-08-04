Python Serialization Benchmark
==============================

This is a simple python serialization benchmark script.

To do benchmark yourself, run ``python run.py``

Here is a sample output of it::

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
