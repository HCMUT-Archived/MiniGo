import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = 1

    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 1))

    def test_002(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+", "+,<EOF>", 2))

    def test_003(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("[]", "[,],<EOF>", 3))

    def test_004(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_VOTien", "_VOTien,<EOF>", 4))

    def test_005(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("12", "12,<EOF>", 5))

    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.checkLexeme("0x11", "0x11,<EOF>", 6))

    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8", "12.e-8,<EOF>", 7))

    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN \\r" """,
                        "\"VOTIEN \\r\",<EOF>", 8))

    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("// VOTIEN", "<EOF>", 9))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("/* VO /* /*TIEN*/ */ SHIBA", "SHIBA,<EOF>", 10))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("^", "ErrorToken ^", 11))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\n" """,
                        "Unclosed string: \"VOTIEN", 12))

    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\\f" """,
                        "Illegal escape in string: \"VOTIEN\\f", 13))

    #!!! 87 test yêu cầu code chấm sau
    def test_014(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("else for return func type struct interface string int float boolean const var continue break range nil true false",
                        "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", 14))

    def test_015(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=",
                        "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>", 15))

    def test_016(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("{}[](),;", "{,},[,],(,),,,;,<EOF>", 16))

    def test_017(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("\t\f\r ", "<EOF>", 17))

    def test_018(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("// tesst //", "<EOF>", 18))

    def test_019(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme(""" /*
        /* a */ /* b */ 
        // 321231
        */ if /* */ /* */""", "if,<EOF>", 19))

    def test_020(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme(""" /*
        /* a /* b /* b */  */  */ 
        */""", "<EOF>", 20))

    def test_021(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme(""" /* //123312
        /* a /* b /* b */  */  */ 
        */""", "<EOF>", 21))

    def test_022(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/*", "/,*,<EOF>", 22))

    def test_023(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/**///", "<EOF>", 23))

    def test_024(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2_bA", "2,_bA,<EOF>", 24))

    def test_025(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 25))

    def test_026(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2b", "2,b,<EOF>", 26))

    def test_027(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("A_2b_3", "A_2b_3,<EOF>", 27))

    def test_028(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_a__", "_a__,<EOF>", 28))

    def test_029(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("u_2_bB", "u_2_bB,<EOF>", 29))

    def test_030(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0452.", "0452.,<EOF>", 30))

    def test_031(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0120", "-,0,120,<EOF>", 31))

    def test_032(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("012", "0,12,<EOF>", 32))

    def test_033(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1_2", "1,_2,<EOF>", 33))

    def test_034(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("12", "12,<EOF>", 34))

    def test_035(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-12", "-,12,<EOF>", 35))

    def test_036(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b000", "0b000,<EOF>", 36))

    def test_037(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b1e", "0b1,e,<EOF>", 37))

    def test_038(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b12", "0b1,2,<EOF>", 38))

    def test_039(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b1101", "0b1101,<EOF>", 39))

    def test_040(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0B111", "0B111,<EOF>", 40))

    def test_041(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("00O72", "0,0O72,<EOF>", 41))

    def test_042(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0O72", "-,0O72,<EOF>", 42))

    def test_043(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0o18", "0o1,8,<EOF>", 43))

    def test_044(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0o12", "0o12,<EOF>", 44))

    def test_045(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0Oo1", "0,Oo1,<EOF>", 45))

    def test_046(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0x2g", "-,0x2,g,<EOF>", 46))

    def test_047(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0X0cb", "0X0cb,<EOF>", 47))

    def test_048(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0xae2", "0xae2,<EOF>", 48))

    def test_049(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0Xx2", "0,Xx2,<EOF>", 49))

    def test_050(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("010.010e-020", "010.010e-020,<EOF>", 50))

    def test_051(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.2e+-2", "1.2,e,+,-,2,<EOF>", 51))

    def test_052(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.2Ee2", "1.2,Ee2,<EOF>", 52))

    def test_053(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("09.e-002", "09.e-002,<EOF>", 53))

    def test_054(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.e-2", "1.e-2,<EOF>", 54))

    def test_055(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.e2", "1.e2,<EOF>", 55))

    def test_056(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.e", "1.,e,<EOF>", 56))

    def test_057(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.", "1.,<EOF>", 57))

    def test_058(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("00.1e2", "00.1e2,<EOF>", 58))

    def test_059(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme(".e+2", ".,e,+,2,<EOF>", 59))

    def test_060(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 60))

    def test_061(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "votien" """, "\"votien\",<EOF>", 61))

    def test_062(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r" """, "\"\\r\",<EOF>", 62))

    def test_063(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\n" """, "\"\\n\",<EOF>", 63))

    def test_064(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\" """, "\"\\\\\",<EOF>", 64))

    def test_065(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\"" """, "\"\\\"\",<EOF>", 65))

    def test_066(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "a \\r a" """, "\"a \\r a\",<EOF>", 66))

    def test_067(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r \\r \\r" """,
                        "\"\\r \\r \\r\",<EOF>", 67))

    def test_068(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" "" """, "\"\",<EOF>", 68))

    def test_069(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" ^ """, "ErrorToken ^", 69))

    def test_070(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" /* @@ * */ """, "<EOF>", 70))

    def test_071(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" 
        /* a * */
 """, "<EOF>", 71))

    def test_072(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" // /* */  """, "<EOF>", 72))

    def test_073(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" // /*
                                       */""", "*,/,<EOF>", 73))

    def test_074(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" 
        /* */ /* */ /*a // */ b""", "b,<EOF>", 74))

    def test_075(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* a */ */ b """, "*,/,b,<EOF>", 75))

    def test_076(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* /* */ a """, "a,<EOF>", 76))

    def test_077(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* a /* b */ */ c /* */""", "c,<EOF>", 77))

    def test_078(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" /* test */ a /* */ """, "a,<EOF>", 78))

    def test_079(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme("""
        /* test
        */ a /* */
""", "a,;,<EOF>", 79))

    def test_080(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" 
    // // //
 """, "<EOF>", 80))

    def test_081(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme("""
// // // """, "<EOF>", 81))

    def test_082(self):
        """COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" // // // """, "<EOF>", 82))

    def test_083(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 83))

    def test_084(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 84))

    def test_085(self):
        """NIL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 85))

    def test_086(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("?", "ErrorToken ?", 86))

    def test_087(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("@", "ErrorToken @", 87))

    def test_088(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("#", "ErrorToken #", 88))

    def test_089(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("\\", "ErrorToken \\", 89))

    def test_090(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("&", "ErrorToken &", 90))

    def test_091(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" 123" """, "123,Unclosed string: \" ", 91))

    def test_092(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123""", "Unclosed string: \"123", 92))

    def test_093(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123 \\n \n" """,
                        "Unclosed string: \"123 \\n ", 93))

    def test_094(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123
        " """, "Unclosed string: \"123", 94))

    def test_095(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123\n" """, "Unclosed string: \"123", 95))

    def test_096(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\" \\\\ \\q" """,
                        "Illegal escape in string: \"\\\" \\\\ \\q", 96))

    def test_097(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "&\\&" """, "Illegal escape in string: \"&\\&", 97))

    def test_098(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\\z" """, "Illegal escape in string: \"\\z", 98))

    def test_099(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\\0" """, "Illegal escape in string: \"\\0", 99))

    def test_100(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\\b" """, "Illegal escape in string: \"\\b", 100))

    def test_101(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            1
""", "1,;,<EOF>", 101))

    def test_102(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            0x1
""", "0x1,;,<EOF>", 102))

    def test_103(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            "s"
""", "\"s\",;,<EOF>", 103))

    def test_104(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            true
""", "true,;,<EOF>", 104))

    def test_105(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            2.
""", "2.,;,<EOF>", 105))

    def test_106(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            ID
""", "ID,;,<EOF>", 106))

    def test_107(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            return
""", "return,;,<EOF>", 107))

    def test_108(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            continue
            break
""", "continue,;,break,;,<EOF>", 108))

    def test_109(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            if
            }
            ]
            )
""", "if,},;,],;,),;,<EOF>", 109))

    def test_110(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 110))

    def test_111(self):
        self.assertTrue(TestLexer.checkLexeme("""
            1e+7
""", "1,e,+,7,;,<EOF>", 111))

    def test_112(self):
        self.assertTrue(TestLexer.checkLexeme("""
           \"12\"\"
""", "\"12\",Unclosed string: \"", 112))

    def test_113(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 113))

    def test_114(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 114))

    def test_115(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 115))

    def test_116(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 116))

    def test_117(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 117))

    def test_118(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil\n/*
*/""", "nil,;,<EOF>", 118))

    def test_119(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil/*
*/\n""", "nil,;,<EOF>", 119))

    def test_120(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil/*
*/""", "nil,<EOF>", 120))

    def test_121(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.checkLexeme("""
            nil
""", "nil,;,<EOF>", 121))
