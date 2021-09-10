from sympy import summation, oo, Symbol, simplify
from sympy import factorial
from sympy import binomial as nC

n = Symbol("n", integer=True, nonnegative=True)
i = Symbol("i")
print(summation(nC(n,i), (i,0,n)))

n = Symbol("n", integer=True, positive=True)
i = Symbol("i")
print(simplify(summation(i*nC(n,i), (i,1,n))))

k = Symbol("k", integer=True, positive=True)
n = Symbol("n", integer=True, positive=True)
i = Symbol("i")
print(simplify(summation(nC(i,k), (i,0,n - 1))))

n = Symbol("n", integer=True, nonnegative=True)
i = Symbol("i")
print(summation(i*factorial(i), (i,0,n)))

m = Symbol("m", integer=True, nonnegative=True)
n = Symbol("n", integer=True, nonnegative=True)
i = Symbol("i")
print(simplify(summation(nC(m+i-1,i), (i,0,n))))

m = Symbol("m", integer=True, nonnegative=True)
n = Symbol("n", integer=True, nonnegative=True)
i = Symbol("i")
print(simplify(summation(m**i, (i,0,n))))

