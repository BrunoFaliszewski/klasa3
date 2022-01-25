from stack import Stack


def postfix_eval(postfix_expr):  # "2 3 +"
    operand_stack = Stack()

    for token in postfix_expr.split():
        if token in '+-*/':
            b = operand_stack.pop()
            a = operand_stack.pop()
            result = do_math(token, a, b)
            operand_stack.push(result)
        else:
            operand_stack.push(int(token))

    return operand_stack.pop()


def do_math(op, a, b):
    if op == "*":
        return a * b
    elif op == "/":
        return a // b
    elif op == "+":
        return a + b
    else:
        return a - b


if __name__ == '__main__':
    print(postfix_eval("5 6 - 4 * 5 2 2 * - -"))
