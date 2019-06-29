# This time we want to write calculations using functions and get the results. 
#   Let's have a look at some examples:
#       JavaScript:
#           seven(times(five())); // must return 35
#           four(plus(nine())); // must return 13
#           eight(minus(three())); // must return 5
#           six(dividedBy(two())); // must return 3
#       Ruby:
#           seven(times(five)) # must return 35
#           four(plus(nine)) # must return 13
#           eight(minus(three)) # must return 5
#           six(divided_by(two)) # must return 3
# Requirements:
#   There must be a function for each number from 0 ("zero") to 9 ("nine")
#   There must be a function for each of the following mathematical 
#       operations: plus, minus, times, dividedBy (divided_by in Ruby)
#   Each calculation consist of exactly one operation and two numbers
#   The most outer function represents the left operand, the most inner 
#       function represents the right operand
#   Divison should be integer division, e.g eight(dividedBy(three()))/
#       eight(divided_by(three)) should return 2, not 2.666666...

def parse(s=0):
    s += s.replace('times', '*')
    s += s.replace('minus', '-')
    s += s.replace('plus', '+')
    s += s.replace('divided_by', '/')
    s += s.replace('one', '1')
    s += s.replace('two', '2')
    s += s.replace('three', '3')
    s += s.replace('four', '4')
    s += s.replace('five', '5')
    s += s.replace('six', '6')
    s += s.replace('seven', '7')
    s += s.replace('eight', '8')
    s += s.replace('nine', '9')
    s += s.replace('(', '')
    s += s.replace(')', '')
    return eval(s)


def one(s=0):
    return parse(s)


def two(s=0):
    return parse(s)


def three(s=0):
    return parse(s)


def four(s=0):
    return parse(s)


def five(s=0):
    return parse(s)


def six(s=0):
    return parse(s)


def seven(s=0):
    return parse(s)


def eight(s=0):
    return parse(s)


def nine(s=0):
    return parse(s)


def plus(s=0):
    return parse(s)


def minus(s=0):
    return parse(s)


def times(s=0):
    return parse(s)


def dividedBy(s=0):
    return parse(s)


print(seven(times(five()))) # must return 35
print(four(plus(nine()))) # must return 13
print(eight(minus(three()))) # must return 5
print(six(dividedBy(two()))) # must return 3
