grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
    self.lastTokenType = 0;

    def cust_emit():
        tk =  super(MiniGoLexer,self).emit()
        self.lastTokenType = tk.type
        return super(MiniGoLexer,self).emit();

    self.emit = cust_emit
}

options{
	language = Python3;
}

// non empty list of x >>> xlist : x xlist | x;

// nullable list of x >>> xlist : x xlist | ;

// non empty list of x separated by y >>> xlist : x y xlist | x;

// nullable list of x separated by y >>> xlist : xprime | ; xprime : x y xprime | x;

/******************************************************************************/
/*                                                                            */
/*                     PARSER RULES                                           */
/*                                                                            */
/******************************************************************************/

program: declList EOF;

// non empty list of x >>> xlist : x xlist | x;
declList: decl declList | decl;
decl: (varDecl | constDecl | funcDecl | methodDecl | typeDecl) SEMICOLON;

constDecl: CONST ID INIT expression;
varDecl: VAR ID (goType (INIT expression)? | INIT expression);
funcDecl: FUNC ID L_PAREN paramsList R_PAREN goType? block;
methodDecl: FUNC L_PAREN receiver R_PAREN ID L_PAREN paramsList R_PAREN goType? block;

receiver: ID ID;

// nullable list of x separated by y >>> xlist : xprime | ; xprime : x y xprime | x;
paramsList: paramPrime |;
paramPrime: param COMMA paramPrime | param;
param: identifierList goType;

// non empty list of x separated by y >>> xlist : x y xlist | x;
identifierList: ID COMMA identifierList | ID;

typeDecl: TYPE ID (structType | interfaceType);

/******************************************************************************/
// =================== TYPING ==================================================

goType: STRING | INT | FLOAT | BOOLEAN | arrayType | ID;

// =================== ARRAY TYPE ==============================================

arrayType: dimensionList goType;
// non empty list of x >>> xlist : x xlist | x;
dimensionList: dimension dimensionList | dimension;
dimension: L_BRACKET (INT_LIT | ID) R_BRACKET;

// =================== STRUCT TYPE =============================================

// must have at least 1 property, can have no methods
structType: STRUCT L_CURLY structFieldList R_CURLY;
// non empty list of x >>> xlist : x xlist | x;
structFieldList: structField structFieldList | structField;
structField: structProp | structMethod;
structProp: ID goType SEMICOLON;
structMethod: methodDecl SEMICOLON;

// =================== INTERFACE TYPE ==========================================

interfaceType: INTERFACE L_CURLY interfaceMethodList R_CURLY;
// non empty list of x >>> xlist : x xlist | x;
interfaceMethodList: interfaceMethod interfaceMethodList | interfaceMethod;
interfaceMethod: ID L_PAREN paramsList R_PAREN goType? SEMICOLON;

/******************************************************************************/
// =================== STATEMENTS ==============================================

// every statement ends with a semicolon

block: L_CURLY statementList R_CURLY;
// nullable list of x >>> xlist : x xlist | ;
statementList: statement statementList |;
statement: (varDecl | constDecl | assignStmt | ifStmt | forStmt | breakStmt | continueStmt | callStmt | returnStmt) SEMICOLON;
assignStmt: lhs ( ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expression;
lhs: ID | elemAccess;
elemAccess: elemAccess L_BRACKET expression R_BRACKET | elemAccess DOT elemAccess | ID;

ifStmt: IF L_PAREN expression R_PAREN block (ELSE (ifStmt | block))?;

forStmt: FOR (expression | forClause | forRangeClause) block;
forClause: forInit SEMICOLON expression SEMICOLON forAssignStmt;
forInit: forAssignStmt | forDeclaration;
forAssignStmt: ID (ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expression;
forDeclaration: VAR ID goType? INIT expression;
forRangeClause: ID COMMA ID ASSIGN RANGE expression;

breakStmt: BREAK;
continueStmt: CONTINUE;
callStmt: methodCall | functionCall;
methodCall: (ID | elemAccess) DOT ID L_PAREN expressionList R_PAREN;
functionCall: ID L_PAREN expressionList R_PAREN;

returnStmt: RETURN expression?;

/******************************************************************************/
// =================== EXPRESSIONS =============================================

arrayLit: arrayType L_CURLY arrayLitElemList R_CURLY;
arrayLit_: L_CURLY arrayLitElemList R_CURLY;
// non empty list of x separated by y >>> xlist : x y xlist | x;
arrayLitElemList: arrayLitElem COMMA arrayLitElemList | arrayLitElem;
arrayLitElem: ID | INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | arrayLit_ | structLit;

// nullable list of x separated by y >>> xlist : xprime | ; xprime : x y xprime | x;
structLit: ID L_CURLY structLitFieldList R_CURLY;
structLitFieldList: structLitFieldPrime |;
structLitFieldPrime: structLitField COMMA structLitFieldPrime | structLitField;
structLitField: ID COLON expression;

literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | arrayLit | structLit;

// nullable list of x separated by y >>> xlist : xprime | ; xprime : x y xprime | x;
expressionList: expressionPrime |;
expressionPrime: expression COMMA expressionPrime | expression;
expression: expOr;
expOr: expAnd | expOr OR expAnd;
expAnd: expRel | expAnd AND expRel;
expRel: expAdd | expRel (EQ | NEQ | LT | LE | GT | GE) expAdd;
expAdd: expMul | expAdd (ADD | SUB) expMul;
expMul: expUnary | expMul (MUL | DIV | MOD) expUnary;
expUnary: expAcc | (NOT | SUB) expUnary;
expAcc: operand | expAcc L_BRACKET expression R_BRACKET | expAcc DOT (ID | functionCall);

operand: L_PAREN expression R_PAREN | ID | literal | callStmt;

/******************************************************************************/
/*                                                                            */
/*                     LEXER RULES                                            */
/*                                                                            */
/******************************************************************************/

// keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

// identifier (after keywords)

ID: [a-zA-Z_][a-zA-Z0-9_]*;

// separators

L_PAREN: '(';
R_PAREN: ')';
L_CURLY: '{';
R_CURLY: '}';
L_BRACKET: '[';
R_BRACKET: ']';
COMMA: ',';
COLON: ':';
SEMICOLON: ';';

// operators 13

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

ASSIGN: ':=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';

INIT: '=';
DOT: '.';

// logical operators 2

AND: '&&';
OR: '||';

// unary operators 1

NOT: '!';

// relational operators 6

EQ: '==';
NEQ: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';

// literals
INT_LIT: DECIMAL_LIT | BIN_LIT | OCTAL_LIT | HEX_LIT;
fragment DECIMAL_LIT: ('0' | [1-9] [0-9]*);
fragment BIN_LIT: '0' [bB] [01]+;
fragment OCTAL_LIT: '0' [oO] [0-7]+;
fragment HEX_LIT: '0' [xX] [0-9a-fA-F]+;

// is 0.e5 valid
FLOAT_LIT: [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?;

STRING_LIT: '"' (~["\\\r\n] | ESC)* '"';
fragment ESC: '\\' [ntr"\\];
// boolean lit and nil lit already defined as keywords

// char set and comments

WS: [ \t\r\f]+ -> skip; // skip spaces, tabs 
NL:
	'\n' {
    lst = [self.ID, self.RETURN, self.CONTINUE, self.BREAK, self.R_PAREN, self.R_CURLY, self.R_BRACKET, self.INT, self.FLOAT, self.BOOLEAN, self.STRING, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT, self.TRUE, self.FALSE, self.NIL];
    for t in lst:
        if self.lastTokenType == t: 
            self.type = self.SEMICOLON;
            self.lastTokenType = self.SEMICOLON;
            self.text = ";" 
            return super(MiniGoLexer,self).emit();
    self.skip();};

COMMENT: '//' ~[\r\n]* -> skip;
COMMENT_MULT: '/*' (COMMENT_MULT | .)*? '*/' -> skip;

ILLEGAL_ESCAPE: '"' (~["\\\r\n] | ESC)* '\\' ~[ntr"\\] {raise IllegalEscape(self.text)};
UNCLOSE_STRING:
	'"' (~["\\\r\n] | ESC)*? ('\r'? '\n' | EOF) {
        text = self.text;
        if text.endswith("\r\n"):
            text = text[:-2]  # Remove Windows newline
        elif text.endswith("\n"):
            text = text[:-1]  # Remove Unix newline
        raise UncloseString(text);};
ERROR_CHAR: . { raise ErrorToken(self.text)};