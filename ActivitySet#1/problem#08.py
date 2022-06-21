fname = input("Enter file name: ")
fh = open(fname)
count = 0 
total=0
y=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count +1
    x=float(line[21:])
    total=x+tot al
    y= total/count
print("Average spam confidence:",y)
