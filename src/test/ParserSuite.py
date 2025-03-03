import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_001(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = 1;", "successful", 1))

    def test_002(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser("const Votien = true;", "successful", 2))

    def test_003(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser(
            "const Votien = [5][0]string{1, \"string\"};", "successful", 3))

    def test_004(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser(
            "const Votien = [1.]ID{1, 3};", "Error on line 1 col 17: 1.", 4))

    def test_005(self):
        """Literal"""
        self.assertTrue(TestParser.checkParser(
            "const Votien = Person{name: \"Alice\", age: 30};", "successful", 5))

    def test_006(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = 1 || 2 && c + 3 / 2 - -1;",
                        "successful", 6))

    def test_007(self):
        """expression"""
        self.assertTrue(TestParser.checkParser(
            "const Votien = 1[2] + foo()[2] + ID[2].b.b;", "successful", 7))

    def test_008(self):
        """expression"""
        self.assertTrue(TestParser.checkParser(
            "const Votien = ca.foo(132) + b.c[2];", "successful", 8))

    def test_009(self):
        """expression"""
        self.assertTrue(TestParser.checkParser("const Votien = a.a.foo();", "successful", 9))

    def test_010(self):
        """declared variables"""
        self.assertTrue(TestParser.checkParser("""
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        """, "successful", 10))

    def test_011(self):
        """declared constants"""
        self.assertTrue(TestParser.checkParser("""
            const VoTien = a.b() + 2;
        """, "successful", 11))

    def test_012(self):
        """declared function"""
        self.assertTrue(TestParser.checkParser("""
            func VoTien(x int, y int) int {return;}
            func VoTien1() [2][3] ID {return;};        
            func VoTien2() {return;}                                       
        """, "successful", 12))

    def test_013(self):
        """declared method"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) VoTien(x int) int {return;};  
            func (c Calculator) VoTien() ID {return;}      
            func (c Calculator) VoTien(x int, y [2]VoTien) {return;}                                                      
        """, "successful", 13))

    def test_014(self):
        """declared struct"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {
                VoTien string ;
                VoTien [1][3]VoTien ;                     
            }                                                                     
        """, "successful", 14))

    def test_015(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type VoTien struct {}                                                                       
        """, "Error on line 2 col 33: }", 15))

    def test_016(self):
        """declared Interface"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
            type VoTien interface {}                                                                       
        """, "Error on line 11 col 36: }", 16))

    def test_017(self):
        """declared_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                                        
                const VoTien = a.b() + 2;
            }                                       
        """, "successful", 17))

    def test_018(self):
        """assign_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        """, "successful", 18))

    def test_019(self):
        """for_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        """, "successful", 19))

    def test_020(self):
        """if_statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        """, "successful", 20))

    def test_021(self):
        """break and continue, return, Call  statement"""
        self.assertTrue(TestParser.checkParser("""    
            func VoTien() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        """, "successful", 21))

    def test_000(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 0b11;                         
        """, "successful", 0))

    def test_022(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const a = 1.;                         
        """, "successful", 22))

    def test_023(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN 1;                         
        """, "Error on line 2 col 26: 1", 23))

    def test_024(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = int{1};                         
        """, "Error on line 2 col 28: int", 24))

    def test_025(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [true]int{1};                         
        """, "Error on line 2 col 29: true", 25))

    def test_026(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = []int{1};                         
        """, "Error on line 2 col 29: ]", 26))

    def test_027(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = []int{1};                         
        """, "Error on line 2 col 29: ]", 27))

    def test_028(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{1;                         
        """, "Error on line 2 col 36: ;", 28))

    def test_029(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{1,3,4;                         
        """, "Error on line 2 col 40: ;", 29))

    def test_030(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = [2]int{};                         
        """, "Error on line 2 col 35: }", 30))

    def test_031(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {};                         
        """, "successful", 31))

    def test_032(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {a: 2, b: 2 + 2 + ID {a: 1}};                         
        """, "successful", 32))

    def test_033(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = int {};                         
        """, "Error on line 2 col 28: int", 33))

    def test_034(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID + 3;                         
        """, "successful", 34))

    def test_035(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = ID {a: };                         
        """, "Error on line 2 col 35: }", 35))

    def test_036(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = 1 && 2 && 3 || 1 || 1;                         
        """, "successful", 36))

    def test_037(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a >= 2 <= "string" > a[2][3] < ID{A: 2} >= [2]S{2};                         
        """, "successful", 37))

    def test_038(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a + b - [2]int{2} + c - z;                         
        """, "successful", 38))

    def test_039(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a * b / d % e * 2;                         
        """, "successful", 39))

    def test_040(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.b.a.c.e.g;                         
        """, "successful", 40))

    def test_041(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2][3][a + 2];                         
        """, "successful", 41))

    def test_042(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[2, 3];                         
        """, "Error on line 2 col 31: ,", 42))

    def test_043(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a[];                         
        """, "Error on line 2 col 30: ]", 43))

    def test_044(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].foo();                         
        """, "successful", 44))

    def test_045(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].foo(1);                         
        """, "successful", 45))

    def test_046(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1, a.b);                         
        """, "successful", 46))

    def test_047(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = a.a.a[2].c[2].foo(1,);                         
        """, "Error on line 2 col 48: )", 47))

    def test_048(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = foo() + foo(2) + foo(2, 3, 4) + a;                         
        """, "successful", 48))

    def test_049(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = (a + 23) * 3 && (1 + 1);                         
        """, "successful", 49))

    def test_050(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            var z VOTIEN = foo().a[2].goo();                         
        """, "successful", 50))

    def test_051(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = [2]int{1}[3][4].foo();                         
        """, "successful", 51))

    def test_052(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = ID {a : 2}.c[2] + 2[2] + true.foo() + (2).foo();                         
        """, "successful", 52))

    def test_053(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = -a + -!-!c - ---[2]int{2};                         
        """, "successful", 53))

    def test_054(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k = foo() + foo(a{a:2}) + foo(2, 3,4);                         
        """, "successful", 54))

    def test_055(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k =  int;                         
        """, "Error on line 2 col 24: int", 55))

    def test_056(self):
        """Expressions"""
        self.assertTrue(TestParser.checkParser("""    
            const k =  (1, 2);                         
        """, "Error on line 2 col 26: ,", 56))

    def test_057(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a VOTIEN = 2 + 3 / 4;
        """, "successful", 57))

    def test_058(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a [2][3]int = 2 + 3 / 4;
        """, "successful", 58))

    def test_059(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a [][3]int = 2 + 3 / 4;
        """, "Error on line 2 col 20: ]", 59))

    def test_060(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a = a.foo()[2];
        """, "successful", 60))

    def test_061(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a = ;
        """, "Error on line 2 col 21: ;", 61))

    def test_062(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var a 1;
        """, "Error on line 2 col 19: 1", 62))

    def test_063(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]int;
        """, "successful", 63))

    def test_064(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            var c [2][3]ID
        """, "successful", 64))

    def test_065(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a;
        """, "Error on line 2 col 20: ;", 65))

    def test_066(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a := 1 + foo.a[2];
        """, "Error on line 2 col 21: :=", 66))

    def test_067(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            const a =;
        """, "Error on line 2 col 22: ;", 67))

    def test_068(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            
            var a int; var d = 2;
                                        
            var d = 2;
                                        
            const a = 2; var d int = 3;
                                        
            
            var d = 2;""", "successful", 68))

    def test_069(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y [2]int) [2]id {return ;}
""", "successful", 69))

    def test_070(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add() [2]id {return ;}
""", "successful", 70))

    def test_071(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(a) [2]id {return ;}
""", "Error on line 2 col 23: )", 71))

    def test_072(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(int a) int {return ;}
""", "Error on line 2 col 22: int", 72))

    def test_073(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add() {return ;}
""", "successful", 73))

    def test_074(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(a int, ) {}
""", "Error on line 2 col 29: )", 74))

    def test_075(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {value int}
""", "Error on line 2 col 46: }", 75))

    def test_076(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {value int;}
""", "successful", 76))

    def test_077(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                                        
                value int;
                a [2]int; a [2]ID;
                c Calculator                    
            }
""", "successful", 77))

    def test_078(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                c Calculator
                c Cal a int;         
            }
""", "Error on line 4 col 23: a", 78))

    def test_079(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator struct {
                a int = 2;       
            }
""", "Error on line 3 col 23: =", 79))

    def test_080(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
""", "successful", 80))

    def test_081(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()}
""", "Error on line 2 col 47: }", 81))

    def test_082(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset()
        }
""", "successful", 82))

    def test_083(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();}
""", "successful", 83))

    def test_084(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID); Add()
        }
""", "successful", 84))

    def test_085(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {
                Add(x int,c,d ID){}
        }
""", "Error on line 3 col 34: {", 85))

    def test_086(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();} type Person struct{value int;}
""", "Error on line 2 col 50: type", 86))

    def test_087(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            type Calculator interface {Reset();}; type Person struct{value int;}
""", "successful", 87))

    def test_088(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""    
            func Add(x int, y int) int  {return ;};
""", "successful", 88))

    def test_089(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c Calculator) Add(x int) int {return ;}
""", "successful", 89))

    def test_999(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c int) Add(x int) int {return ;}
""", "Error on line 2 col 21: int", 999))

    def test_090(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x int) {return ;}
""", "successful", 90))

    def test_091(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x, c int) {return ;}
""", "successful", 91))

    def test_092(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c [2]c) Add(x int) {return ;}
""", "Error on line 2 col 21: [", 92))

    def test_093(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (int c) Add(x int) {return ;}
""", "Error on line 2 col 19: int", 93))

    def test_094(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
            func (c c) Add(x int) {return ;};
""", "successful", 94))

    def test_095(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            func (c c) Add(x int) {return ;}
                                        
            func Add(x int) {return ;}; var c int;
                                        
            var c int; type Calculator struct{c int;}; type Calculator struct{c int;} var c int;
""", "Error on line 7 col 87: var", 95))

    def test_096(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            var c int func (c c) Add(x int) {return ;}
""", "Error on line 3 col 23: func", 96))

    def test_097(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            const a = 2 func (c c) Add(x int) {return ;}
""", "Error on line 3 col 25: func", 97))

    def test_098(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""
                                        
            const MaxSize = 100 + 50; func (c c) Add() {return ;}
""", "successful", 98))

    def test_099(self):
        """Declared"""
        self.assertTrue(TestParser.checkParser("""

""", "Error on line 3 col 1: <EOF>", 99))

    def test_100(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
            func Add() {
                                        }
""", "successful", 100))

    def test_101(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a int = 2;      
                                    };""", "successful", 101))

    def test_102(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a int;      
                                    };""", "successful", 102))

    def test_103(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         var a = a[2].b;      
                                    };""", "successful", 103))

    def test_104(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                         const a = a[2].b;      
                                    };""", "successful", 104))

    def test_105(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b; var a = "s";           
                                    };""", "successful", 105))

    def test_106(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        const a = a[2].b
                                        var a = a[2].b var a = "s";           
                                    };""", "Error on line 4 col 56: var", 106))

    def test_107(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a += 2;
                                        a -= a[2].b();
                                        a /= 2
                                        a *= 2
                                        a %= 2;       
                                    };""", "successful", 107))

    def test_108(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2].b := 2;       
                                    };""", "successful", 108))

    def test_109(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.c[2].e[3].k += 2;       
                                    };""", "successful", 109))

    def test_110(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo() += 2;       
                                    };""", "Error on line 3 col 49: +=", 110))

    def test_111(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        2 + 2 += 2;       
                                    };""", "Error on line 3 col 41: 2", 111))

    def test_112(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                       ID {id:2}.c += 2;       
                                    };""", "Error on line 3 col 43: {", 112))

    def test_113(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];       
                                    };""", "successful", 113))

    def test_114(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            a := 2;
                                        } else if (a && b) {
                                            return; 
                                        } else {
                                            a := 2;
                                        }   
                                    };""", "successful", 114))

    def test_115(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (){return;}
                                        } 
                                    };""", "Error on line 4 col 49: )", 115))

    def test_116(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (1){return; } else {return; }

                                        } else if(2) {return; 
                                        }
                                    };""", "successful", 116))

    def test_117(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {return
                                        } else if(){
                                        }
                                    };""", "Error on line 4 col 51: )", 117))

    def test_118(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (x.foo().b[2]) {return; 
                                        } else if(1){return; 
                                        }else if(1){return; 
                                        }else if(2){return
                                        }else {return; 
                                        }
                                    };""", "successful", 118))

    def test_119(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true {return; }
                                    };""", "successful", 119))

    def test_120(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for true + 2 + foo().b {return; }
                                    };""", "successful", 120))

    def test_121(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for int {return; }
                                    };""", "Error on line 3 col 45: int", 121))

    def test_122(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for int {return; }
                                    };""", "Error on line 3 col 45: int", 122))

    def test_123(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i := 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""", "successful", 123))

    def test_124(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                           return; 
                                        }
                                    };""", "successful", 124))

    def test_125(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for const i = 0; i < 10; i += 1 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 45: const", 125))

    def test_126(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[3] := 1 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 78: [", 126))

    def test_127(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b();  {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 77: {", 127))

    def test_128(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); var i [2]int = 0 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 76: var", 128))

    def test_129(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""", "successful", 129))

    def test_130(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index[2], value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""", "Error on line 3 col 53: ,", 130))

    def test_131(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index.ab, value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        return; 
                                        }
                                    };""", "Error on line 3 col 53: ,", 131))

    def test_132(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value[2] := range arr {
                                        // index: 0, 1, 2
                                        return; 
                                        }
                                    };""", "Error on line 3 col 57: [", 132))

    def test_133(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range arr[2] {return
                                        }
                                    };""", "successful", 133))

    def test_134(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {return; 
                                        }
                                    };""", "successful", 134))

    def test_135(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for index, value := range 23 {
                                            for index, value := range 23 {return; }
                                        }
                                    };""", "successful", 135))

    def test_136(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        break;
                                        continue
                                        break; continue; break
                                    };""", "successful", 136))

    def test_137(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return
                                        return 2 + a[2].b()
                                        return; return a
                                    };""", "successful", 137))

    def test_138(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return return 2 + a[2].b()
                    
                                    };""", "Error on line 3 col 48: return", 138))

    def test_139(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        break continue
                    
                                    };""", "Error on line 3 col 47: continue", 139))

    def test_140(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo();
                                        foo()
                                    };""", "successful", 140))

    def test_141(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a.foo(2 + 3, a {a:2})
                                        foo(2 + 3, a {a:2});
                                    };""", "successful", 141))

    def test_142(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        (1+2).foo(2 + 3, a {a:2})
                                    };""", "Error on line 3 col 41: (", 142))

    def test_143(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };""", "successful", 143))

    def test_144(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        {break;}
                                    };""", "Error on line 3 col 41: {", 144))

    def test_145(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                        break;
                                    func Add() {
                                    };""", "Error on line 2 col 41: break", 145))

    def test_146(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return (2 + 3).b
                                        return -1.c
                                    };""", "Error on line 4 col 51: c", 146))

    def test_147(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        return (2 + 3)[b]
                                        return -1.c[c]
                                    };""", "Error on line 4 col 51: c", 147))

    def test_148(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return struct;}
                                        else if(2) {return string;}
                                        else if(3) {reutrn int;}
                                    };""", "Error on line 3 col 56: struct", 148))

    def test_149(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}
                                    };""", "Error on line 3 col 76: string", 149))

    def test_150(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        if (1) {return;}else if(2) {return string;}else if(3) {reutrn int;}else  {return struct;}
                                    };""", "Error on line 3 col 76: string", 150))

    def test_151(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{1+1}                    
""", "Error on line 1 col 19: +", 151))

    def test_152(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{}, {{ID{}}}}                    
""", "successful", 152))

    def test_153(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{}                    
""", "Error on line 1 col 18: }", 153))

    def test_154(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{[1]int{1}}                    
""", "Error on line 1 col 18: [", 154))

    def test_155(self):
        """array_literal"""
        self.assertTrue(TestParser.checkParser("""const a = [1]int{{1, 0x1}, ID{}, 1.2, "s", true, false, nil} + nil                    
""", "successful", 155))

    def test_156(self):
        self.assertTrue(TestParser.checkParser("""
        func Add(x, y int, b float) {return ;}           
""", "successful", 156))

    def test_157(self):
        self.assertTrue(TestParser.checkParser("""
        func (c c) Add(x, y int, b float) {return ;}           
""", "successful", 157))

    def test_158(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }
            c c
            func (c c) Add(x, y int, b float) {return ;}  
            value int;                            
        }      
""", "successful", 158))

    def test_998(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            c int  c int;                                                    
        }      
""", "Error on line 3 col 20: c", 998))

    def test_159(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1 
                {
                    return
                }
            };  
""", "Error on line 10 col 29: ;", 159))

    def test_160(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;}
                else if (1)
                {}
            };  
""", "Error on line 4 col 17: else", 160))

    def test_161(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;
                }else if (1) {}
            };  
""", "successful", 161))

    def test_162(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {return;
                }else {}
            };  
""", "successful", 162))

    def test_163(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                if (1) {}
            };  
""", "successful", 163))

    def test_164(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i < 10 {
// loop body
}
            };  
""", "successful", 164))

    def test_165(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for i := 0; i < 10; i += 1 {
// loop body
}
            };  
""", "successful", 165))

    def test_166(self):
        self.assertTrue(TestParser.checkParser("""
            func (p Person) Greet() string {
                for index, value := range STRUCT{} {
// loop body                                   
};
            };  
""", "successful", 166))

    def test_167(self):
        self.assertTrue(TestParser.checkParser("""
        const a = a.2; 
""", "Error on line 2 col 21: 2", 167))

    def test_168(self):
        self.assertTrue(TestParser.checkParser("""
        const a = a.b.c().d().e[2].k()[2]; 
""", "successful", 168))

    def test_169(self):
        self.assertTrue(TestParser.checkParser("""
        const a = [1]int{1, 2 
""", "Error on line 2 col 32: ;", 169))

    def test_170(self):
        self.assertTrue(TestParser.checkParser("""
        const a = foo(1, 2
""", "Error on line 2 col 28: ;", 170))

    def test_171(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i.b := 1 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 78: .", 171))

    def test_172(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var i [2] int = 0; foo().a.b(); i[2].c += 1 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 78: [", 172))

    def test_173(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 50: :=", 173))

    def test_174(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i.c[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 52: :=", 174))

    def test_175(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for i.c[2] := 1; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 52: :=", 175))

    def test_176(self):
        self.assertTrue(TestParser.checkParser("""
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            };                                                 
        }      
""", "Error on line 3 col 13: func", 176))

    def test_177(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 50: ;", 177))

    def test_178(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b int; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""", "Error on line 3 col 54: ;", 178))

    def test_179(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        for var b [2]ID = 1 + 2 / 4; foo().a.b(); i := 1 {
                                            return; 
                                        }
                                    };""", "successful", 179))

    def test_180(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [ID][2][VT]int{{{1}}, ID, a, {b}}                              
                                        """, "successful", 180))

    def test_181(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a;
                                        """, "Error on line 2 col 50: ;", 181))

    def test_182(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a = {1, 2};
                                        """, "Error on line 2 col 53: {", 182))

    def test_183(self):
        self.assertTrue(TestParser.checkParser("""
                                            var a = {1, 2};
                                        """, "Error on line 2 col 53: {", 183))

    def test_184(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                        {
                                            return;
                                        }
                                    };""", "Error on line 3 col 41: {", 184))

    def test_185(self):
        self.assertTrue(TestParser.checkParser("""
                                            const a = [ID][2][VT]int{a, b, {c}}                              
                                        """, "successful", 185))

    def test_186(self):
        """Statement"""
        self.assertTrue(TestParser.checkParser("""
                                    func Add() {
                                            return;
                                    };""", "successful", 186))
