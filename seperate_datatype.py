list=['sharda','suman',1,2,2.6,5.7]
i=0
a=[]
b=[]
c=[]
while i<len(list):
	if type(list[i])==int:
		a.append(list[i])
	if type(list[i])==float:
		b.append(list[i])
	if type(list[i])==str:
		c.append(list[i])
	i=i+1
print(a)
print(b)
print(c)