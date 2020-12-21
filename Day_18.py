import re, operator
from stack import Stack
from string import digits

filename = 'aoc-18.txt'
operators = '** * / // + -'.split()

def math(op,d1,d2):
    ops = {'**':operator.pow(d1, d2), '*':operator.mul(d1, d2), '/':operator.truediv(d1, d2),
        '//':operator.floordiv(d1, d2), '+':operator.add(d1, d2), '-':operator.sub(d1, d2)}
    return ops.get(op)


def load(infile):
    lines = []
    with open(infile) as f:
        reader = f.readlines()
        return [line.replace('(', '( ').replace(')', ' )').replace('\n','') for line in reader]
        

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 3
    prec["-"] = 3
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def convert_expression(data):
    return [infixToPostfix(line) for line in data]


def calculate_expression(data):
    s = Stack()
    total = 0

    for item in data:
        for token in item:
            if token in digits:
                s.push(int(token))
            else:
                if token != ' ':
                    op1 = s.pop()
                    op2 = s.pop()
                    if token == '*':
                        result = op1 * op2
                    if token == '+':
                        result = op1 + op2
                    s.push(result)
        total += s.pop()
    return total


info = load(filename)
postfix_expression = convert_expression(info)
answers = calculate_expression(postfix_expression)
print(answers)
