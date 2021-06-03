from lex import *
from emit import *
from parse import *
import sys

def main():
    print("Sack Compiler!")

    if len(sys.argv) < 2:
        sys.exit("Error: Compiler needs source file as argument.")
    if len(sys.argv) > 2:
        sys.exit("Error: Compiler only takes 1 source file as a parameter.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed. Ouptuted file: out.c")
    #exec(open("out.py").read())

if __name__ == '__main__':
    main()
