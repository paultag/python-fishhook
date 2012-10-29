
import importlib
import fishhook.core


def import_by_name(obj_path):
    module, obj = obj_path.rsplit(".", 1)
    mod = importlib.import_module(module)
    fltr = getattr(mod, obj)
    return fltr


def load_by_event(event_name):
    ret = []
    tacklebox = fishhook.core.tacklebox_path
    print tacklebox
    return ret
