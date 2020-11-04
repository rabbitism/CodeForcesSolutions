count = int(input())
for i in range(0, count):
  word = input()
  if(len(word)<=10):
    print(word)
  else:
    length = len(word)-2
    print(word[0]+str(length)+word[length+1])
