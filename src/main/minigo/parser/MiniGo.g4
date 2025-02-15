grammar MiniGo;

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

// parser rules

program: decl+ EOF;

decl: .;

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

// identifier

ID: [a-zA-Z_][a-zA-Z0-9_]*;

// separators

L_PAREN: '(';
R_PAREN: ')';
L_CURLY: '{';
R_CURLY: '}';
L_BRACKET: '[';
R_BRACKET: ']';
COMMA: ',';
SEMICOLON: ';';

// operators 13

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

DECL_ASSIGN: ':=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';

ASSIGN: '=';
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
DECIMAL_LIT: ('0' | [1-9][0-9]*);
BIN_LIT: '0' [bB] [01]+;
OCTAL_LIT: '0' [oO] [0-7]+;
HEX_LIT: '0' [xX] [0-9a-fA-F]+;

// is 0.e5 valid
FLOAT_LIT: [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?;

STRING_LIT: '"' (~["\\] | ESC) '"';
fragment ESC: '\\' [ntr"\\];
// boolean lit and nil lit already defined as keywords

// char set and comments

WS: [ \t\r\f]+ -> skip; // skip spaces, tabs 
NL: '\n' -> skip; //skip newlines

COMMENT: '//' ~[\r\n]* -> skip;
COMMENT_MULT: '/*' (COMMENT_MULT | .)*? '*/' -> skip;

ILLEGAL_ESCAPE: .;
UNCLOSE_STRING: .;
ERROR_CHAR: .;