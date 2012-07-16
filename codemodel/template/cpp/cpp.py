import sys
import os
sys.path.append("../../")
from generator.mc import *

class CPPGenerator(BaseGenerator):
    
    def __init__(self, outpath):
        BaseGenerator.__init__(self, outpath)
    
    def GenerateCode(self, src):
        model = dict2object(json.loads(src))
        for p in model.packages:
            self.GeneratePackage(self.outpath, p)
    
    def GeneratePackage(self, path, package):
        current_path = path + '/' + package.name
        if not os.path.exists(current_path):
            os.mkdir(current_path)
        if hasattr(package, 'packages'):
            for p in package.packages:
                self.GeneratePackage(current_path, p)
        if hasattr(package, 'classes'):
            for c in package.classes:
                self.GenerateClass(current_path + '/' + c.name, c)

    def GenerateClass(self, path, klass):
        self.FileGen(klass, 'template/cpp/header.mako', path+'.h')
        self.FileGen(klass, 'template/cpp/code.mako', path+'.cpp')
