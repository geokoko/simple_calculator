operators = {'+': (1, 'left', lambda x, y: x + y), 
             '-': (1, 'left', lambda x, y: x - y),
             '*': (2, 'left', lambda x, y: x * y),
             '/': (2, 'left', lambda x, y: x / y),
             'u': (3, 'right', lambda x: -x)}

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def tokenize(expression):
    tokens = []
    current_token = ''
    #tokenize the expression
    for char in expression:
        if char.isdigit() or char == '.':
            current_token += char
        elif char in operators or char in ['(', ')']:
            if current_token:
                tokens.append(current_token)
            tokens.append(char)
            current_token = ''
    if current_token:
        tokens.append(current_token)
    
    for i, token in enumerate(tokens):
        if token == '-' and (i == 0 or (tokens[i - 1] in operators or tokens[i - 1] in ['(',')'])):
            tokens[i] = 'u'

    print(tokens)

    return tokens

def calc(expression):  
    def infix_to_postfix():
        tokens = tokenize(expression)
        postfix_list = []
        operator_stack = []
        for token in tokens:
            if is_float(token):
                postfix_list.append(token)
            elif token in operators:
                while operator_stack and operator_stack[-1] in operators and operators[token][0] <= operators[operator_stack[-1]][0]:
                    postfix_list.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    postfix_list.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            
        while operator_stack:
            postfix_list.append(operator_stack.pop())
            
        return (postfix_list)
        
    print(infix_to_postfix())
        
    return 1


calc("-7 * -(6 / 3)")
calc("3 -(-1)")
calc("2 + 3 + 8 * 16")
