from generator.mc import *


def testGenerate():
    if not os.path.exists('out'):
        os.mkdir('out')
    infile = file("sample.txt", 'r')
    content = ""
    for line in infile:
       content += line
    gen = Generator('out')
    gen.GenerateCode(content)


testGenerate()