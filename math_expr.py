def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def calc(expression):
    operators = {'+': (1, lambda x, y: x + y), 
                 '-': (1, lambda x, y: x - y),
                 '*': (2, lambda x, y: x * y),
                 '/': (2, lambda x, y: x / y)}
    
    def infix_to_postfix():
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
            
        postfix_list = []
        operator_stack = []
        print(tokens)

        for token in tokens:
            if is_float(token):
                postfix_list.append(token)
            elif token in operators:
                while operator_stack and operators[token][0] <= operators[operator_stack[-1]][0]:
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
            
            
        return ''.join(postfix_list)
        
    print(infix_to_postfix())
        
    return 1


calc("-7 * -(6 / 3)")
calc("3 -(-1)")