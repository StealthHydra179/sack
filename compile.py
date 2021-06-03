from lex import *
from emit import *
from parse import *
import sys

def main():
    print("Sack Compiler!")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter("out.py")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")
    #exec(open("out.py").read())

main()
