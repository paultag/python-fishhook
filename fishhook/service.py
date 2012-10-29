
from fishhook.utils import load_by_event


class Hook(object):

    @staticmethod
    def emit(self, event, obj):
        print load_by_event(event)
