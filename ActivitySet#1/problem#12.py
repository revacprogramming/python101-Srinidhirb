 import re 
file = input('enter the file name')
fhand=open(file)
number = list()
for line in fhand:
  x =  line.rstrip()
  y= re.findall('[0-9]+',x)
  for a in y :
    a=int(y)
    number.append(a)
print(sum(number))