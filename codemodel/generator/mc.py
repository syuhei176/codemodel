import sys
import os
from mako.template import Template
from mako.lookup import TemplateLookup
from mako.runtime import Context
from StringIO import StringIO
import json


class BaseGenerator(object):
    
    def __init__(self, outpath):
        self.outpath = outpath
    
    def GenerateCode(self, src):
        #model = loader.LoadXML(src)
        model = dict2object(json.loads(src))
        for p in model.packages:
            self.GeneratePackage(self.outpath, p)
    
    def FileGen(self, model, in_path, outpath):
        mylookup = TemplateLookup(directories=["./"], output_encoding="utf-8", encoding_errors='replace')
        tmpl = mylookup.get_template(in_path)
        buf = StringIO()
        ctx = Context(buf, root = model)
        tmpl.render_context(ctx)
        hf = open(outpath, 'w')
        hf.write(buf.getvalue())
        hf.close()

def dict2object(d):
    class klass: pass
    for key in d:
        if isinstance(d[key], dict):
            setattr(klass, key, dict2object(d[key]))
        elif isinstance(d[key], list):
            setattr(klass, key, list2object(d[key]))
        else:
            setattr(klass, key, d[key])
    return klass()

def list2object(l):
    ret = []
    for e in l:
        if isinstance(e, dict):
            ret.append(dict2object(e))
        elif isinstance(e, list):
            ret.append(list2object(e))
        else:
            ret.append(e)
    return ret


    
