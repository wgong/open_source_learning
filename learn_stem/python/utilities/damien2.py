from sympy import *
x,y=symbols('x y')
y=1
for x in range(1,19):
    y=y*(I-x+1)/x
    print y.expand(complex=True)

