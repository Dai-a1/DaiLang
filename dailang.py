from lex import *
from emit import *
from parse import *
import sys
import argparse
import subprocess

def main(file=None):
    print("Dai Compiler!")

    if file == None:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(file, 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")
    subprocess.call(["gcc", "out.c", "-o", "out"])

argparser = argparse.ArgumentParser(description="Dai Compiler")
argparser.add_argument("file", help="Source file to compile.")
args = argparser.parse_args()

if args.file:
    main(args.file)
