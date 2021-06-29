a=['a','b']
b=[]
i=1
n=int(input('enter the number'))
while i<=n:
	j=0
	while j<len(a):
		b=b+[a[j]+str(i)]
		j=j+1
	i=i+1
print(b)