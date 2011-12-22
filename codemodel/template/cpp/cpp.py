import sys
import os
from mako.template import Template
from mako.lookup import TemplateLookup
from mako.runtime import Context
from StringIO import StringIO
sys.path.append("../../")
from generator.mc import *

class CPPGenerator(BaseGenerator):
    
    def __init__(self, outpath):
        self.outpath = outpath
    
    def GenerateCode(self, src):
        model = loader.LoadXML(src)
        for p in model.packages:
            self.GeneratePackage(self.outpath, p)
    
    def GeneratePackage(self, path, package):
        current_path = path + '/' + package.name
        if not os.path.exists(current_path):
            os.mkdir(current_path)
        for p in package.packages:
            self.GeneratePackage(current_path, p)
        for c in package.classes:
            self.GenerateClass(current_path + '/' + c.name, c)

    def GenerateClass(self, path, klass):
        self.FileGen(klass, 'template/cpp/header.mako', path)
            
    def FileGen(self, model, in_path, outpath):
        mylookup = TemplateLookup(directories=["./"], output_encoding="utf-8", encoding_errors='replace')
        tmpl = mylookup.get_template(in_path)
        buf = StringIO()
        ctx = Context(buf, root = model)
        tmpl.render_context(ctx)
        hf = open(outpath, 'w')
        hf.write(buf.getvalue())
        hf.close()
