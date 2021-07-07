e= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
b=[]
while i<len(e):
	j=0
	a=[]
	c=0
	while j<len(e):
		if e[i]==e[j]:
			c=c+1
		j=j+1
	a.append(c)
	a.append(e[i])
	if a not in b:
			b.append(a)
	i=i+1
print(b)