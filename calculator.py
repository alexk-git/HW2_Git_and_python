
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
    print('I can calculate one of four operations "+ - * /" on two numbers.')
    input_expr = input("Please, enter your expression as 'a <operator> b':")
    expr_lst = input_expr.split(' ')
    print(expr_lst)

if __name__ == "__main__":

    main()

