# Generated from c:/Users/PC/Desktop/PPL/BTL/initial/initial/src/main/minigo/parser/M.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,69,8,3,10,3,
        12,3,72,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,5,4,89,8,4,10,4,12,4,92,9,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,
        100,8,5,10,5,12,5,103,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,
        8,1,8,1,8,1,8,5,8,118,8,8,10,8,12,8,121,9,8,1,8,1,8,1,9,1,9,1,10,
        1,10,1,11,1,11,1,11,0,4,4,6,8,10,12,0,2,4,6,8,10,12,14,16,18,20,
        22,0,0,133,0,25,1,0,0,0,2,31,1,0,0,0,4,37,1,0,0,0,6,50,1,0,0,0,8,
        73,1,0,0,0,10,93,1,0,0,0,12,104,1,0,0,0,14,110,1,0,0,0,16,112,1,
        0,0,0,18,124,1,0,0,0,20,126,1,0,0,0,22,128,1,0,0,0,24,26,3,2,1,0,
        25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,
        0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,32,9,0,0,0,32,3,1,0,0,0,33,34,
        6,2,-1,0,34,38,5,58,0,0,35,36,5,38,0,0,36,38,3,4,2,3,37,33,1,0,0,
        0,37,35,1,0,0,0,38,47,1,0,0,0,39,40,10,2,0,0,40,41,5,36,0,0,41,46,
        3,4,2,3,42,43,10,1,0,0,43,44,5,37,0,0,44,46,3,4,2,2,45,39,1,0,0,
        0,45,42,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,5,1,
        0,0,0,49,47,1,0,0,0,50,51,6,3,-1,0,51,52,5,55,0,0,52,70,1,0,0,0,
        53,54,10,5,0,0,54,55,5,25,0,0,55,69,3,6,3,6,56,57,10,4,0,0,57,58,
        5,26,0,0,58,69,3,6,3,5,59,60,10,3,0,0,60,61,5,27,0,0,61,69,3,6,3,
        4,62,63,10,2,0,0,63,64,5,28,0,0,64,69,3,6,3,3,65,66,10,1,0,0,66,
        67,5,29,0,0,67,69,3,6,3,2,68,53,1,0,0,0,68,56,1,0,0,0,68,59,1,0,
        0,0,68,62,1,0,0,0,68,65,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,7,1,0,0,0,72,70,1,0,0,0,73,74,6,4,-1,0,74,75,5,56,0,0,
        75,90,1,0,0,0,76,77,10,4,0,0,77,78,5,25,0,0,78,89,3,8,4,5,79,80,
        10,3,0,0,80,81,5,26,0,0,81,89,3,8,4,4,82,83,10,2,0,0,83,84,5,27,
        0,0,84,89,3,8,4,3,85,86,10,1,0,0,86,87,5,28,0,0,87,89,3,8,4,2,88,
        76,1,0,0,0,88,79,1,0,0,0,88,82,1,0,0,0,88,85,1,0,0,0,89,92,1,0,0,
        0,90,88,1,0,0,0,90,91,1,0,0,0,91,9,1,0,0,0,92,90,1,0,0,0,93,94,6,
        5,-1,0,94,95,5,57,0,0,95,101,1,0,0,0,96,97,10,1,0,0,97,98,5,25,0,
        0,98,100,3,10,5,2,99,96,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,
        102,1,0,0,0,102,11,1,0,0,0,103,101,1,0,0,0,104,105,5,20,0,0,105,
        106,5,24,0,0,106,107,5,51,0,0,107,108,5,55,0,0,108,109,5,52,0,0,
        109,13,1,0,0,0,110,111,9,0,0,0,111,15,1,0,0,0,112,113,5,12,0,0,113,
        114,5,24,0,0,114,115,5,13,0,0,115,119,5,49,0,0,116,118,3,18,9,0,
        117,116,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,
        120,122,1,0,0,0,121,119,1,0,0,0,122,123,5,50,0,0,123,17,1,0,0,0,
        124,125,9,0,0,0,125,19,1,0,0,0,126,127,9,0,0,0,127,21,1,0,0,0,128,
        129,9,0,0,0,129,23,1,0,0,0,10,27,37,45,47,68,70,88,90,101,119
    ]

class MParser ( Parser ):

    grammarFileName = "M.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'\\n'", "'\\f'", "'\\r'", 
                     "<INVALID>", "<INVALID>", "'if'", "'else'", "'for'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'const'", 
                     "'var'", "'continue'", "'break'", "'range'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
                     "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", 
                     "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "WS", "NL", "FF", "CR", "COMMENT", "MULTIL_COMMENT", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "ID", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", 
                      "LE", "GT", "GE", "AND", "OR", "NOT", "DECL_ASSIGN", 
                      "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "ASSIGN", "DOT", "L_PAREN", "R_PAREN", 
                      "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", "COMMA", 
                      "SEMICOLON", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "BOOL_LIT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_booleanExp = 2
    RULE_intExp = 3
    RULE_floatExp = 4
    RULE_stringExp = 5
    RULE_arrayDecl = 6
    RULE_arrayDimension = 7
    RULE_structDecl = 8
    RULE_structField = 9
    RULE_varDecl = 10
    RULE_typeSpecifiers = 11

    ruleNames =  [ "program", "decl", "booleanExp", "intExp", "floatExp", 
                   "stringExp", "arrayDecl", "arrayDimension", "structDecl", 
                   "structField", "varDecl", "typeSpecifiers" ]

    EOF = Token.EOF
    WS=1
    NL=2
    FF=3
    CR=4
    COMMENT=5
    MULTIL_COMMENT=6
    IF=7
    ELSE=8
    FOR=9
    RETURN=10
    FUNC=11
    TYPE=12
    STRUCT=13
    INTERFACE=14
    STRING=15
    INT=16
    FLOAT=17
    BOOLEAN=18
    CONST=19
    VAR=20
    CONTINUE=21
    BREAK=22
    RANGE=23
    ID=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    EQ=30
    NEQ=31
    LT=32
    LE=33
    GT=34
    GE=35
    AND=36
    OR=37
    NOT=38
    DECL_ASSIGN=39
    ADD_ASSIGN=40
    SUB_ASSIGN=41
    MUL_ASSIGN=42
    DIV_ASSIGN=43
    MOD_ASSIGN=44
    ASSIGN=45
    DOT=46
    L_PAREN=47
    R_PAREN=48
    L_CURLY=49
    R_CURLY=50
    L_BRACKET=51
    R_BRACKET=52
    COMMA=53
    SEMICOLON=54
    INT_LIT=55
    FLOAT_LIT=56
    STRING_LIT=57
    BOOL_LIT=58
    ERROR_CHAR=59
    ILLEGAL_ESCAPE=60
    UNCLOSE_STRING=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.DeclContext)
            else:
                return self.getTypedRuleContext(MParser.DeclContext,i)


        def getRuleIndex(self):
            return MParser.RULE_program




    def program(self):

        localctx = MParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.decl()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4611686018427387902) != 0)):
                    break

            self.state = 29
            self.match(MParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_decl




    def decl(self):

        localctx = MParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_LIT(self):
            return self.getToken(MParser.BOOL_LIT, 0)

        def NOT(self):
            return self.getToken(MParser.NOT, 0)

        def booleanExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.BooleanExpContext)
            else:
                return self.getTypedRuleContext(MParser.BooleanExpContext,i)


        def AND(self):
            return self.getToken(MParser.AND, 0)

        def OR(self):
            return self.getToken(MParser.OR, 0)

        def getRuleIndex(self):
            return MParser.RULE_booleanExp



    def booleanExp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.BooleanExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_booleanExp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [58]:
                self.state = 34
                self.match(MParser.BOOL_LIT)
                pass
            elif token in [38]:
                self.state = 35
                self.match(MParser.NOT)
                self.state = 36
                self.booleanExp(3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = MParser.BooleanExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExp)
                        self.state = 39
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 40
                        self.match(MParser.AND)
                        self.state = 41
                        self.booleanExp(3)
                        pass

                    elif la_ == 2:
                        localctx = MParser.BooleanExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExp)
                        self.state = 42
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 43
                        self.match(MParser.OR)
                        self.state = 44
                        self.booleanExp(2)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IntExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MParser.INT_LIT, 0)

        def intExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.IntExpContext)
            else:
                return self.getTypedRuleContext(MParser.IntExpContext,i)


        def ADD(self):
            return self.getToken(MParser.ADD, 0)

        def SUB(self):
            return self.getToken(MParser.SUB, 0)

        def MUL(self):
            return self.getToken(MParser.MUL, 0)

        def DIV(self):
            return self.getToken(MParser.DIV, 0)

        def MOD(self):
            return self.getToken(MParser.MOD, 0)

        def getRuleIndex(self):
            return MParser.RULE_intExp



    def intExp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.IntExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_intExp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MParser.INT_LIT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MParser.IntExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExp)
                        self.state = 53
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 54
                        self.match(MParser.ADD)
                        self.state = 55
                        self.intExp(6)
                        pass

                    elif la_ == 2:
                        localctx = MParser.IntExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExp)
                        self.state = 56
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 57
                        self.match(MParser.SUB)
                        self.state = 58
                        self.intExp(5)
                        pass

                    elif la_ == 3:
                        localctx = MParser.IntExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExp)
                        self.state = 59
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 60
                        self.match(MParser.MUL)
                        self.state = 61
                        self.intExp(4)
                        pass

                    elif la_ == 4:
                        localctx = MParser.IntExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExp)
                        self.state = 62
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 63
                        self.match(MParser.DIV)
                        self.state = 64
                        self.intExp(3)
                        pass

                    elif la_ == 5:
                        localctx = MParser.IntExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_intExp)
                        self.state = 65
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 66
                        self.match(MParser.MOD)
                        self.state = 67
                        self.intExp(2)
                        pass

             
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FloatExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(MParser.FLOAT_LIT, 0)

        def floatExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.FloatExpContext)
            else:
                return self.getTypedRuleContext(MParser.FloatExpContext,i)


        def ADD(self):
            return self.getToken(MParser.ADD, 0)

        def SUB(self):
            return self.getToken(MParser.SUB, 0)

        def MUL(self):
            return self.getToken(MParser.MUL, 0)

        def DIV(self):
            return self.getToken(MParser.DIV, 0)

        def getRuleIndex(self):
            return MParser.RULE_floatExp



    def floatExp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.FloatExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_floatExp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(MParser.FLOAT_LIT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 88
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MParser.FloatExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExp)
                        self.state = 76
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 77
                        self.match(MParser.ADD)
                        self.state = 78
                        self.floatExp(5)
                        pass

                    elif la_ == 2:
                        localctx = MParser.FloatExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExp)
                        self.state = 79
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 80
                        self.match(MParser.SUB)
                        self.state = 81
                        self.floatExp(4)
                        pass

                    elif la_ == 3:
                        localctx = MParser.FloatExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExp)
                        self.state = 82
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 83
                        self.match(MParser.MUL)
                        self.state = 84
                        self.floatExp(3)
                        pass

                    elif la_ == 4:
                        localctx = MParser.FloatExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_floatExp)
                        self.state = 85
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 86
                        self.match(MParser.DIV)
                        self.state = 87
                        self.floatExp(2)
                        pass

             
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StringExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LIT(self):
            return self.getToken(MParser.STRING_LIT, 0)

        def stringExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.StringExpContext)
            else:
                return self.getTypedRuleContext(MParser.StringExpContext,i)


        def ADD(self):
            return self.getToken(MParser.ADD, 0)

        def getRuleIndex(self):
            return MParser.RULE_stringExp



    def stringExp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MParser.StringExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_stringExp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(MParser.STRING_LIT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MParser.StringExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stringExp)
                    self.state = 96
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 97
                    self.match(MParser.ADD)
                    self.state = 98
                    self.stringExp(2) 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArrayDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MParser.VAR, 0)

        def ID(self):
            return self.getToken(MParser.ID, 0)

        def L_BRACKET(self):
            return self.getToken(MParser.L_BRACKET, 0)

        def INT_LIT(self):
            return self.getToken(MParser.INT_LIT, 0)

        def R_BRACKET(self):
            return self.getToken(MParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return MParser.RULE_arrayDecl




    def arrayDecl(self):

        localctx = MParser.ArrayDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arrayDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MParser.VAR)
            self.state = 105
            self.match(MParser.ID)
            self.state = 106
            self.match(MParser.L_BRACKET)
            self.state = 107
            self.match(MParser.INT_LIT)
            self.state = 108
            self.match(MParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_arrayDimension




    def arrayDimension(self):

        localctx = MParser.ArrayDimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayDimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MParser.TYPE, 0)

        def ID(self):
            return self.getToken(MParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MParser.STRUCT, 0)

        def L_CURLY(self):
            return self.getToken(MParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(MParser.R_CURLY, 0)

        def structField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MParser.StructFieldContext)
            else:
                return self.getTypedRuleContext(MParser.StructFieldContext,i)


        def getRuleIndex(self):
            return MParser.RULE_structDecl




    def structDecl(self):

        localctx = MParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MParser.TYPE)
            self.state = 113
            self.match(MParser.ID)
            self.state = 114
            self.match(MParser.STRUCT)
            self.state = 115
            self.match(MParser.L_CURLY)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 116
                    self.structField() 
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 122
            self.match(MParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_structField




    def structField(self):

        localctx = MParser.StructFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_varDecl




    def varDecl(self):

        localctx = MParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MParser.RULE_typeSpecifiers




    def typeSpecifiers(self):

        localctx = MParser.TypeSpecifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typeSpecifiers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.booleanExp_sempred
        self._predicates[3] = self.intExp_sempred
        self._predicates[4] = self.floatExp_sempred
        self._predicates[5] = self.stringExp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def booleanExp_sempred(self, localctx:BooleanExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def intExp_sempred(self, localctx:IntExpContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def floatExp_sempred(self, localctx:FloatExpContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 1)
         

    def stringExp_sempred(self, localctx:StringExpContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         




