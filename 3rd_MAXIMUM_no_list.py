numbers=[42,50,40,23,70,56,12,5,10,7,24]
i=0
max=0
sec_max=0
third_max=0
while i<len(numbers):
	if numbers[i]>max:
		sec_max=max
		max=numbers[i]
	elif sec_max<numbers[i] and max>numbers[i]:
		third_max=sec_max
		sec_max=numbers[i]
	elif third_max<numbers[i]and sec_max>numbers[i]and max>numbers[i]:
		third_max=numbers[i]
	i=i+1
print(third_max)