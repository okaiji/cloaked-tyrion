import math

start = raw_input("start app?")
limit = int(raw_input("limit?")) - 1

a = int( raw_input("first multiple?") )
b = int( raw_input("second multiple?") )
c = a * b

n1 = limit / a
n2 = limit / b
n3 = limit / c

print n1
print n2
print n3

summation1 = a * ( n1 / 2 * ( n1 + 1) )
summation2 = b * ( n2 / 2 * ( n2 + 1) )
summation3 = c * ( n3 / 2 * ( n3 + 1) )

ans_to_eqn = summation1 + summation2 - summation3

print "The answer to the equation is: {answer}".format(answer=ans_to_eqn)
