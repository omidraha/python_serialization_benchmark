Python Serialization Benchmark
==============================

This is a simple python serialization benchmark script.

To do benchmark yourself, run `python run.py`

Here is a sample output of it:

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
