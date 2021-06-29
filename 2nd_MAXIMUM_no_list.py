num=[10,20,30,40,50,60]
i=0
max=0
sec1=0
while i<len(num):
	if  num[i]>max:
		sec1=max
		max=num[i]
	if sec1<num[i] and num[i]<max:
		sec1=num[i]
	i=i+1
print(sec1)
