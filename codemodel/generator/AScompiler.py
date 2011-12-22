
class Node:
	def __init__(self, type=""):
		self.type = type
		self.value = None
		self.child = []

	def setType(self, type):
		self.type = type

	def setValue(self, value):
		self.value = value

	def addChild(self, child):
		self.child.append(child)

'''
Prototype file of Python parser.
Written by Yu Kobayashi
This file is PUBLIC DOMAIN.
'''

buffer = ""
token = ""
toktype = ""
YYDEFAULTSTACK = 512

YYERRTOK = 256
ARROW = 257
NUMBER = 258
STRING = 259
TYPE_INT = 260
TYPE_STRING = 261
TYPE_BOOLEAN = 262
TYPE_CHAR = 263
TYPE_REAL = 264
TYPE_DATE = 265
CREATE = 266
DELETE = 267
SELECT = 268
RELATE = 269
UNRELATE = 270
GENERATE = 271
CALL = 272
EXTERNAL_CALL = 273
OF = 274
TO = 275
ACROSS = 276
RELATED = 277
BY = 278
FROM = 279
IN = 280
THAT = 281
WHERE = 282
AND = 283
OR = 284
MANY = 285
ONE = 286
IF = 287
ELSEIF = 288
ELSE = 289
FOR = 290
EACH = 291
TRUE = 292
FALSE = 293
EQU = 294
NOTEQU = 295
GTEQ = 296
STEQ = 297
SELF = 298
SELECTED = 299
RCVD_EVT = 300
EMPTY = 301
NOT = 302

	
'''
	#define yyclearin (yychar = -1)
	#define yyerrok (yyerrflag = 0)
	#define YYRECOVERING (yyerrflag != 0)
	#define YYERROR	goto yyerrlab
'''


''' Debug mode flag '''
yydebug = False

''' lexical element object '''
yylval = None

def yyprintln(msg):
	print msg

def yyflush():
	dummy = 0



yytranslate = [ \
	    0,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   10,   66,   66,   66,   66,   66, \
	   63,   64,   59,   57,   65,   58,    3,   60,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   11,    2, \
	   56,    4,   55,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,    8,   66,    9,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,    5,   66,    6,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,   66,   66,   66,   66, \
	   66,   66,   66,   66,   66,   66,    1,    7,   12,   13, \
	   14,   15,   16,   17,   18,   19,   20,   21,   22,   23, \
	   24,   25,   26,   27,   28,   29,   30,   31,   32,   33, \
	   34,   35,   36,   37,   38,   39,   40,   41,   42,   43, \
	   44,   45,   46,   47,   48,   49,   50,   51,   52,   53, \
	   54,   61,   62 \
	]

YYBADCH = 66
YYMAXLEX = 303
YYTERMS = 66
YYNONTERMS = 25

yyaction = [ \
	  113,  122,  133,  200,   99,   33,   13,   39,   40,   71, \
	   41,   37,   95,   42,   93,  -36,    0,   43,   94,  122, \
	  169,  200,   14,   15,   16,   17,    9,   10,    6,   18, \
	   19,  114,   96,   38,  113,   43,   94,   56,   57,  184, \
	  115,  116,  168,   14,   15,   16,   17,  174,  -36,  123, \
	   18,   19,   44,    7,    8,  207,  208,   12,  141,  199, \
	  231,  232,  233,  234,  235,  236,  237,  123,  -67,  167, \
	  164,  -67,   24,  184,  115,  116,  -68,-32766,-32766,  -68, \
	   20,   21,   22,   23,  134,  166,  100,  108,  170,  176, \
	  177,  173,  163,  178,  171,  165,  239,  172,  238,  175, \
	  162,   54,   34,  -67,  -67,   47,   46,   36,   48,   35, \
	  150,  -68,  -68,  153,  152,  155,  154,  202,  241,   69, \
	   70,  146,   45,  106,  107,   29,  110,  109,   98,  151, \
	   30,    0,   25,  -24,  201,   28,  180,  183,  127,   76, \
	  192,  191,  189,  188,  193,  226,  179,    0,  215,  199, \
	    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, \
	    0,   49,   55,   51,    0,  104,  105,  111,    0,    0, \
	   52,   53,    0,   50,    0,  101,    0,  135,    0,   11 \
	]

YYLAST = 180

yycheck = [ \
	   13,   10,   31,   12,   33,    3,    4,   20,   21,   22, \
	   23,   24,   25,   26,   27,    2,    0,   26,   27,   10, \
	    2,   12,   48,   49,   50,   51,   37,   38,   41,   55, \
	   56,   44,   39,   40,   13,   26,   27,   46,   47,   52, \
	   53,   54,    2,   48,   49,   50,   51,    2,   35,   58, \
	   55,   56,   61,   62,   63,   46,   47,   42,   43,   64, \
	   13,   14,   15,   16,   17,   18,   19,   58,    2,    2, \
	    2,    5,   63,   52,   53,   54,    2,   57,   58,    5, \
	   57,   58,   59,   60,   31,    2,   33,   20,    2,    2, \
	    2,    2,    2,    2,    2,    2,    2,    2,    2,    2, \
	    2,   23,    3,   37,   38,    3,    3,    3,    3,    3, \
	    9,   37,   38,    5,    5,    5,    5,   10,    6,    6, \
	    6,    6,   45,    7,    7,   63,    8,    8,   28,    9, \
	   65,   -1,   11,   63,   12,   63,   13,   13,   13,   13, \
	   13,   13,   13,   13,   13,   64,   64,   -1,   64,   64, \
	   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1, \
	   -1,   29,   29,   29,   -1,   30,   30,   30,   -1,   -1, \
	   32,   32,   -1,   33,   -1,   34,   -1,   35,   -1,   36 \
	]

yybase = [ \
	    0,  113,  115,  112,  114,  -13,   -9,   -9,   -9,   -9, \
	   -9,   -9,   -9,    9,    9,    9,    9,    9,    9,    9, \
	    9,    9,    9,    9,    9,    9,   -5,  -26,   47,   47, \
	   47,   68,   85,   21,   21,   21,   21,  126,  126,  124, \
	  124,  124,  124,  124,  124,  124,  124,  124,  124,  124, \
	  124,  124,  124,  124,  124,  124,   66,   74,   23,   23, \
	   23,   23,   23,   23,   23,  109,   53,   84,  110,   15, \
	   15,   -7,    2,  100,   90,  132,   13,  140,  -29,  141, \
	   82,  135,  136,   81,   20,   20,   45,  116,  117,  133, \
	   67,  -11,  137,  123,  123,  131,  130,   62,  129,  129, \
	  129,  130,  143,  143,  128,  128,  129,  129,  127,  128, \
	  128,  128,   16,   70,   77,  103,  102,   91,   72,   89, \
	   99,   88,  125,  122,  106,  142,  134,  107,  104,  105, \
	   87,  121,   98,  138,  139,   78,   97,  108,   93,   83, \
	   86,  111,   96,  119,  118,   92,   94,  101,  120,   95, \
	   40,   18,    0,    0,    0,    0,    0,  -13,  -13,  -13, \
	  -13,    0,   21,   21,   21,   21,   21,   21,   21,   21, \
	   21,   21,   21,   21,   21,   21,   21,   21,   21,   21, \
	   21,   21,   23,   23,    0,    0,    0,   23,   23,    0, \
	    0,    0,    0,   21,   21,   21,   21,   21,   21,   21, \
	   21,   21,   21,   21,   21,   21,   21,   21,   21,   21, \
	   21,   21,    0,    0,    0,    0,    0,    0,    0,    0, \
	    0,  -11,  105,  -11,  -11,    0,    0,    0,    0,  105, \
	  105,  105,    0,  105,    0,  105,   65,  105,  105,   65, \
	   23,   23,  105,  105,  105,  105,    0,    0,  105 \
	]

YY2TBLSTATE = 93

yydefault = [ \
	    2,32767,32767,32767,32767,    1,32767,32767,32767,32767, \
	32767,32767,32767,32767,32767,32767,32767,32767,32767,32767, \
	32767,32767,32767,32767,32767,32767,32767,32767,   71,   71, \
	32767,32767,32767,32767,32767,32767,32767,32767,32767,32767, \
	32767,32767,32767,32767,32767,32767,32767,32767,32767,32767, \
	32767,32767,32767,32767,32767,32767,   51,   52,   60,   61, \
	   64,   65,   62,   63,   74,32767,32767,32767,32767,   84, \
	   84,32767,32767,32767,32767,32767,   27,32767,32767,32767, \
	32767,32767,32767,32767,   39,   40,32767,32767,32767,32767, \
	32767,   54,32767,32767,32767,32767,32767,   69,32767,32767, \
	32767,32767,   53,   53,32767,32767,32767,32767,32767,32767, \
	32767,32767,32767,   27,32767,32767,32767,32767,32767,32767, \
	32767,32767,32767,32767,   38,32767,32767,32767,32767,   66, \
	32767,32767,32767,32767,32767,32767,32767,32767,32767,32767, \
	32767,32767,32767,32767,32767,32767,32767,32767,32767,32767, \
	32767,32767,    2,    2,    2,    2 \
	]



yygoto = [ \
	   72,   72,   72,   72,   72,   26,    1,    2,    3,    4, \
	   31,   58,   59,   60,   61,   62,   63,   84,   85,  197, \
	  198,   32,   64,  117,  117,  117,  117,  117,  125,  242, \
	   83,  137,  185,  185,  185,  185,   77,   66,   73,   74, \
	   75,  120,  128,  129,   79,  186,  187,  185,   81,   82, \
	   86,   87,   88,   89,   92,  130,  136,  206,  205,  214, \
	   67,  212,  213,   91,   68,  102,  103,  229,    0,    0, \
	  140,  139,  143,  144,  147,  148,  149,    0,    0,    0, \
	    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, \
	    0,    0,    0,    0,    0,    0,    0,    0,  145,    0, \
	    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, \
	    0,    0,    0,    0,    0,  121,  203 \
	]

YYGLAST = 117

yygcheck = [ \
	    6,    6,    6,    6,    6,    8,    2,    2,    2,    2, \
	    8,    8,    8,    8,    8,    8,    8,    8,    8,    8, \
	    8,    8,    8,   15,   15,   15,   15,   15,   12,   24, \
	   17,    9,    6,    6,    6,    6,    6,    6,    6,    6, \
	    6,    6,    6,    6,    6,    6,    6,    6,    6,    6, \
	    6,    6,    6,    6,    6,   15,   15,   15,   15,   20, \
	   20,   20,   20,   20,   20,    7,    7,   22,   -1,   -1, \
	   11,   10,    7,    7,   11,   11,   11,   -1,   -1,   -1, \
	   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1, \
	   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   12,   -1, \
	   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1, \
	   -1,   -1,   -1,   -1,   -1,   15,   15 \
	]

yygbase = [ \
	    0,    0, -146,    0,    0,    0,   -1,  -34,   -3,  -70, \
	  -32,  -35,  -10,    0,    0,   22,    0,    1,    0,    0, \
	   52,    0,   37,    0,  -41 \
	]

yygdefault = [ \
	-32768,  112,    5,  159,  160,  161,  124,  132,   27,   78, \
	  138,   90,  119,   97,  126,  204,  118,   80,-32768,-32768, \
	   65,  211,  228,  131,  142 \
	]

yylhs = [ \
	    0,    1,    2,    2,    3,    3,    4,    4,    4,    4, \
	    4,    4,    4,    4,    4,    4,    4,    4,    4,    4, \
	    4,    4,    4,   15,   16,   18,   18,    6,    6,    6, \
	    6,    6,    9,    7,   19,   11,   12,   13,    8,    8, \
	    8,    8,    8,    8,    8,    8,    8,    8,    8,    8, \
	    8,    8,    8,   10,   10,   20,   20,   20,   20,   20, \
	   21,   21,   21,   21,   21,   21,   21,   21,   21,   14, \
	   14,   17,   17,   17,   22,   23,   23,   23,   23,   23, \
	   23,   23,    5,    5,   24,   24,   24 \
	]

yylen = [ \
	    1,    1,    0,    2,    1,    1,    5,    3,    4,    7, \
	    7,    7,   12,   12,    7,    9,   11,    3,    6,    5, \
	    4,    3,    2,    4,    1,    3,    1,    1,    1,    3, \
	    3,    3,    1,    1,    1,    1,    1,    1,    1,    3, \
	    3,    3,    3,    3,    1,    2,    3,    2,    1,    4, \
	    3,    1,    1,    0,    2,    1,    3,    3,    2,    3, \
	    3,    3,    3,    3,    3,    3,    2,    1,    1,    0, \
	    3,    0,    1,    3,    3,    1,    1,    1,    1,    1, \
	    1,    1,    7,    9,    0,    4,    6 \
	]

YYSTATES = 219
YYNLSTATES = 156
YYINTERRTOK = 1
YYUNEXPECTED = 32767
YYDEFAULT = -32766

'''
Parser entry point
'''

def yyparse():
	yyastk = range(YYDEFAULTSTACK)
	yysstk = range(YYDEFAULTSTACK)

	yystate = 0
	yychar = -1

	yysp = 0
	yysstk[yysp] = 0
	yyerrflag = 0
	while True:
		if yybase[yystate] == 0:
			yyn = yydefault[yystate]
		else:
			if yychar < 0:
				yychar = yylex()
				if yychar <= 0:
					yychar = 0
				if yychar < YYMAXLEX:
					yychar = yytranslate[yychar]
				else: 
					yychar = YYBADCH
			yyn = yybase[yystate] + yychar
			goNext = yyn >= 0 and yyn < YYLAST and yycheck[yyn] == yychar
			if not goNext:
				goNext = yystate < YY2TBLSTATE
				if goNext:
					yyn = yybase[yystate + YYNLSTATES] + yychar
					goNext = yyn >= 0 and yyn < YYLAST and yycheck[yyn] == yychar
			if goNext:
				yyn = yyaction[yyn]
				goNext = yyn != YYDEFAULT
			if goNext:
				'''
				 >= YYNLSTATE: shift and reduce
				 > 0: shift
				 = 0: accept
				 < 0: reduce
				 = -YYUNEXPECTED: error
				 '''
				if yyn > 0 :
					''' shift '''
					yysp = yysp + 1

					yysstk[yysp] = yystate = yyn
					yyastk[yysp] = yylval
					yychar = -1
					
					if yyerrflag > 0:
						yyerrflag = yyerrflag - 1
					if yyn < YYNLSTATES:
						continue
						
					''' yyn >= YYNLSTATES means shift-and-reduce '''
					yyn -= YYNLSTATES
				else:
					yyn = -yyn
			else:
				yyn = yydefault[yystate]
		
		while True:
			''' reduce/error '''
			if yyn == 0:
				''' accept '''
				yyflush()
				return 0
			elif yyn != YYUNEXPECTED:
				''' reduce '''
				yyl = yylen[yyn]
				yyval = yyastk[yysp-yyl+1]
				''' Following line will be replaced by reduce actions '''
				if yyn == 1:
					yyval = yyastk[yysp-(1-1)]
					global root
					root = yyval
					
				if yyn == 2:
					n = Node()
					n.setType("PROGRAMS")
					n2 = Node()
					n2.setType("NONE")
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 3:
					n = Node()
					n.setType("PROGRAMS")
					for node in yyastk[yysp-(2-1)].child:
						if node.type != "NONE":
							n.addChild(node)
					n2 = Node()
					n2.setType("PROGRAM")
					n2.addChild(yyastk[yysp-(2-2)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 4:
					n = Node()
					n.setType("ACTION")
					n.addChild(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 5:
					n = Node()
					n.setType("SYNTAX")
					n.addChild(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 6:
					n = Node()
					n.setType("CRE_OBJ")
					n.addChild(yyastk[yysp-(5-2)])
					n.addChild(yyastk[yysp-(5-4)])
					yyval = n
					#print n.type
					
				if yyn == 7:
					n = Node()
					n.setType("DEL_OBJ")
					n.addChild(yyastk[yysp-(3-2)])
					yyval = n
					#print n.type
					
				if yyn == 8:
					n = Node()
					n.setType("WT_ATT")
					n.addChild(yyastk[yysp-(4-1)])
					#n.addChild(attr)
					n.addChild(yyastk[yysp-(4-3)])
					yyval = n
					#print n.type
					
				if yyn == 9:
					n = Node()
					n.setType("SEL_MANY")
					n.addChild(yyastk[yysp-(7-3)])
					n.addChild(yyastk[yysp-(7-5)])
					n.addChild(yyastk[yysp-(7-6)])
					yyval = n
					#print n.type
					
				if yyn == 10:
					n = Node()
					n.setType("SEL_ONE")
					n.addChild(yyastk[yysp-(7-3)])
					n.addChild(yyastk[yysp-(7-5)])
					n.addChild(yyastk[yysp-(7-6)])
					yyval = n
					#print n.type
					
				if yyn == 11:
					n = Node()
					n.setType("CRE_LNK")
					n.addChild(yyastk[yysp-(7-2)])
					n.addChild(yyastk[yysp-(7-4)])
					n.addChild(yyastk[yysp-(7-6)])
					yyval = n
					#print n.type
					
				if yyn == 12:
					n = Node()
					n.setType("TRA_MANY")
					n.addChild(yyastk[yysp-(12-3)])
					n.addChild(yyastk[yysp-(12-6)])
					n.addChild(yyastk[yysp-(12-8)])
					n.addChild(yyastk[yysp-(12-10)])
					yyval = n
					#print n.type
					
				if yyn == 13:
					n = Node()
					n.setType("TRA_ONE")
					n.addChild(yyastk[yysp-(12-3)])
					n.addChild(yyastk[yysp-(12-6)])
					n.addChild(yyastk[yysp-(12-8)])
					n.addChild(yyastk[yysp-(12-10)])
					yyval = n
					#print n.type
					
				if yyn == 14:
					n = Node()
					n.setType("DEL_LNK")
					n.addChild(yyastk[yysp-(7-2)])
					n.addChild(yyastk[yysp-(7-4)])
					n.addChild(yyastk[yysp-(7-6)])
					yyval = n
					#print n.type
					
				if yyn == 15:
					n = Node()
					n.setType("CRE_LNK_OBJ")
					n.addChild(yyastk[yysp-(9-2)])
					n.addChild(yyastk[yysp-(9-4)])
					n.addChild(yyastk[yysp-(9-6)])
					n.addChild(yyastk[yysp-(9-8)])
					yyval = n
					#print n.type
					
				if yyn == 16:
					n = Node()
					n.setType("TRA_LNK_OBJ")
					n.addChild(yyastk[yysp-(11-3)])
					n.addChild(yyastk[yysp-(11-6)])
					n.addChild(yyastk[yysp-(11-8)])
					n.addChild(yyastk[yysp-(11-10)])
					yyval = n
					#print n.type
					
				if yyn == 17:
					n = Node()
					n.setType("DEL_LNK_OBJ")
					n.addChild(yyastk[yysp-(3-2)])
					yyval = n
					#print n.type
					
				if yyn == 18:
					n = Node()
					n.setType("GEN_SIG")
					n.addChild(yyastk[yysp-(6-2)])
					n.addChild(yyastk[yysp-(6-3)])
					n.addChild(yyastk[yysp-(6-5)])
					yyval = n
					#print n.type
					
				if yyn == 19:
					n = Node()
					n.setType("CALL")
					n.addChild(yyastk[yysp-(5-2)])
					n.addChild(yyastk[yysp-(5-4)])
					yyval = n
					#print n.type
					
				if yyn == 20:
					n = Node()
					n.setType("CALL")
					n.addChild(yyastk[yysp-(4-1)])
					n.addChild(yyastk[yysp-(4-3)])
					yyval = n
					#print n.type
					
				if yyn == 21:
					n = Node()
					n.setType("EXTERNAL_CALL")
					n.addChild(yyastk[yysp-(3-2)])
					yyval = n
					#print n.type
					
				if yyn == 22:
					n = Node()
					n.setType("EXTERNAL_CALL")
					n.addChild(yyastk[yysp-(2-1)])
					yyval = n
					#print n.type
					
				if yyn == 23:
					n = Node()
					n.setType("FUNCTION")
					n.addChild(yyastk[yysp-(4-1)])
					n.addChild(yyastk[yysp-(4-3)])
					yyval = n
					#print n.type
					
				if yyn == 24:
					n = Node()
					n.setType("FUNCTION_NAME")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 25:
					n = Node()
					n.setType("FULLY_QUALIFIED_NAME")
					n.setValue(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 26:
					n = Node()
					n.setType("FULLY_QUALIFIED_NAME")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 27:
					n = Node()
					n.setType("OBJ_REF")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 28:
					n = Node()
					n.setType("SELF")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 29:
					n = Node()
					n.setType("OBJ_MEMBER")
					n.setValue("OBJ_MEMBER")
					n.addChild(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 30:
					n = Node()
					n.setType("SELECTED")
					n.setValue(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 31:
					n = Node()
					n.setType("RCVD_EVT")
					n.setValue(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 32:
					n = Node()
					n.setType("OBJ_REFS")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 33:
					n = Node()
					n.setType("CLASS")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 34:
					n = Node()
					n.setType("ATTR")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 35:
					n = Node()
					n.setType("ASSOC")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 36:
					n = Node()
					n.setType("LNK_OBJ")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 37:
					n = Node()
					n.setType("SIG")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 38:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("RD_ATT")
					n2.addChild(yyastk[yysp-(1-1)])
					#n2.addChild(attr)
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 39:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("PLUS")
					n2.addChild(yyastk[yysp-(3-1)])
					n2.addChild(yyastk[yysp-(3-3)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 40:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("MINUS")
					n2.addChild(yyastk[yysp-(3-1)])
					n2.addChild(yyastk[yysp-(3-3)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 41:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("PROD")
					n2.addChild(yyastk[yysp-(3-1)])
					n2.addChild(yyastk[yysp-(3-3)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 42:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("DIV")
					n2.addChild(yyastk[yysp-(3-1)])
					n2.addChild(yyastk[yysp-(3-3)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 43:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("PAR")
					n2.addChild(yyastk[yysp-(3-2)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 44:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("NUMBER")
					n2.setValue(yyastk[yysp-(1-1)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 45:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("NUMBER")
					n2.setValue(yyastk[yysp-(2-2)])
					n2.value = -n2.value
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 46:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("CONST_STRING")
					n2.setValue(yyastk[yysp-(3-2)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 47:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("EXTERNAL_CALL")
					n2.addChild(yyastk[yysp-(2-2)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 48:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("EXTERNAL_CALL")
					n2.addChild(yyastk[yysp-(1-1)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 49:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("CALL")
					n2.addChild(yyastk[yysp-(4-2)])
					n2.addChild(yyastk[yysp-(4-4)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 50:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("CALL")
					n2.addChild(yyastk[yysp-(3-1)])
					n2.addChild(yyastk[yysp-(3-3)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 51:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("TRUE")
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 52:
					n = Node()
					n.setType("EXPR")
					n2 = Node()
					n2.setType("FALSE")
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 53:
					n = Node()
					n.setType("WHERE")
					n2 = Node()
					n2.setType("NONE")
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 54:
					n = Node()
					n.setType("WHERE")
					n.addChild(yyastk[yysp-(2-2)])
					yyval = n
					#print n.type
					
				if yyn == 55:
					n = Node()
					n.setType("CONDS")
					n2 = Node()
					n2.setType("COND")
					n2.addChild(yyastk[yysp-(1-1)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 56:
					n = Node()
					n.setType("CONDS")
					n2 = Node()
					n2.setType("AND")
					n2.addChild(yyastk[yysp-(3-1)])
					n2.addChild(yyastk[yysp-(3-3)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 57:
					n = Node()
					n.setType("CONDS")
					n2 = Node()
					n2.setType("OR")
					n2.addChild(yyastk[yysp-(3-1)])
					n2.addChild(yyastk[yysp-(3-3)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 58:
					n = Node()
					n.setType("CONDS")
					n2 = Node()
					n2.setType("NOT")
					n2.addChild(yyastk[yysp-(2-2)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 59:
					n = Node()
					n.setType("CONDS")
					n2 = Node()
					n2.setType("PAR")
					n2.addChild(yyastk[yysp-(3-2)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 60:
					n = Node()
					n.setType("EQU")
					n.addChild(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 61:
					n = Node()
					n.setType("NOTEQU")
					n.addChild(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 62:
					n = Node()
					n.setType("GT")
					n.addChild(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 63:
					n = Node()
					n.setType("ST")
					n.addChild(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 64:
					n = Node()
					n.setType("GTEQ")
					n.addChild(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 65:
					n = Node()
					n.setType("STEQ")
					n.addChild(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 66:
					n = Node()
					n.setType("EMPTY")
					n.addChild(yyastk[yysp-(2-2)])
					yyval = n
					#print n.type
					
				if yyn == 67:
					n = Node()
					n.setType("TRUE")
					yyval = n
					#print n.type
					
				if yyn == 68:
					n = Node()
					n.setType("FALSE")
					yyval = n
					#print n.type
					
				if yyn == 69:
					n = Node()
					n.setType("ARG")
					n2 = Node()
					n2.setType("NONE")
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 70:
					n = Node()
					n.setType("ARG")
					n2 = Node()
					n2.setType("PAR")
					n2.addChild(yyastk[yysp-(3-2)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 71:
					n = Node()
					n.setType("PARAMS")
					n2 = Node()
					n2.setType("NONE")
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 72:
					n = Node()
					n.setType("PARAMS")
					n.addChild(yyastk[yysp-(1-1)])
					yyval = n
					#print n.type
					
				if yyn == 73:
					n = Node()
					n.setType("PARAMS")
					for node in yyastk[yysp-(3-1)].child:
						if node.type != "NONE":
							n.addChild(node)
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					#print n.type
					
				if yyn == 74:
					n = Node()
					n.setType("PARAM")
					n.addChild(yyastk[yysp-(3-1)])
					n.addChild(yyastk[yysp-(3-3)])
					yyval = n
					
				if yyn == 75:
					n = Node()
					n.setType("TYPE")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					#print n.yyval
					
				if yyn == 76:
					n = Node()
					n.setType("TYPE_INT")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					
				if yyn == 77:
					n = Node()
					n.setType("TYPE_STRING")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					
				if yyn == 78:
					n = Node()
					n.setType("TYPE_BOOLEAN")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					
				if yyn == 79:
					n = Node()
					n.setType("TYPE_CHAR")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					
				if yyn == 80:
					n = Node()
					n.setType("TYPE_REAL")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					
				if yyn == 81:
					n = Node()
					n.setType("TYPE_DATE")
					n.setValue(yyastk[yysp-(1-1)])
					yyval = n
					
				if yyn == 82:
					n = Node()
					n.setType("IF")
					n.addChild(yyastk[yysp-(7-2)])
					n.addChild(yyastk[yysp-(7-4)])
					n.addChild(yyastk[yysp-(7-6)])
					yyval = n
					#print n.type
					
				if yyn == 83:
					n = Node()
					n.setType("FOREACH")
					n.addChild(yyastk[yysp-(9-3)])
					n.addChild(yyastk[yysp-(9-5)])
					n.addChild(yyastk[yysp-(9-7)])
					yyval = n
					#print n.type
					
				if yyn == 84:
					n = Node()
					n.setType("ELSES")
					n2 = Node()
					n2.setType("NONE")
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 85:
					n = Node()
					n.setType("ELSES")
					n2 = Node()
					n2.setType("ELSE")
					n2.addChild(yyastk[yysp-(4-3)])
					n.addChild(n2)
					yyval = n
					#print n.type
					
				if yyn == 86:
					n = Node()
					n.setType("ELSES")
					n2 = Node()
					n2.setType("ELIF")
					n2.addChild(yyastk[yysp-(6-2)])
					n2.addChild(yyastk[yysp-(6-4)])
					n.addChild(n2)
					for node in yyastk[yysp-(6-6)].child:
						if node.type != "NONE":
							n.addChild(node)
					yyval = n
					#print n.type
					
				''' Goto - shift nonterminal '''
				yysp -= yyl
				yyn = yylhs[yyn]
				yyp = yygbase[yyn] + yysstk[yysp]
				if yyp >= 0 and yyp < YYGLAST and yygcheck[yyp] == yyn:
					yystate = yygoto[yyp]
				else:
					yystate = yygdefault[yyn]
					
				yysp = yysp + 1

				yysstk[yysp] = yystate
				yyastk[yysp] = yyval
			else :
				''' error '''
				if yyerrflag == 0:
					yyerror("&error=syntax error")
				if yyerrflag == 0 or yyerrflat == 1 or yyerrflag == 2:
					yyerrflag = 3
					''' Pop until error-expecting state uncovered '''

					while True:
						yyn = yybase[yystate] + YYINTERRTOK
						b = yyn >= 0 and yyn < YYLAST and yycheck[yyn] == YYINTERRTOK
						if not b:
							b = yystate < YY2TBLSTATE
							if b:
								yyn = yybase[yystate + YYNLSTATES] + YYINTERRTOK
								b = yyn >= 0 and yyn < YYLAST and yycheck[yyn] == YYINTERRTOK
						if not b:
							break
						if yysp <= 0:
							yyflush()
							return 1
						yysp = yysp - 1
						yystate = yysstk[yysp]
					yyn = yyaction[yyn]
					yysp = yysp + 1
					yystate = yyn
					yysstk[yysp] = yyn
				elif yyerrflatcase == 3:
					if yychar == 0 :
						yyflush()
						return 1
					yychar = -1
				
			if yystate < YYNLSTATES:
				break
			''' >= YYNLSTATES means shift-and-reduce '''
			yyn = yystate - YYNLSTATES


''' Lexical analyzer '''

token = None
toktype = None
root = None


def isletter(c):
	return (ord('a') <= ord(c) and ord(c) <= ord('z')) or (ord('A') <= ord(c) and ord(c) <= ord('Z')) or (ord('_') == ord(c))

def isdigit(c):
	return (ord('0') <= ord(c) and ord(c) <= ord('9'))

def yylex():
	global buffer, token, toktype, yylval
	while len(buffer) > 0 and (buffer[0] == ' ' or buffer[0] == '\t' or buffer[0] == '\n' or buffer[0] == '\r'):
		buffer = buffer[1:]
	if len(buffer) == 0:
		return 0

	if isletter(buffer[0]):
		i = 0
		while i < len(buffer):
			if not isletter(buffer[i]) and not isdigit(buffer[i]):
				break
			i = i + 1
		token = buffer[:i]
		buffer = buffer[i:]
		
		yylval = token

		#print token
		if token == "create":
			return CREATE
		if token == "delete":
			return DELETE
		if token == "select":
			return SELECT
		if token == "relate":
			return RELATE
		if token == "unrelate":
			return UNRELATE
		if token == "generate":
			return GENERATE
		if token == "call":
			return CALL
		if token == "excall":
			return EXTERNAL_CALL
		if token == "many":
			return MANY
		if token == "one":
			return ONE
		if token == "where":
			return WHERE
		if token == "AND" or token == "and":
			return AND
		if token == "OR" or token == "or":
			return OR
		if token == "if":
			return IF
		if token == "elseif":
			return ELSEIF
		if token == "else":
			return ELSE
		if token == "for":
			return FOR
		if token == "each":
			return EACH
		if token == "TRUE":
			return TRUE
		if token == "FALSE":
			return FALSE
		if token == "to":
			return TO
		if token == "across":
			return ACROSS
		if token == "self":
			return SELF
		if token == "selected":
			return SELECTED
		if token == "rcvd_evt":
			return RCVD_EVT
		if token == "of":
			return OF
		if token == "related":
			return RELATED
		if token == "by":
			return BY
		if token == "from":
			return FROM
		if token == "in":
			return IN
		if token == "EMPTY":
			return EMPTY
		if token == "that":
			return THAT
		if token == "->":
			return ARROW
		if token == "NOT" or token == "not":
			return NOT
		if token == "int":
			return TYPE_INT
		if token == "string":
			return TYPE_STRING
		if token == "boolean":
			return TYPE_BOOLEAN
		if token == "char":
			return TYPE_CHAR
		if token == "real":
			return TYPE_REAL
		if token == "date":
			return TYPE_DATE
		return STRING

	elif isdigit(buffer[0]):
		i = 0
		while i < len(buffer):
			if not isdigit(buffer[i]):
				break
			i = i + 1
		token = buffer[:i]
		#print token
		buffer = buffer[i:]
		yylval = int(token)
		return NUMBER

	else:
		if buffer[0] == "=" and buffer[1] == "=":
				token = buffer[:2]
				buffer = buffer[2:]
				#print "=="
				return EQU
		elif buffer[0] == "!" and buffer[1] == "=":
				token = buffer[:2]
				buffer = buffer[2:]
				print "!="
				return NOTEQU
		elif buffer[0] == ">" and buffer[1] == "=":
				token = buffer[:2]
				buffer = buffer[2:]
				return GTEQ
		elif buffer[0] == "<" and buffer[1] == "=":
				token = buffer[:2]
				buffer = buffer[2:]
				return STEQ
		elif buffer[0] == '-' and buffer[1] == '>':
				token = buffer[:2]
				buffer = buffer[2:]
				return ARROW
		
		elif buffer[0] == '!':
				token = buffer[:1]
				buffer = buffer[1:]
				return NOT
		
		token = buffer[:1]
#		print token
		buffer = buffer[1:]
		return ord(token[0])

def yyerror(msg):
	yyprintln(msg)


buffer = ""

def CompileAS(char):
	global buffer
	buffer = char
	yyparse()
	return root
