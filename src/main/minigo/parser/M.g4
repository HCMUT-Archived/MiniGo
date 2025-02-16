grammar M;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
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

program: decl+ EOF;

decl: .;

// decl: funcdecl | vardecl;

// vardecl: 'var' ID 'int' ';';

// funcdecl: 'func' ID '(' ')' '{' '}' ';';

// 3.1 characters set

WS: [ \t\r]+ -> skip; // skip spaces, tabs 
NL: '\n' -> skip; //skip newlines
FF: '\f'; // form feed
CR: '\r'; // carriage return 

// 3.2 program comment unfinished

COMMENT: '//' ~[\r\n]*? -> skip;
MULTIL_COMMENT: '/*' ~[\r\n]*? '*/' -> skip;

// 3.3 tokens set

// 3.3.2 keywords

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

// 3.3.1 identifiers identifier must not clash with keywords

ID: [a-zA-Z_][a-zA-Z0-9_]*;

// 3.3.3 operators

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQ: '==';
NEQ: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';

AND: '&&';
OR: '||';
NOT: '!';

DECL_ASSIGN: ':=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';

ASSIGN: '='; // =
DOT: '.'; // .

// 3.3.4 separators

L_PAREN: '(';
R_PAREN: ')';
L_CURLY: '{';
R_CURLY: '}';
L_BRACKET: '[';
R_BRACKET: ']';
COMMA: ',';
SEMICOLON: ';';

// 3.3.5 literals

INT_LIT: DECIMAL_LIT | BIN_LIT | OCTAL_LIT | HEX_LIT;
fragment DECIMAL_LIT: ('0' | [1-9][0-9]*);
fragment BIN_LIT: ('0b' | '0B') [01]+;
fragment OCTAL_LIT: ('0o' | '0O') [0-7]+;
fragment HEX_LIT: ('0x' | '0X') [0-9a-fA-F]+;

FLOAT_LIT: [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?;

// https://stackoverflow.com/questions/66902057/antlr-how-to-accept-double-quotes-inside-double-quoted-string-while-parsing

STRING_LIT: '"' '"';

fragment ESC: .;
fragment CHAR: .;

BOOL_LIT: .;

// 4 type and values (4.1 - 4.4)

booleanExp:
	BOOL_LIT
	| NOT booleanExp
	| booleanExp AND booleanExp
	| booleanExp OR booleanExp;

intExp:
	INT_LIT
	| intExp ADD intExp
	| intExp SUB intExp
	| intExp MUL intExp
	| intExp DIV intExp
	| intExp MOD intExp; // missing == != > >= < <=

floatExp:
	FLOAT_LIT
	| floatExp ADD floatExp
	| floatExp SUB floatExp
	| floatExp MUL floatExp
	| floatExp DIV floatExp; // missing == != > >= < <=

stringExp:
	STRING_LIT
	| stringExp ADD stringExp; // missing == != > >= < <=

// 4.5 array type

arrayDecl:
	VAR ID L_BRACKET INT_LIT R_BRACKET; // not finished (need multi-dimension and type)
arrayDimension: .;

// 4.6 struct type 

structDecl: TYPE ID STRUCT L_CURLY structField* R_CURLY;

structField: .;

// 4.7 interface type

// 5.1 var

varDecl: .;

// 5.2 const

// 5.3 func and method

// 6. expression

// 6.1 arith opt

// 6.2 relational opt

// 6.3 bool opt

// 6.4 accessing array elem

// 6.5 accessing struct field

// 6.6 literal

// 6.7 func and method call

// 6.8 op precedence and associativity 

// 7 statements

// 7.1 var and const assignment

// 7.2 assignment statement

// 7.3 if statement

// 7.4 for statement 

// 7.5 break statement

// 7.6 continue statement 

// 7.7 return statement

// 8 scope

// things 
typeSpecifiers: .;

ERROR_CHAR: .;
ILLEGAL_ESCAPE: .;
UNCLOSE_STRING: .;