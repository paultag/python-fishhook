
import os
import sys
import fishhook.core
from fishhook import Hook
from fishhook.service import fire

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "."))


class AlphaHook(Hook):
    def fire(self, caller, event, obj):
        pass


def test_standard_fire():
    fishhook.core.TACKLEBOX = 'tests/resources/tacklebox'
    fire(None, 'alpha', {
        'foo': 'foo',
        'bar': 'bar',
        'baz': 'foo'
    })
