
from antlr4 import *
from antlr4.tree.Trees import Trees
import sys
import os
sys.path.append('./test/')

# Make sure that ANTLR_JAR is set to antlr-4.9.2-complete.jar
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET = '../target/main/minigo/parser' if os.name == 'posix' else os.path.normpath('../target/')

if not './main/minigo/parser/' in sys.path:
    sys.path.append('./main/minigo/parser/')

if os.path.isdir(TARGET) and not TARGET in sys.path:
    sys.path.append(TARGET)

try:
    from MiniGoLexer import MiniGoLexer
    from MiniGoParser import MiniGoParser
except ModuleNotFoundError as e:
    print(f"Error: {e}")
    print(f"Ensure that MiniGoLexer.py and MiniGoParser.py exist in {TARGET}")
    sys.exit(1)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_tree(node, parser, indent=0):
    """Recursively prints the parse tree with indentation."""
    rule_name = parser.ruleNames[node.getRuleIndex()] if node.getChildCount() > 0 else str(node)
    if node.getChildCount() != 0:
        print(bcolors.FAIL, end='')
    else:
        print(bcolors.WARNING, end='')
    print("  " * indent + rule_name + bcolors.ENDC)

    for i in range(node.getChildCount()):
        child = node.getChild(i)
        print_tree(child, parser, indent + 1)


def print_tree2(node, parser, child=0):
    rule_name = parser.ruleNames[node.getRuleIndex()] if node.getChildCount() > 0 else str(node)
    if node.getChildCount() != 0:
        print(bcolors.WARNING + child * ' ' + "(" + bcolors.ENDC + bcolors.FAIL + rule_name + bcolors.ENDC, end='')
    else:
        print(" " + bcolors.OKBLUE + rule_name + bcolors.ENDC, end='')

    for i in range(node.getChildCount()):
        child = node.getChild(i)
        print_tree2(child, parser, 1)

    if node.getChildCount() != 0:
        print(bcolors.WARNING + ")" + bcolors.ENDC, end='')


def print_tokens(lexer):
    """Prints all tokens with their types"""
    token = lexer.nextToken()
    while token.type != Token.EOF:
        print(f"Token: {token.text}, Type: {lexer.symbolicNames[token.type]}")
        token = lexer.nextToken()


def main():
    input_file = os.path.join(os.path.dirname(__file__), f"test/testcases/{sys.argv[1]}.txt")

    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found!")
        return

    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = MiniGoLexer(input_stream)

    print("Token Stream:")
    print_tokens(lexer)  # Debug tokens

    lexer.reset()  # Reset lexer to start parsing

    stream = CommonTokenStream(lexer)
    parser = MiniGoParser(stream)
    tree = parser.program()

    print_tree(tree, parser)

    # Print ANTLR's default tree representation
    print(bcolors.OKCYAN + "\nANTLR Default Parse Tree:" + bcolors.ENDC)
    print(bcolors.OKBLUE + Trees.toStringTree(tree, None, parser) + bcolors.ENDC)
    print_tree2(tree, parser)


if __name__ == '__main__':
    main()
