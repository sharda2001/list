question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal= ", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
fiftyfifty=[['four','seven'],['Delhi','Bhopal'],['Tourism','software engineering']]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solutions=[2,1,2]
solution_list = [3, 4, 1] 

print("Co-Powered by Dabur Amla presents,Kaun Banega Crorepati mein apka swagat hai!!")
print("Sadab,Aadab aur Shastriyakal.")
print("Pehla Question yeh rha apke screen ke upar:")
i= 0
c= 0
while i<len(question_list):
	print('your question is')
	print(i+1,question_list[i])
	
	a= 0
	while a<=len(options_list):
		print(a+1,options_list[i][a])
		a= a+1
	j= int(input('enter solution'))
	if j==solution_list[i]:
			print('congrats')
	elif j==5050:
		if c==0:
			m= 0
			while m<len(fiftyfifty[i]):
				print(m+1,fiftyfifty[i][m])
				m= m+1
			c= c+1
			num= int(input('enter no.'))
			if num==solutions[i]:
				print('correct')
			else:
				print('your option is wrong')
				print('quit')

		else:
			print('you used 5050 lifeline')
			num1= int(input('enter your option'))
			if num1==solution_list[i]:
				print('congrats,ap jeet gye 10000 rupaiye')
				break
			else:
				print('your option is wrong')
				break
	else:
				print('your answer is wrong')
				print('quit')
				break
	i= i+1
