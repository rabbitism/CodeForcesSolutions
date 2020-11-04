[n, k] = input().split()
n = int(n)
k = int(k)
result = 0
lyst = input().split()
critera = int(lyst[k-1])
for i in range(0, n):
  if(int(lyst[i])<=0):
    break
  elif(int(lyst[i])>=critera):
    result+=1
  else:
    break 
print(result)
