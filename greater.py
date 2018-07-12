import sys
L=sys.stdin.read()
L=L.split()
L=[int(i) for i in L]
a=L[0]
b=L[1]
c=L[2]
if a>b and a>c:
	print(a)
elif b>c:
	print(b)
else:
	print(c)
