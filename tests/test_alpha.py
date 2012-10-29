
from fishhook import Hook


class AlphaHook(Hook):
    pass


def test_standard_fire():
    Hook.emit('alpha', {
        'foo': 'foo',
        'bar': 'bar',
        'baz': 'foo'
    })
