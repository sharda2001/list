sentence = 'My name is sharda'
list = []
a = ''
i=0
while i<len(sentence):
    if sentence[i]== ' ':
        list.append(a)
        a = ''
    else:
        a=a+sentence[i] 
    i+=1
if a:
    list.append(a)
    print(list)