
from abc import abstractmethod
from fishhook.utils import load_by_event


class Hook(object):

    @abstractmethod
    def fire(self, caller, event, obj):
        pass


def fire(caller, event, obj):
    for plugin in load_by_event(event):
        o = plugin()
        o.fire(caller, event, obj)
