elements=[23,14,56,12,19,9,15,31,42,43]
i=0
count_even=0
count_odd=0
sum_even=0
sum_odd=0
while i<len(elements):
	if elements[i]%2==0:
		count_even=count_even+1
		sum_even=sum_even+elements[i]
	else:
		count_odd=count_odd+1
		sum_odd=sum_odd+elements[i]
	i=i+1
even_average=sum_even/count_even
odd_average=sum_odd/count_odd
print(even_average,'average of even')
print(odd_average,'average of odd')