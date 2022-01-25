from infix_to_postfix import infix_to_postfix
from postfix_eval import postfix_eval

if __name__ == '__main__':
    print(postfix_eval(infix_to_postfix("( 5 - 6 ) * 4 - ( 5 - 2 * 2 )")))
    print(postfix_eval(infix_to_postfix("( 7 + 8 ) / ( 3 + 2 )")))
