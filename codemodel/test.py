import shutil
from template.cpp.cpp import *


def testGenerate():
    if os.path.exists('out'):
        shutil.rmtree('out')
    if not os.path.exists('out'):
        os.mkdir('out')
    infile = file("sample.json", 'r')
    content = ""
    for line in infile:
       content += line
    gen = CPPGenerator('out')
    gen.GenerateCode(content)


testGenerate()