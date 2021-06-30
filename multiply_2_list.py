list1 = [1, 2, 3]
list2 = [4, 5, 6]
products = []
for num1, num2 in zip(list1, list2):
	products.append(num1 * num2)
print(products)