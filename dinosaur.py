def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0
    
def infix_to_postfix(exprssn):
    stack = []
    postfix = ''
    
    for var in exprssn:
        if var.isalnum():
            postfix += var
            
        elif var == '(':
            stack.append(var)
            
        elif var == ')':
            while stack and stack[-1]!= '(':
                postfix = stack.pop()
            stack.pop()
        
        else:
            while stack and precedence(stack[-1]) >= precedence(var):
                postfix += stack.pop()
            stack.append(var)
                 
    while stack:
        postfix += stack.pop()
    return postfix   

exprssn = input("enter your value ")
exprssn = exprssn.replace(" ","")
result = infix_to_postfix(exprssn)
print(result)     
        