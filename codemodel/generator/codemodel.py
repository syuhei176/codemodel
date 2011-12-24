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

class CMPackage(CMNamedElement):
    def __init__(self, name):
        CMNamedElement.__init__(self, name)
        self.packages = []
        self.classes = []

class CMClass(CMNamedElement):
    def __init__(self, name):
        CMNamedElement.__init__(self, name)
        self.properties = []
        self.operations = []

class CMProperty(CMNamedElement):
    def __init__(self, name, type):
        CMNamedElement.__init__(self, name)
        self.type = type

class CMOperation(CMNamedElement):
    def __init__(self, name, type):
        CMNamedElement.__init__(self, name)
        self.type = type
