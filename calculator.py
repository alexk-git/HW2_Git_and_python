import re

def is_expression_valid(expression):
    pattern = r'^\d+(?:\.\d+)?\s[+\-*/]\s\d+(?:\.\d+)?$'
    return bool(re.match(pattern, expression))

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

def main():
    operators = ["+", "-", "*", "/"]

    print('I can calculate one of four operations "+ - * /" on two numbers.')
    input_expr = input("Please, enter your expression as 'a <operator> b': ")

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

