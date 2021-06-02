from lex import *


def main():
  with open('test.sk','r') as file:
    input = file.read()
  lexer = Lexer(input)
  
  token = lexer.getToken()
  while token.kind != TokenType.EOF:
    print(token.kind)
    token = lexer.getToken()

main()
