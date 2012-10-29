
import os
import json
import importlib
import fishhook.core


def import_by_name(obj_path):
    module, obj = obj_path.rsplit(".", 1)
    mod = importlib.import_module(module)
    fltr = getattr(mod, obj)
    return fltr


def load_by_event(event_name):
    ret = []
    tacklebox = fishhook.core.TACKLEBOX
    modules = os.listdir(tacklebox)
    for module in modules:
        path = os.path.abspath("%s/%s" % (
            tacklebox,
            module
        ))
        obj = json.load(open(path, 'r'))
        if event_name in obj['events']:
            yield import_by_name(obj['path'])
