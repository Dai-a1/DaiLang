from lex import *
from emit import *
from parse import *
import sys
import argparse
import subprocess
import os

def main(file=None, sandbox=False):
    print("Dai Compiler!")

    if file == None:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(file, 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter, sandbox)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")
    subprocess.call(["gcc", "out.c", "-o", "out"])
    # delete c file
    os.remove("out.c")

argparser = argparse.ArgumentParser(description="Dai Compiler")
argparser.add_argument("-f", "--file", help="Source file to compile.")
argparser.add_argument("-ls", "--list-tokens", help="List all tokens.", action="store_true")
# sandbox arg
argparser.add_argument("-s", "--sandbox", help="Run in sandbox mode.", action="store_true")
args = argparser.parse_args()

if args.file:
    if args.sandbox:
        main(args.file, sandbox=True)
    else:
        main(args.file)
elif args.list_tokens:
    import lex
    for i in lex.TokenType:
        # Strip the TokenType. from the string.
        print(str(i)[10:])
else:
    argparser.print_help()
