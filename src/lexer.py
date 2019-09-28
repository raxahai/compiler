import re
import collections

class lexer(object):

    def __init__(self,code):
        self.code = code
    
    def tokenize(self):
        code = self.code

        Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])

        keywords = {'False','True','class','def','return','None','continue','break',
            'while','for','not','if','or','pass','and','else','elif','print'}
        token_specification = [
            ('Float',   r'\d+\.\d*'),  # decimal number
            ('Integer', r'\d+'),    # Integer number
            ('Compound_assign_op', r'[+\-*/]='),    #compund assignment
            ('ASSIGN',   r'='),           # Assignment operator
            ('ID',       r'\w+'),    # Identifiers
            ('Arith_OP',       r'[+\-*/]'),      # Arithmetic operators
            ('Comparision_OP', r'[><=!]=?'),    #comparision operators
            ('Statement_end',  r'\n'),           # Line endings
            ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
            ('Seperator', r'[\.\(\)\{\}\[\],:]'), # seperator
            ('MISMATCH', r'.'),            # Any other character
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        line_num = 1
        line_start = 0
        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group()
            column = mo.start() - line_start
            if kind == 'Float':
                value = float(value)
            elif kind == 'Integer':
                value = int(value)
            elif kind == 'ID' and value in keywords:
                kind = value
            elif kind == 'Statement_end':
                line_start = mo.end()
                line_num += 1
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            yield Token(kind, value, line_num, column)