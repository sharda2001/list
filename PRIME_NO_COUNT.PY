num=int(input("enter any number:"))
a=2
c=1
while a>0:
    b=2
    while b<a:
        if a%b==0:
            break
        b+=1
    else:
        print(a)
        if c==num:
            break
        c+=1
    a+=1