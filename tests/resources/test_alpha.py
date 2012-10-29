#

from fishhook import Hook


class AlphaHook(Hook):
    def trigger(self, caller, obj):
        pass


def test_fire():
    Hook.emit('alpha', {
        "foo": "foo",
        "bar": "bar",
        "baz": "foo"
    })
