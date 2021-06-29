list=[1,5,4,2,3]
i=0
while i<len(list):
	j=0
	while j<(len(list)-1):
		if list[j]>list[j+1]:
			list[j],list[j+1]=list[j+1],list[j]
		j+=1
	i+=1
print(list)
#print[1,2,3,4,5]