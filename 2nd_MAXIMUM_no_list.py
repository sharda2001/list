num=[10,20,30,40,50,60]
i=0
max=0
sec=0
while i<len(num):
	if  num[i]>max:
		sec=max
		max=num[i]
	if sec<num[i] and num[i]<max:
		sec=num[i]
	i=i+1
print(sec)