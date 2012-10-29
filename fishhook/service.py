
from abc import abstractmethod
from fishhook.utils import load_by_event


class Hook(object):

    @abstractmethod
    def fire(self, caller, event, obj):
        pass


def fire(caller, event, obj):
    for plugin in load_by_event(event):
        obj = plugin()
        obj.fire(caller, event, obj)
