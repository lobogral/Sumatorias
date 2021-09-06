from sympy import summation, oo, Symbol, simplify
from sympy import factorial
from sympy import binomial as C

n = Symbol("n", integer=True, nonnegative=True)
i = Symbol("i")
print(summation(C(n,i), (i,0,n)))

n = Symbol("n", integer=True, positive=True)
i = Symbol("i")
print(simplify(summation(i*C(n,i), (i,1,n))))

k = Symbol("k", integer=True, positive=True)
n = Symbol("n", integer=True, positive=True)
i = Symbol("i")
print(simplify(summation(C(i,k), (i,0,n - 1))))

n = Symbol("n", integer=True, nonnegative=True)
i = Symbol("i")
print(summation(i*factorial(i), (i,0,n)))

m = Symbol("m", integer=True, nonnegative=True)
n = Symbol("n", integer=True, nonnegative=True)
i = Symbol("i")
print(simplify(summation(C(m+i-1,i), (i,0,n))))

