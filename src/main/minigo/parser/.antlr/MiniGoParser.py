# Generated from c:/Users/PC/Desktop/PPL/BTL/initial/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,62,426,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,115,8,1,1,2,1,2,1,2,1,2,1,2,
        3,2,122,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,132,8,4,1,4,1,4,
        3,4,136,8,4,1,5,1,5,1,5,1,5,3,5,142,8,5,1,6,1,6,1,6,1,6,1,6,1,6,
        3,6,150,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,161,8,7,1,7,
        1,7,1,8,1,8,3,8,167,8,8,1,9,1,9,1,9,1,9,1,9,3,9,174,8,9,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,
        1,13,1,13,3,13,193,8,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,3,18,211,8,18,1,19,1,19,
        1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,3,21,223,8,21,1,22,1,22,
        1,22,1,22,1,22,3,22,230,8,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,3,26,248,8,26,1,27,
        1,27,3,27,252,8,27,1,28,1,28,1,28,1,28,1,28,3,28,259,8,28,1,29,1,
        29,3,29,263,8,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,3,31,278,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,3,32,289,8,32,1,33,1,33,1,33,1,33,3,33,295,8,33,1,33,
        1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,
        1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,
        1,40,1,41,1,41,3,41,327,8,41,1,42,1,42,5,42,331,8,42,10,42,12,42,
        334,9,42,1,42,1,42,1,43,1,43,1,43,1,43,3,43,342,8,43,1,44,1,44,1,
        44,1,44,1,45,1,45,1,45,1,45,1,46,1,46,3,46,354,8,46,1,47,1,47,1,
        47,1,47,1,47,3,47,361,8,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,3,
        48,370,8,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,3,49,379,8,49,1,50,
        1,50,3,50,383,8,50,1,51,1,51,1,51,1,51,1,51,3,51,390,8,51,1,52,1,
        52,1,52,1,52,3,52,396,8,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,
        52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,
        52,1,52,1,52,5,52,421,8,52,10,52,12,52,424,9,52,1,52,0,1,104,53,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,
        90,92,94,96,98,100,102,104,0,8,2,0,21,21,53,53,1,0,9,12,1,0,7,8,
        1,0,36,41,2,0,32,32,46,46,1,0,33,35,1,0,31,32,1,0,47,52,426,0,106,
        1,0,0,0,2,114,1,0,0,0,4,121,1,0,0,0,6,123,1,0,0,0,8,128,1,0,0,0,
        10,137,1,0,0,0,12,143,1,0,0,0,14,153,1,0,0,0,16,166,1,0,0,0,18,173,
        1,0,0,0,20,175,1,0,0,0,22,178,1,0,0,0,24,183,1,0,0,0,26,192,1,0,
        0,0,28,194,1,0,0,0,30,196,1,0,0,0,32,198,1,0,0,0,34,200,1,0,0,0,
        36,210,1,0,0,0,38,212,1,0,0,0,40,215,1,0,0,0,42,222,1,0,0,0,44,229,
        1,0,0,0,46,231,1,0,0,0,48,235,1,0,0,0,50,240,1,0,0,0,52,247,1,0,
        0,0,54,251,1,0,0,0,56,258,1,0,0,0,58,262,1,0,0,0,60,264,1,0,0,0,
        62,277,1,0,0,0,64,279,1,0,0,0,66,290,1,0,0,0,68,298,1,0,0,0,70,304,
        1,0,0,0,72,306,1,0,0,0,74,308,1,0,0,0,76,310,1,0,0,0,78,312,1,0,
        0,0,80,317,1,0,0,0,82,324,1,0,0,0,84,328,1,0,0,0,86,341,1,0,0,0,
        88,343,1,0,0,0,90,347,1,0,0,0,92,353,1,0,0,0,94,360,1,0,0,0,96,369,
        1,0,0,0,98,378,1,0,0,0,100,382,1,0,0,0,102,389,1,0,0,0,104,395,1,
        0,0,0,106,107,3,2,1,0,107,108,5,0,0,1,108,1,1,0,0,0,109,110,3,4,
        2,0,110,111,5,30,0,0,111,112,3,2,1,0,112,115,1,0,0,0,113,115,3,4,
        2,0,114,109,1,0,0,0,114,113,1,0,0,0,115,3,1,0,0,0,116,122,3,6,3,
        0,117,122,3,8,4,0,118,122,3,10,5,0,119,122,3,12,6,0,120,122,3,14,
        7,0,121,116,1,0,0,0,121,117,1,0,0,0,121,118,1,0,0,0,121,119,1,0,
        0,0,121,120,1,0,0,0,122,5,1,0,0,0,123,124,5,13,0,0,124,125,5,21,
        0,0,125,126,5,42,0,0,126,127,3,104,52,0,127,7,1,0,0,0,128,129,5,
        14,0,0,129,131,5,21,0,0,130,132,3,26,13,0,131,130,1,0,0,0,131,132,
        1,0,0,0,132,135,1,0,0,0,133,134,5,42,0,0,134,136,3,104,52,0,135,
        133,1,0,0,0,135,136,1,0,0,0,136,9,1,0,0,0,137,138,5,6,0,0,138,141,
        5,21,0,0,139,142,3,34,17,0,140,142,3,48,24,0,141,139,1,0,0,0,141,
        140,1,0,0,0,142,11,1,0,0,0,143,144,5,5,0,0,144,145,5,21,0,0,145,
        146,5,24,0,0,146,147,3,16,8,0,147,149,5,25,0,0,148,150,3,26,13,0,
        149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,3,84,42,
        0,152,13,1,0,0,0,153,154,5,5,0,0,154,155,3,22,11,0,155,156,5,21,
        0,0,156,157,5,24,0,0,157,158,3,16,8,0,158,160,5,25,0,0,159,161,3,
        26,13,0,160,159,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,163,
        3,84,42,0,163,15,1,0,0,0,164,167,3,18,9,0,165,167,1,0,0,0,166,164,
        1,0,0,0,166,165,1,0,0,0,167,17,1,0,0,0,168,169,3,20,10,0,169,170,
        5,28,0,0,170,171,3,18,9,0,171,174,1,0,0,0,172,174,3,20,10,0,173,
        168,1,0,0,0,173,172,1,0,0,0,174,19,1,0,0,0,175,176,3,86,43,0,176,
        177,3,26,13,0,177,21,1,0,0,0,178,179,5,22,0,0,179,180,5,21,0,0,180,
        181,5,21,0,0,181,182,5,23,0,0,182,23,1,0,0,0,183,184,5,26,0,0,184,
        185,7,0,0,0,185,186,5,27,0,0,186,187,3,26,13,0,187,25,1,0,0,0,188,
        193,3,28,14,0,189,193,3,30,15,0,190,193,3,24,12,0,191,193,3,32,16,
        0,192,188,1,0,0,0,192,189,1,0,0,0,192,190,1,0,0,0,192,191,1,0,0,
        0,193,27,1,0,0,0,194,195,7,1,0,0,195,29,1,0,0,0,196,197,7,2,0,0,
        197,31,1,0,0,0,198,199,5,21,0,0,199,33,1,0,0,0,200,201,5,7,0,0,201,
        202,5,24,0,0,202,203,3,36,18,0,203,204,5,25,0,0,204,35,1,0,0,0,205,
        206,3,38,19,0,206,207,5,30,0,0,207,208,3,36,18,0,208,211,1,0,0,0,
        209,211,3,38,19,0,210,205,1,0,0,0,210,209,1,0,0,0,211,37,1,0,0,0,
        212,213,5,21,0,0,213,214,3,26,13,0,214,39,1,0,0,0,215,216,5,7,0,
        0,216,217,5,24,0,0,217,218,3,42,21,0,218,219,5,25,0,0,219,41,1,0,
        0,0,220,223,3,44,22,0,221,223,1,0,0,0,222,220,1,0,0,0,222,221,1,
        0,0,0,223,43,1,0,0,0,224,225,3,46,23,0,225,226,5,28,0,0,226,227,
        3,44,22,0,227,230,1,0,0,0,228,230,3,46,23,0,229,224,1,0,0,0,229,
        228,1,0,0,0,230,45,1,0,0,0,231,232,5,21,0,0,232,233,5,29,0,0,233,
        234,3,104,52,0,234,47,1,0,0,0,235,236,5,8,0,0,236,237,5,24,0,0,237,
        238,3,50,25,0,238,239,5,25,0,0,239,49,1,0,0,0,240,241,5,21,0,0,241,
        242,5,22,0,0,242,243,3,16,8,0,243,244,5,23,0,0,244,51,1,0,0,0,245,
        248,3,96,48,0,246,248,9,0,0,0,247,245,1,0,0,0,247,246,1,0,0,0,248,
        53,1,0,0,0,249,252,3,56,28,0,250,252,1,0,0,0,251,249,1,0,0,0,251,
        250,1,0,0,0,252,55,1,0,0,0,253,254,3,58,29,0,254,255,5,30,0,0,255,
        256,3,56,28,0,256,259,1,0,0,0,257,259,3,58,29,0,258,253,1,0,0,0,
        258,257,1,0,0,0,259,57,1,0,0,0,260,263,3,4,2,0,261,263,3,60,30,0,
        262,260,1,0,0,0,262,261,1,0,0,0,263,59,1,0,0,0,264,265,3,62,31,0,
        265,266,7,3,0,0,266,267,3,104,52,0,267,61,1,0,0,0,268,278,5,21,0,
        0,269,270,5,21,0,0,270,271,5,43,0,0,271,278,5,21,0,0,272,273,5,21,
        0,0,273,274,5,26,0,0,274,275,3,104,52,0,275,276,5,27,0,0,276,278,
        1,0,0,0,277,268,1,0,0,0,277,269,1,0,0,0,277,272,1,0,0,0,278,63,1,
        0,0,0,279,280,5,1,0,0,280,281,3,104,52,0,281,282,3,84,42,0,282,283,
        5,2,0,0,283,284,5,1,0,0,284,285,3,84,42,0,285,288,1,0,0,0,286,287,
        5,2,0,0,287,289,3,84,42,0,288,286,1,0,0,0,288,289,1,0,0,0,289,65,
        1,0,0,0,290,294,5,3,0,0,291,295,3,104,52,0,292,295,3,68,34,0,293,
        295,3,70,35,0,294,291,1,0,0,0,294,292,1,0,0,0,294,293,1,0,0,0,295,
        296,1,0,0,0,296,297,3,84,42,0,297,67,1,0,0,0,298,299,9,0,0,0,299,
        300,5,30,0,0,300,301,3,104,52,0,301,302,5,30,0,0,302,303,9,0,0,0,
        303,69,1,0,0,0,304,305,9,0,0,0,305,71,1,0,0,0,306,307,5,16,0,0,307,
        73,1,0,0,0,308,309,5,15,0,0,309,75,1,0,0,0,310,311,1,0,0,0,311,77,
        1,0,0,0,312,313,5,21,0,0,313,314,5,22,0,0,314,315,3,100,50,0,315,
        316,5,23,0,0,316,79,1,0,0,0,317,318,5,21,0,0,318,319,5,43,0,0,319,
        320,5,21,0,0,320,321,5,22,0,0,321,322,3,100,50,0,322,323,5,23,0,
        0,323,81,1,0,0,0,324,326,5,4,0,0,325,327,3,104,52,0,326,325,1,0,
        0,0,326,327,1,0,0,0,327,83,1,0,0,0,328,332,5,24,0,0,329,331,3,58,
        29,0,330,329,1,0,0,0,331,334,1,0,0,0,332,330,1,0,0,0,332,333,1,0,
        0,0,333,335,1,0,0,0,334,332,1,0,0,0,335,336,5,25,0,0,336,85,1,0,
        0,0,337,338,5,21,0,0,338,339,5,28,0,0,339,342,3,86,43,0,340,342,
        5,21,0,0,341,337,1,0,0,0,341,340,1,0,0,0,342,87,1,0,0,0,343,344,
        5,24,0,0,344,345,3,92,46,0,345,346,5,25,0,0,346,89,1,0,0,0,347,348,
        5,24,0,0,348,349,3,92,46,0,349,350,5,25,0,0,350,91,1,0,0,0,351,354,
        3,94,47,0,352,354,1,0,0,0,353,351,1,0,0,0,353,352,1,0,0,0,354,93,
        1,0,0,0,355,356,3,98,49,0,356,357,5,28,0,0,357,358,3,94,47,0,358,
        361,1,0,0,0,359,361,3,98,49,0,360,355,1,0,0,0,360,359,1,0,0,0,361,
        95,1,0,0,0,362,370,5,53,0,0,363,370,5,54,0,0,364,370,5,55,0,0,365,
        370,5,19,0,0,366,370,5,20,0,0,367,370,5,18,0,0,368,370,3,88,44,0,
        369,362,1,0,0,0,369,363,1,0,0,0,369,364,1,0,0,0,369,365,1,0,0,0,
        369,366,1,0,0,0,369,367,1,0,0,0,369,368,1,0,0,0,370,97,1,0,0,0,371,
        379,5,53,0,0,372,379,5,54,0,0,373,379,5,55,0,0,374,379,5,19,0,0,
        375,379,5,20,0,0,376,379,5,18,0,0,377,379,3,90,45,0,378,371,1,0,
        0,0,378,372,1,0,0,0,378,373,1,0,0,0,378,374,1,0,0,0,378,375,1,0,
        0,0,378,376,1,0,0,0,378,377,1,0,0,0,379,99,1,0,0,0,380,383,3,102,
        51,0,381,383,1,0,0,0,382,380,1,0,0,0,382,381,1,0,0,0,383,101,1,0,
        0,0,384,385,3,104,52,0,385,386,5,28,0,0,386,387,3,102,51,0,387,390,
        1,0,0,0,388,390,3,104,52,0,389,384,1,0,0,0,389,388,1,0,0,0,390,103,
        1,0,0,0,391,392,6,52,-1,0,392,396,3,52,26,0,393,394,7,4,0,0,394,
        396,3,104,52,6,395,391,1,0,0,0,395,393,1,0,0,0,396,422,1,0,0,0,397,
        398,10,5,0,0,398,399,7,5,0,0,399,421,3,104,52,6,400,401,10,4,0,0,
        401,402,7,6,0,0,402,421,3,104,52,5,403,404,10,3,0,0,404,405,7,7,
        0,0,405,421,3,104,52,4,406,407,10,2,0,0,407,408,5,44,0,0,408,421,
        3,104,52,3,409,410,10,1,0,0,410,411,5,45,0,0,411,421,3,104,52,2,
        412,413,10,8,0,0,413,414,5,26,0,0,414,415,3,104,52,0,415,416,5,27,
        0,0,416,421,1,0,0,0,417,418,10,7,0,0,418,419,5,43,0,0,419,421,5,
        21,0,0,420,397,1,0,0,0,420,400,1,0,0,0,420,403,1,0,0,0,420,406,1,
        0,0,0,420,409,1,0,0,0,420,412,1,0,0,0,420,417,1,0,0,0,421,424,1,
        0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,105,1,0,0,0,424,422,1,
        0,0,0,32,114,121,131,135,141,149,160,166,173,192,210,222,229,247,
        251,258,262,277,288,294,326,332,341,353,360,369,378,382,389,395,
        420,422
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "':'", "';'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'='", "'.'", "'&&'", "'||'", "'!'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ID", "L_PAREN", "R_PAREN", 
                      "L_CURLY", "R_CURLY", "L_BRACKET", "R_BRACKET", "COMMA", 
                      "COLON", "SEMICOLON", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "INIT", "DOT", "AND", 
                      "OR", "NOT", "EQ", "NEQ", "LT", "LE", "GT", "GE", 
                      "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "NL", 
                      "COMMENT", "COMMENT_MULT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declList = 1
    RULE_decl = 2
    RULE_constDecl = 3
    RULE_varDecl = 4
    RULE_typeDecl = 5
    RULE_funcDecl = 6
    RULE_methodDecl = 7
    RULE_paramsList = 8
    RULE_paramPrime = 9
    RULE_param = 10
    RULE_receiver = 11
    RULE_arrayType = 12
    RULE_type = 13
    RULE_primType = 14
    RULE_compType = 15
    RULE_userDefType = 16
    RULE_structType = 17
    RULE_fieldList = 18
    RULE_field = 19
    RULE_structInit = 20
    RULE_fieldInitList = 21
    RULE_fieldInitPrime = 22
    RULE_fieldInit = 23
    RULE_interfaceType = 24
    RULE_methodList = 25
    RULE_primaryExpr = 26
    RULE_statementList = 27
    RULE_statementPrime = 28
    RULE_statement = 29
    RULE_assignStmt = 30
    RULE_lhs = 31
    RULE_ifStmt = 32
    RULE_forStmt = 33
    RULE_forClause = 34
    RULE_rangeClause = 35
    RULE_breakStmt = 36
    RULE_continueStmt = 37
    RULE_callStmt = 38
    RULE_functionCall = 39
    RULE_methodCall = 40
    RULE_returnStmt = 41
    RULE_blockStmt = 42
    RULE_identifierList = 43
    RULE_arrayLit = 44
    RULE_arrayLit_ = 45
    RULE_arrayLitElemList = 46
    RULE_arrayLitElemPrime = 47
    RULE_literal = 48
    RULE_arrayLitElem = 49
    RULE_expressionList = 50
    RULE_expressionPrime = 51
    RULE_expression = 52

    ruleNames =  [ "program", "declList", "decl", "constDecl", "varDecl", 
                   "typeDecl", "funcDecl", "methodDecl", "paramsList", "paramPrime", 
                   "param", "receiver", "arrayType", "type", "primType", 
                   "compType", "userDefType", "structType", "fieldList", 
                   "field", "structInit", "fieldInitList", "fieldInitPrime", 
                   "fieldInit", "interfaceType", "methodList", "primaryExpr", 
                   "statementList", "statementPrime", "statement", "assignStmt", 
                   "lhs", "ifStmt", "forStmt", "forClause", "rangeClause", 
                   "breakStmt", "continueStmt", "callStmt", "functionCall", 
                   "methodCall", "returnStmt", "blockStmt", "identifierList", 
                   "arrayLit", "arrayLit_", "arrayLitElemList", "arrayLitElemPrime", 
                   "literal", "arrayLitElem", "expressionList", "expressionPrime", 
                   "expression" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ID=21
    L_PAREN=22
    R_PAREN=23
    L_CURLY=24
    R_CURLY=25
    L_BRACKET=26
    R_BRACKET=27
    COMMA=28
    COLON=29
    SEMICOLON=30
    ADD=31
    SUB=32
    MUL=33
    DIV=34
    MOD=35
    ASSIGN=36
    ADD_ASSIGN=37
    SUB_ASSIGN=38
    MUL_ASSIGN=39
    DIV_ASSIGN=40
    MOD_ASSIGN=41
    INIT=42
    DOT=43
    AND=44
    OR=45
    NOT=46
    EQ=47
    NEQ=48
    LT=49
    LE=50
    GT=51
    GE=52
    INT_LIT=53
    FLOAT_LIT=54
    STRING_LIT=55
    WS=56
    NL=57
    COMMENT=58
    COMMENT_MULT=59
    ILLEGAL_ESCAPE=60
    UNCLOSE_STRING=61
    ERROR_CHAR=62

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

        def declList(self):
            return self.getTypedRuleContext(MiniGoParser.DeclListContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.declList()
            self.state = 107
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def declList(self):
            return self.getTypedRuleContext(MiniGoParser.DeclListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declList




    def declList(self):

        localctx = MiniGoParser.DeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declList)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.decl()
                self.state = 110
                self.match(MiniGoParser.SEMICOLON)
                self.state = 111
                self.declList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.decl()
                pass


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

        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.constDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.typeDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.funcDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 120
                self.methodDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INIT(self):
            return self.getToken(MiniGoParser.INIT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MiniGoParser.CONST)
            self.state = 124
            self.match(MiniGoParser.ID)
            self.state = 125
            self.match(MiniGoParser.INIT)
            self.state = 126
            self.expression(0)
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

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.TypeContext,0)


        def INIT(self):
            return self.getToken(MiniGoParser.INIT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDecl




    def varDecl(self):

        localctx = MiniGoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(MiniGoParser.VAR)
            self.state = 129
            self.match(MiniGoParser.ID)
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 130
                self.type_()


            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 133
                self.match(MiniGoParser.INIT)
                self.state = 134
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDecl




    def typeDecl(self):

        localctx = MiniGoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MiniGoParser.TYPE)
            self.state = 138
            self.match(MiniGoParser.ID)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 139
                self.structType()
                pass
            elif token in [8]:
                self.state = 140
                self.interfaceType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def paramsList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsListContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockStmtContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.TypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(MiniGoParser.FUNC)
            self.state = 144
            self.match(MiniGoParser.ID)
            self.state = 145
            self.match(MiniGoParser.L_CURLY)
            self.state = 146
            self.paramsList()
            self.state = 147
            self.match(MiniGoParser.R_CURLY)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 69214080) != 0):
                self.state = 148
                self.type_()


            self.state = 151
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def paramsList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsListContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockStmtContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.TypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MiniGoParser.FUNC)
            self.state = 154
            self.receiver()
            self.state = 155
            self.match(MiniGoParser.ID)
            self.state = 156
            self.match(MiniGoParser.L_CURLY)
            self.state = 157
            self.paramsList()
            self.state = 158
            self.match(MiniGoParser.R_CURLY)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 69214080) != 0):
                self.state = 159
                self.type_()


            self.state = 162
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramsList




    def paramsList(self):

        localctx = MiniGoParser.ParamsListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramsList)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.paramPrime()
                pass
            elif token in [23, 25]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramPrime




    def paramPrime(self):

        localctx = MiniGoParser.ParamPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramPrime)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.param()
                self.state = 169
                self.match(MiniGoParser.COMMA)
                self.state = 170
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.TypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.identifierList()
            self.state = 176
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MiniGoParser.L_PAREN)
            self.state = 179
            self.match(MiniGoParser.ID)
            self.state = 180
            self.match(MiniGoParser.ID)
            self.state = 181
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.TypeContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MiniGoParser.L_BRACKET)
            self.state = 184
            _la = self._input.LA(1)
            if not(_la==21 or _la==53):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 185
            self.match(MiniGoParser.R_BRACKET)
            self.state = 186
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimTypeContext,0)


        def compType(self):
            return self.getTypedRuleContext(MiniGoParser.CompTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def userDefType(self):
            return self.getTypedRuleContext(MiniGoParser.UserDefTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type




    def type_(self):

        localctx = MiniGoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.primType()
                pass
            elif token in [7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.compType()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.arrayType()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.userDefType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primType




    def primType(self):

        localctx = MiniGoParser.PrimTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_compType




    def compType(self):

        localctx = MiniGoParser.CompTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_compType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UserDefTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_userDefType




    def userDefType(self):

        localctx = MiniGoParser.UserDefTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_userDefType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def fieldList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldListContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structType




    def structType(self):

        localctx = MiniGoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_structType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MiniGoParser.STRUCT)
            self.state = 201
            self.match(MiniGoParser.L_CURLY)
            self.state = 202
            self.fieldList()
            self.state = 203
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def fieldList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldList




    def fieldList(self):

        localctx = MiniGoParser.FieldListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_fieldList)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.field()
                self.state = 206
                self.match(MiniGoParser.SEMICOLON)
                self.state = 207
                self.fieldList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.field()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniGoParser.TypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MiniGoParser.ID)
            self.state = 213
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def fieldInitList(self):
            return self.getTypedRuleContext(MiniGoParser.FieldInitListContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structInit




    def structInit(self):

        localctx = MiniGoParser.StructInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_structInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.STRUCT)
            self.state = 216
            self.match(MiniGoParser.L_CURLY)
            self.state = 217
            self.fieldInitList()
            self.state = 218
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldInitListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldInitPrime(self):
            return self.getTypedRuleContext(MiniGoParser.FieldInitPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldInitList




    def fieldInitList(self):

        localctx = MiniGoParser.FieldInitListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_fieldInitList)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.fieldInitPrime()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldInitPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldInit(self):
            return self.getTypedRuleContext(MiniGoParser.FieldInitContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def fieldInitPrime(self):
            return self.getTypedRuleContext(MiniGoParser.FieldInitPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldInitPrime




    def fieldInitPrime(self):

        localctx = MiniGoParser.FieldInitPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_fieldInitPrime)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.fieldInit()
                self.state = 225
                self.match(MiniGoParser.COMMA)
                self.state = 226
                self.fieldInitPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.fieldInit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldInit




    def fieldInit(self):

        localctx = MiniGoParser.FieldInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_fieldInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MiniGoParser.ID)
            self.state = 232
            self.match(MiniGoParser.COLON)
            self.state = 233
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def methodList(self):
            return self.getTypedRuleContext(MiniGoParser.MethodListContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceType




    def interfaceType(self):

        localctx = MiniGoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_interfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(MiniGoParser.INTERFACE)
            self.state = 236
            self.match(MiniGoParser.L_CURLY)
            self.state = 237
            self.methodList()
            self.state = 238
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def paramsList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamsListContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodList




    def methodList(self):

        localctx = MiniGoParser.MethodListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_methodList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(MiniGoParser.ID)
            self.state = 241
            self.match(MiniGoParser.L_PAREN)
            self.state = 242
            self.paramsList()
            self.state = 243
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpr




    def primaryExpr(self):

        localctx = MiniGoParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_primaryExpr)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.matchWildcard()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StatementPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementList




    def statementList(self):

        localctx = MiniGoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statementList)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 13, 14, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.statementPrime()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def statementPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StatementPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementPrime




    def statementPrime(self):

        localctx = MiniGoParser.StatementPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statementPrime)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.statement()
                self.state = 254
                self.match(MiniGoParser.SEMICOLON)
                self.state = 255
                self.statementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 13, 14]:
                self.state = 260
                self.decl()
                pass
            elif token in [21]:
                self.state = 261
                self.assignStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.assign_op = None # Token

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStmt




    def assignStmt(self):

        localctx = MiniGoParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.lhs()
            self.state = 265
            localctx.assign_op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4329327034368) != 0)):
                localctx.assign_op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 266
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lhs)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(MiniGoParser.ID)
                self.state = 270
                self.match(MiniGoParser.DOT)
                self.state = 271
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.match(MiniGoParser.ID)
                self.state = 273
                self.match(MiniGoParser.L_BRACKET)
                self.state = 274
                self.expression(0)
                self.state = 275
                self.match(MiniGoParser.R_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IF)
            else:
                return self.getToken(MiniGoParser.IF, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def blockStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockStmtContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStmt




    def ifStmt(self):

        localctx = MiniGoParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MiniGoParser.IF)
            self.state = 280
            self.expression(0)
            self.state = 281
            self.blockStmt()

            self.state = 282
            self.match(MiniGoParser.ELSE)
            self.state = 283
            self.match(MiniGoParser.IF)
            self.state = 284
            self.blockStmt()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 286
                self.match(MiniGoParser.ELSE)
                self.state = 287
                self.blockStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockStmtContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def forClause(self):
            return self.getTypedRuleContext(MiniGoParser.ForClauseContext,0)


        def rangeClause(self):
            return self.getTypedRuleContext(MiniGoParser.RangeClauseContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStmt




    def forStmt(self):

        localctx = MiniGoParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(MiniGoParser.FOR)
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 291
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 292
                self.forClause()
                pass

            elif la_ == 3:
                self.state = 293
                self.rangeClause()
                pass


            self.state = 296
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forClause




    def forClause(self):

        localctx = MiniGoParser.ForClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_forClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.matchWildcard()
            self.state = 299
            self.match(MiniGoParser.SEMICOLON)
            self.state = 300
            self.expression(0)
            self.state = 301
            self.match(MiniGoParser.SEMICOLON)
            self.state = 302
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_rangeClause




    def rangeClause(self):

        localctx = MiniGoParser.RangeClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_rangeClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStmt




    def breakStmt(self):

        localctx = MiniGoParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStmt




    def continueStmt(self):

        localctx = MiniGoParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStmt




    def callStmt(self):

        localctx = MiniGoParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_callStmt)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_functionCall




    def functionCall(self):

        localctx = MiniGoParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(MiniGoParser.ID)
            self.state = 313
            self.match(MiniGoParser.L_PAREN)
            self.state = 314
            self.expressionList()
            self.state = 315
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def L_PAREN(self):
            return self.getToken(MiniGoParser.L_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def R_PAREN(self):
            return self.getToken(MiniGoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCall




    def methodCall(self):

        localctx = MiniGoParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(MiniGoParser.ID)
            self.state = 318
            self.match(MiniGoParser.DOT)
            self.state = 319
            self.match(MiniGoParser.ID)
            self.state = 320
            self.match(MiniGoParser.L_PAREN)
            self.state = 321
            self.expressionList()
            self.state = 322
            self.match(MiniGoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStmt




    def returnStmt(self):

        localctx = MiniGoParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(MiniGoParser.RETURN)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9223372036854775806) != 0):
                self.state = 325
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockStmt




    def blockStmt(self):

        localctx = MiniGoParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MiniGoParser.L_CURLY)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2121824) != 0):
                self.state = 329
                self.statement()
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 335
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_identifierList




    def identifierList(self):

        localctx = MiniGoParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_identifierList)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(MiniGoParser.ID)
                self.state = 338
                self.match(MiniGoParser.COMMA)
                self.state = 339
                self.identifierList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def arrayLitElemList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitElemListContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLit




    def arrayLit(self):

        localctx = MiniGoParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MiniGoParser.L_CURLY)
            self.state = 344
            self.arrayLitElemList()
            self.state = 345
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLit_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(MiniGoParser.L_CURLY, 0)

        def arrayLitElemList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitElemListContext,0)


        def R_CURLY(self):
            return self.getToken(MiniGoParser.R_CURLY, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLit_




    def arrayLit_(self):

        localctx = MiniGoParser.ArrayLit_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arrayLit_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(MiniGoParser.L_CURLY)
            self.state = 348
            self.arrayLitElemList()
            self.state = 349
            self.match(MiniGoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitElemListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayLitElemPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitElemPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLitElemList




    def arrayLitElemList(self):

        localctx = MiniGoParser.ArrayLitElemListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_arrayLitElemList)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 24, 53, 54, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.arrayLitElemPrime()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitElemPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayLitElem(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitElemContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arrayLitElemPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitElemPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLitElemPrime




    def arrayLitElemPrime(self):

        localctx = MiniGoParser.ArrayLitElemPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arrayLitElemPrime)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.arrayLitElem()
                self.state = 356
                self.match(MiniGoParser.COMMA)
                self.state = 357
                self.arrayLitElemPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.arrayLitElem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literal)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 364
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 365
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 366
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 367
                self.match(MiniGoParser.NIL)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 7)
                self.state = 368
                self.arrayLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def arrayLit_(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLit_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLitElem




    def arrayLitElem(self):

        localctx = MiniGoParser.ArrayLitElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arrayLitElem)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 374
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 375
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 376
                self.match(MiniGoParser.NIL)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 7)
                self.state = 377
                self.arrayLit_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionList




    def expressionList(self):

        localctx = MiniGoParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expressionList)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.expressionPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expressionPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionPrime




    def expressionPrime(self):

        localctx = MiniGoParser.ExpressionPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expressionPrime)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.expression(0)
                self.state = 385
                self.match(MiniGoParser.COMMA)
                self.state = 386
                self.expressionPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.unary_op = None # Token
            self.mul_op = None # Token
            self.add_op = None # Token
            self.rel_op = None # Token

        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def L_BRACKET(self):
            return self.getToken(MiniGoParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(MiniGoParser.R_BRACKET, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 392
                self.primaryExpr()
                pass

            elif la_ == 2:
                self.state = 393
                localctx.unary_op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==32 or _la==46):
                    localctx.unary_op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 394
                self.expression(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 420
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 397
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 398
                        localctx.mul_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
                            localctx.mul_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 399
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 400
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 401
                        localctx.add_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==31 or _la==32):
                            localctx.add_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 402
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 403
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 404
                        localctx.rel_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8866461766385664) != 0)):
                            localctx.rel_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 405
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 406
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 407
                        self.match(MiniGoParser.AND)
                        self.state = 408
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 409
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 410
                        self.match(MiniGoParser.OR)
                        self.state = 411
                        self.expression(2)
                        pass

                    elif la_ == 6:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 412
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 413
                        self.match(MiniGoParser.L_BRACKET)
                        self.state = 414
                        self.expression(0)
                        self.state = 415
                        self.match(MiniGoParser.R_BRACKET)
                        pass

                    elif la_ == 7:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 417
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 418
                        self.match(MiniGoParser.DOT)
                        self.state = 419
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[52] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         




