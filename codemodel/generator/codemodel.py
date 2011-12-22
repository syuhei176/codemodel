# coding: utf-8
import sys

class CodeModel(object):
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.packages = []

class CMElement(object):
    def __init__(self):
        pass

class CMNamedElement(object):
    def __init__(self, name):
        self.name = name

class CMTypedElement(CMNamedElement):
    def __init__(self, name):
        CMNamedElement.__init__(name)

class CMPackage(object):
    def __init__(self, name):
        self.name = name
        self.packages = []

class CMClass(object):
    def __init__(self, name):
        self.name = name
