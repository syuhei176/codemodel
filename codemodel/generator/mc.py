import sys
import os
import loader

class Generator(object):
    
    def __init__(self, outpath):
        self.outpath = outpath
    
    def GenerateCode(self, src):
        model = loader.LoadXML(src)
        for p in model.packages:
            self.GeneratePackage(self.outpath, p)
    
    def GeneratePackage(self, path, package):
        if not os.path.exists(path + '/' + package.name):
            os.mkdir(path + '/' + package.name)
        for p in package.packages:
            self.GeneratePackage(path + '/' + package.name, p)