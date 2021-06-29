elements=[23,14,56,12,19,9,15,31,42,43]
i=0
count_even=0
count_odd=0
while i<len(elements):
	if elements[i]%2==0:
		count_even=count_even+1
	else:
		count_odd=count_odd+1
	i=i+1
print(count_even,'even no')
print(count_odd,'odd no')