# coding: utf-8
import sys
import xml.sax as sax
from xml.sax.handler import ContentHandler
from xml.sax.handler import ErrorHandler
from xml.sax.saxutils import unescape
from codemodel import *

class MyHandler(ContentHandler):
        pass

class MyHandler(ContentHandler):

    def __init__(self, root='root'):
        self.root = root
        self.current_node = root
        self.prev_node = None
        self.codemodel = None
        self.current_codemodel = None
        self.current_package = None

    def startElement(self, name, attrs):
        self.prev_node = self.current_node
        self.current_node = name

        if name == "CodeModel":
            attrs_name = attrs.getValue("name")
            if len(attrs_name) == 0:
                print "&error=Model name length = 0"
            else:
                self.current_codemodel = CodeModel(attrs_name, '1.0')

        if name == "Package":
            attrs_name = attrs.getValue("name")
            if len(attrs_name) == 0:
                print "&error=Package name length = 0"
            else:
                if self.current_package == None:
                    p = CMPackage(attrs_name)
                    self.current_codemodel.packages.append(p)
                    self.current_package = p
                else:
                    p = CMPackage(attrs_name)
                    self.current_package.packages.append(p)
                    self.current_package = p                

    def endElement(self, name):
        self.current_node = self.root
        if name == "CodeModel":
            self.codemodel = self.current_codemodel
        if name == "Package":
            pass

    def characters(self, char):
        pass


def decode_xml(str):
    return unescape(str)
#    return str.un('&lt;', '<')

class MyErrorHandler(ErrorHandler):

    def error(exception):
        print "error"
        return exception.getMessage()

    def fatalError(exception):
        print "error2"
        return exception.getMessage()

    def warning(exception):
        print "error3"
        return exception.getMessage()

myhandler = MyHandler()
myErrorHandler = MyErrorHandler()


def LoadXML(content):
    try:
        sax.parseString(content, myhandler)
#, myErrorHandler)
    finally:
        pass
    return myhandler.codemodel

