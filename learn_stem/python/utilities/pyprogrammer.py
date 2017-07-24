# Evolution of a Python programmer.py

#Newbie programmer
def factorial_newbie(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
print factorial_newbie(6)
 
 
#First year programmer, studied Pascal
def factorial_pascal(x):
    result = 1
    i = 2
    while i <= x:
        result = result * i
        i = i + 1
    return result
print factorial_pascal(6)
 
 
#First year programmer, studied C
def factorial_c(x): 
    result = i = 1;
    while (i <= x): 
        result *= i;
        i += 1;
    return result;
print(factorial_c(6))
 
 
#First year programmer, SICP
@tailcall
def factorial_sicp(x, acc=1):
    if (x > 1): 
		return x*factorial_sicp(x - 1)
    else:       
		return acc
print(factorial_sicp(6))
 
 
#First year programmer, Python
def factorial(x):
    res = 1
    for i in xrange(2, x + 1):
        res *= i
    return res
print factorial(6)
 
 
#Lazy Python programmer
def factorial_lazy(x):
    return x > 1 and x * fact(x - 1) or 1
print factorial_lazy(6)
 
 
#Lazier Python programmer
f = lambda x: x and x * f(x - 1) or 1
print f(6)
 
 
#Python expert programmer
# does not work using Canopy
import operator as op
import functional as f
fact = lambda x: f.foldl(op.mul, 1, xrange(2, x + 1))
print fact(6)
 
 
#Python hacker
import sys
#@tailcall
def fact(x, acc=1):
    if x: return fact(x.__sub__(1), acc.__mul__(x))
    return acc
sys.stdout.write(str(fact(6)) + '\n')
 
 
#EXPERT PROGRAMMER
import c_math   # ImportError: No module named c_math
fact = c_math.fact
print fact(6)
 
 
#ENGLISH EXPERT PROGRAMMER
import c_maths
fact = c_maths.fact
print fact(6)
 
 
#Web designer
def factorial(x):
    #-------------------------------------------------
    #--- Code snippet from The Math Vault          ---
    #--- Calculate factorial (C) Arthur Smith 1999 ---
    #-------------------------------------------------
    result = str(1)
    i = 1 #Thanks Adam
    while i <= x:
        #result = result * i  #It's faster to use *=
        #result = str(result * result + i)
           #result = int(result *= i) #??????
        result str(int(result) * i)
        #result = int(str(result) * i)
        i = i + 1
    return result
print factorial(6)
 
 
#Unix programmer
# incomplete
import os
def fact(x):
    os.system('factorial ' + str(x))
fact(6)
 
 
#Windows programmer
NULL = None
def CalculateAndPrintFactorialEx(dwNumber,
                                 hOutputDevice,
                                 lpLparam,
                                 lpWparam,
                                 lpsscSecurity,
                                 *dwReserved):
    if lpsscSecurity != NULL:
        return NULL #Not implemented
    dwResult = dwCounter = 1
    while dwCounter <= dwNumber:
        dwResult *= dwCounter
        dwCounter += 1
    hOutputDevice.write(str(dwResult))
    hOutputDevice.write('\n')
    return 1
import sys
CalculateAndPrintFactorialEx(6, sys.stdout, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
 
 
#Enterprise programmer
def new(cls, *args, **kwargs):
    return cls(*args, **kwargs)
 
class Number(object):
    pass
 
class IntegralNumber(int, Number):
    def toInt(self):
        return new (int, self)
 
class InternalBase(object):
    def __init__(self, base):
        self.base = base.toInt()
 
    def getBase(self):
        return new (IntegralNumber, self.base)
 
class MathematicsSystem(object):
    def __init__(self, ibase):
        Abstract
 
    @classmethod
    def getInstance(cls, ibase):
        try:
            cls.__instance
        except AttributeError:
            cls.__instance = new (cls, ibase)
        return cls.__instance
 
class StandardMathematicsSystem(MathematicsSystem):
    def __init__(self, ibase):
        if ibase.getBase() != new (IntegralNumber, 2):
            raise NotImplementedError
        self.base = ibase.getBase()
 
    def calculateFactorial(self, target):
        result = new (IntegralNumber, 1)
        i = new (IntegralNumber, 2)
        while i <= target:
            result = result * i
            i = i + new (IntegralNumber, 1)
        return result
 
print StandardMathematicsSystem.getInstance(new (InternalBase, new (IntegralNumber, 2))).calculateFactorial(new (IntegralNumber, 6))
