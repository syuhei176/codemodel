import sys
import os
from mako.template import Template
from mako.lookup import TemplateLookup
from mako.runtime import Context
from StringIO import StringIO
import loader


class BaseGenerator(object):
    
    def __init__(self, outpath):
        self.outpath = outpath
    
    def GenerateCode(self, src):
        model = loader.LoadXML(src)
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

    
