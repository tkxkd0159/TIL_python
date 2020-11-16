import sys

# The list of command line arguments passed to a Python script.
print("Convert 'Tap' to 'space' ", sys.argv[0])

src = sys.argv[1]
dst = sys.argv[2]

with open(src,'r') as f:
    temp = f.read()


res = temp.replace("\t"," ")

with open(dst, 'w') as f:
    f.write(res)


