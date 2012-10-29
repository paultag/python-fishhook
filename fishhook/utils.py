# Copyright (c) 2012 Paul Tagliamonte <paultag@debian.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import os
import json
import importlib
import fishhook.core


def import_by_name(obj_path):
    """
    Import a thing by name of obj_path.
    """
    module, obj = obj_path.rsplit(".", 1)
    mod = importlib.import_module(module)
    fltr = getattr(mod, obj)
    return fltr


def load_by_event(event_name):
    """
    Fire off all events that go by event_name.
    """
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
            try:
                yield import_by_name(obj['path'])
            finally:
                pass
