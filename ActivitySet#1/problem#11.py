name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
z=None
for line in handle:
    if not line.startswith("From"):
        continue
    words=line.split()
    x=(words[5])
    y=x[0:2]
    for word in y:
        counts[y]=counts.get[y,0]+1
           
lst=list()
for k,v in counts.items():
    lst.append((k,v))
lst.sort()
for k,v in lst:
    print(k,v)