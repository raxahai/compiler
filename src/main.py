import lexer

def main():

    # read the source code first
    content = ""
    with open('C:/Users/Raza Haider/Desktop/Slither/src/test.lang','r') as file:
        content = file.read()

    # lexer
    lex = lexer.lexer(content)
    token = lex.tokenize()
    for tk in token:
        print(tk)

main()