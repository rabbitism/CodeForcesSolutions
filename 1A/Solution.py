import math
numbers = input()
[n, m, a] = numbers.split()
n = int(n)
m = int(m)
a = int(a)
x = math.ceil(n/a)
y = math.ceil(m/a)
print(x*y)