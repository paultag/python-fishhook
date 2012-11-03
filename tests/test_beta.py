import os
import sys
import fishhook.core
from fishhook import Hook
from fishhook.service import fire

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "."))
_callees = []


class BetaHook(Hook):
    def fire(self, caller, event, obj):
        global _callees
        _callees.append(caller)


def test_callee():
    global _callees
    fishhook.core.TACKLEBOX = 'tests/resources/tacklebox'

    assert _callees == []
    fire(None, 'beta', {})
    assert _callees == [None]
    fire('foo', 'beta', {})
    assert _callees == [None, 'foo']
    fire('foo', 'alpha', {})
    assert _callees == [None, 'foo']
