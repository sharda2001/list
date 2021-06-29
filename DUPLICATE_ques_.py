a=[1,2,3,4,5,2,1]
i=0
b=[]
while i<len(a):
	if a[i]not in b:
		b.append(a[i])
	i=i+1
print(b)

# a=[1,2,3,4,5,2,1]
# i=0
# while i<len(a):
# 	if a[i]!=2 or a[i]!=5:
# 		i=i+1
# 	print(a[i],end=" ")
