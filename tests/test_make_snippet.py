from lib.make_snippet import *

def test_snip_helicopter():
    result = make_snippet("helicopter")
    assert result == "helic..."