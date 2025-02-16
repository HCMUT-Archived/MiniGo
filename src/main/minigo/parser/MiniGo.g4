grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
    int lastTokenType = 0;

    def emit(self):
        tk = self.type
        if tk == self.NL: 
            lst = [self.ID, self.RETURN, self.CONTINUE, self.BREAK, self.R_PAREN, self.R_CURLY, self.R_BRACKET, self.INT, self.FLOAT, self.BOOLEAN, self.STRING, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT, self.TRUE, self.FALSE]
            if self.lastTokenType == self.ID: 
                self.type = self.SEMICOLON
                self.lastTokenType = self.SEMICOLON
                self.text = ";" 
                return super().emit()
            else: 
                return None
        elif tk == self.UNCLOSE_STRING:       
            result = super().emit();
            text = result.text
            if text.endswith("\r\n"):
                text = text[:-2]  # Remove Windows newline
            elif text.endswith("\n"):
                text = text[:-1]  # Remove Unix newline
            raise UncloseString(text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();
}

options{
	language = Python3;
}

// parser rules

program: declList EOF;

declList: decl SEMICOLON declList | decl;
decl: constDecl | varDecl | typeDecl | funcDecl | methodDecl;

constDecl: CONST ID INIT expression;
varDecl: VAR ID type? (INIT expression)?;
typeDecl: TYPE ID (structType | interfaceType);
funcDecl: FUNC ID L_CURLY paramsList R_CURLY type? blockStmt;
methodDecl:
	FUNC receiver ID L_CURLY paramsList R_CURLY type? blockStmt;
paramsList: paramPrime |;
paramPrime: param COMMA paramPrime | param;
param: identifierList type;
receiver: L_PAREN ID ID R_PAREN;

// array type
arrayType: L_BRACKET (INT_LIT | ID) R_BRACKET type;
type: primType | compType | arrayType | userDefType;

primType: STRING | INT | FLOAT | BOOLEAN;
compType: STRUCT | INTERFACE;
userDefType: ID;

// struct type not finished need to change to list of struct field
structType: STRUCT L_CURLY fieldList R_CURLY;
fieldList: field SEMICOLON fieldList | field;
field: ID type;

structInit: STRUCT L_CURLY fieldInitList R_CURLY;
fieldInitList: fieldInitPrime |;
fieldInitPrime: fieldInit COMMA fieldInitPrime | fieldInit;
fieldInit: ID COLON expression;

// interface type
interfaceType: INTERFACE L_CURLY methodList R_CURLY;
methodList: ID L_PAREN paramsList R_PAREN;

primaryExpr: literal | .;

// statements

statementList: statementPrime |;
statementPrime: statement SEMICOLON statementPrime | statement;
statement: (decl | assignStmt);
assignStmt:
	lhs assign_op = (
		ASSIGN
		| ADD_ASSIGN
		| SUB_ASSIGN
		| MUL_ASSIGN
		| DIV_ASSIGN
		| MOD_ASSIGN
	) expression;
lhs: ID | ID DOT ID | ID L_BRACKET expression R_BRACKET;

ifStmt:
	IF expression blockStmt (ELSE IF blockStmt) (ELSE blockStmt)?;

forStmt: FOR (expression | forClause | rangeClause) blockStmt;
forClause: . SEMICOLON expression SEMICOLON .;
rangeClause: .;

breakStmt: BREAK;
continueStmt: CONTINUE;
callStmt:;
functionCall: ID L_PAREN expressionList R_PAREN;
methodCall: ID DOT ID L_PAREN expressionList R_PAREN;

returnStmt: RETURN expression?;
blockStmt: L_CURLY statement* R_CURLY;

identifierList: ID COMMA identifierList | ID;

arrayLit: L_CURLY arrayLitElemList R_CURLY;
arrayLit_: L_CURLY arrayLitElemList R_CURLY;
// nullable, separated by comma
arrayLitElemList: arrayLitElemPrime |;
arrayLitElemPrime:
	arrayLitElem COMMA arrayLitElemPrime
	| arrayLitElem;

literal:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
	| NIL
	| arrayLit;

arrayLitElem:
	INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| TRUE
	| FALSE
	| NIL
	| arrayLit_;

// nullable separated by comma
expressionList: expressionPrime |;
expressionPrime: expression COMMA expressionPrime | expression;
expression:
	primaryExpr
	| expression L_BRACKET expression R_BRACKET // array access
	| expression DOT ID // struct field access
	| unary_op = (NOT | SUB) expression
	| expression mul_op = (MUL | DIV | MOD) expression
	| expression add_op = (ADD | SUB) expression
	| expression rel_op = (EQ | NEQ | LT | LE | GT | GE) expression
	| expression AND expression
	| expression OR expression;

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

STRING_LIT: '"' (~["\\] | ESC)* '"';
fragment ESC: '\\' [ntr"\\];
// boolean lit and nil lit already defined as keywords

// char set and comments

WS: [ \t\r\f]+ -> skip; // skip spaces, tabs 
NL: '\n'; //skip newlines

COMMENT: '//' ~[\r\n]* -> skip;
COMMENT_MULT: '/*' (COMMENT_MULT | .)*? '*/' -> skip;

ILLEGAL_ESCAPE: '"' (~["\\] | ESC)* ('\\' ~[ntr"\\]);
UNCLOSE_STRING: '"' (~["\\] | ESC)* ('\n' | EOF);
ERROR_CHAR: .;