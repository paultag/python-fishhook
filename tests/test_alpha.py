
import os
import sys
import fishhook.core
from fishhook import Hook
from fishhook.service import fire

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "."))

_test_obj = None

class AlphaHook(Hook):
    def fire(self, caller, event, obj):
        global _test_obj
        _test_obj = obj


def test_standard_fire():
    global _test_obj
    assert _test_obj == None
    fishhook.core.TACKLEBOX = 'tests/resources/tacklebox'

    tobj = {
        'foo': 'foo',
        'bar': 'bar',
        'baz': 'foo'
    }
    fire(None, 'alpha', tobj)
    assert _test_obj == tobj
