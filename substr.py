text = "X-DSPAM-Confidence:0.8475";
pos=text.find(':')
str=float(text[pos+1:100])
print(str)
