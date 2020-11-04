count = int(input())
result = 0
for i in range(0, count):
  [a,b,c] = input().split()
  sum = int(a)+int(b)+int(c)
  if(sum>=2):
    result+=1
print(result)