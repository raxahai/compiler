import re
import string

class lexer(object):

    def __init__(self,source_code):
        self.source_code = source_code

    def scan(self):
        words_list= []

        source_code = self.source_code #assign original txt file or source code

        # single-char seperators
        symbols = ['=','{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ','] 

        white_space = ' '
        lexeme = ''

        for i,char in enumerate(source_code):
            if char != white_space:
                lexeme += char # adding a char each time
            if (i+1 < len(source_code)): # prevents error
                # just to check if there are whitespaces or symbols so that it can seperate it
                if source_code[i+1] == white_space or source_code[i+1] in symbols or lexeme in symbols:
                    if lexeme != '':
                        words_list.append(lexeme)
                    lexeme = ''
        return words_list

    def tokenize(self):

        # keywords that will be used in my language
        keywrds = ['False','True','class','def','return','None','continue','break',
        'while','for','not','if','or','pass','and','else','elif','print']

        # Arithmetic Operators
        arit_opera = '+-*/'

        #logical operator
        log_op = ['>','<','<=','>=','==']

        #assignment operators
        assign = ['=']

        sepera = ['\n',',',':','(',')',"\'",'\"'] # seperator

        # where all token created by lexer will be stored
        tokens = []
        words = self.scan()
        # a loop that runs over the lexeme and then combine them as tokens
        for word in words:
            if re.match('[a-z]',word) or re.match('[A-Z]',word):
                if word in keywrds:
                    tokens.append(['Keyword',word])
                else:
                    tokens.append(['Identifier',word])
            
            elif word in arit_opera:
                tokens.append(['Arithmetic',word])

            elif word in assign:
                tokens.append(['Assignment_Operator',word])

            elif word in log_op:
                tokens.append(['Logical_Operator',word])

            elif word in sepera:
                tokens.append(['Seperator',word])

            elif re.match('[0-9]',word):
                tokens.append(['Integer',word])

        return tokens
