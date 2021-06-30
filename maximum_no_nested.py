num=[[2,3,4],[5,7,6],[8,9,11]]
i=0
b=[]
while i<len(num):
	j=0
	c=0
	while j<len(num[i]):
		if (num[i][j]>c):
			c=num[i][j]
		j=j+1
	b.append(c)	
	i=i+1
print(b)