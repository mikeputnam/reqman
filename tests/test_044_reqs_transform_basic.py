import pytest,reqman


def test_simplest(Reqs):
    y="""
- GET: /<<hello|upper>>
  params:
    upper: return x.upper()
"""
    l=Reqs(y)
    assert len(l) == 1
    ll=l.execute( {"/HELLO" : (200,"ok")} )
    assert ll[0].url == "/HELLO"

def test_simplest_chaining(Reqs):
    y="""
- GET: /<<Hello|upper|lower>>
  params:
    upper: return x.upper()
    lower: return x.lower()
"""
    l=Reqs(y)
    assert len(l) == 1
    ll=l.execute( {"/hello" : (200,"ok")} )
    assert ll[0].url == "/hello"

def test_simplest_transciant(Reqs):
    y="""
- GET: /<<param>>
  params:
    param: <<hello|upper>>
    upper: return x.upper()
"""
    l=Reqs(y,trace=True)
    assert len(l) == 1
    ll=l.execute( {"/HELLO" : (200,"ok")} )
#     assert ll[0].url == "/HELLO"


def test_pass_object_to_method(Reqs):
    y="""
- GET: /<<param>>
  params:
    param: <<data|getVal>>
    data:
        value: "hello"
        nimp: 42
    getVal: return x.get("value")
"""
    l=Reqs(y,trace=True)    
    ll=l.execute( {"/hello" : (200,"ok")} )
    assert ll[0].url == "/hello"

