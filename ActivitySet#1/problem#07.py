text = "X-DSPAM-Confidence:    0.8475"
x = text.find(':')
y= text[x+4:]
a=float(y)
print(a)