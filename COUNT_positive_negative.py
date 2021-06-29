numbers=[35,-40,-201,0,66,-78,33,0,13,18]
i=0
count_positive=0
count_negitive=0
count_zero=0
while i<len(numbers):
	if numbers[i]>0:
		count_positive=count_positive+1
	elif numbers[i]<0:
		count_negitive=count_negitive+1
	else:
		count_zero=count_zero+1
	i=i+1
print(count_positive,'positive')
print(count_negitive,'negitive')
print(count_zero,'zero')