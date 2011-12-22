import sys
import os
import loader

class BaseGenerator(object):
    
    def __init__(self, outpath):
        self.outpath = outpath
    
    def GenerateCode(self, src):
        model = loader.LoadXML(src)
        for p in model.packages:
            self.GeneratePackage(self.outpath, p)
            
    def FileGen(self, model, in_path, out_file):
        mylookup = TemplateLookup(directories=[self.path], output_encoding="utf-8", encoding_errors='replace')
        tmpl = mylookup.get_template(in_path)
        buf = StringIO()
        ctx = Context(buf, root = model)
        tmpl.render_context(ctx)
        hf = open(self.outpath + out_file, 'w')
        hf.write(buf.getvalue())
        hf.close()

    
