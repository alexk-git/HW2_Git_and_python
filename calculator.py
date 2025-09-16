import re

def is_expression_valid(expression):
    '''
    Checking if expression is in required format:
    (number)(space)(operator)(space)(number)
    '''
    pattern = r'^\d+(?:\.\d+)?\s[+\-*/]\s\d+(?:\.\d+)?$'
    return bool(re.match(pattern, expression))

def simple_clean(text):
    '''
    Removing backspace symbod (\x08)
    useful if input was edited
    '''
    while '\x08' in text:
        pos = text.find('\x08')
        if pos > 0:
            text = text[:pos-1] + text[pos+1:]
        else:
            text = text[1:]
    return text

def division(a, b):
    '''
    Function returns the quotient of a divided by b.
    '''
    return(a/b)

def multiplication(a, b):
    '''
    Function returns the product of a multiplied by b
    '''
    return(a * b)

def addition(a, b):
    '''
    Function returns the sum of a and b.
    '''
    return(a + b)

def subtraction(a, b):
    '''
    Function returns the difference of a and b.
    ''' 
    return (a - b)

def main():
    operators = ["+", "-", "*", "/"]

    print('I can calculate one of four operations "+ - * /" on two numbers.')
    input_expr = input("Please, enter your expression as 'a <operator> b': ")
    input_expr = simple_clean(input_expr)

    if is_expression_valid(input_expr):
        expr_lst = input_expr.split(' ')

        if expr_lst[1] == '+': print(f"Result of {input_expr} = {addition(float(expr_lst[0]), float(expr_lst[2]))}")
        elif expr_lst[1] == '-': print(f"Result of {input_expr} = {addition(float(expr_lst[0]), float(expr_lst[2]))}")
        elif expr_lst[1] == '*': print(f"Result of {input_expr} = {multiplication(float(expr_lst[0]), float(expr_lst[2]))}")
        elif expr_lst[1] == '/': print(f"Result of {input_expr} = {division(float(expr_lst[0]), float(expr_lst[2]))}")
        else:
            print(f'I can calculate one of four operations "+ - * /" on two numbers, not {expr_lst[1]}.')
    else:
        print("Your expression is not passed validity check!")
        print("Please, enter your expression as 'a <operator> b' <- spaces are impotant!")
        print(f"But your expression is {input_expr}.")

    print(input_expr.split(' '))

if __name__ == "__main__":

    main()

