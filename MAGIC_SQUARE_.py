a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(a):
    j=0
    r_sum=0
    c_sum=0
    while j<len(a[i]):
        c_sum=c_sum+a[i][j]
        r_sum=r_sum+a[j][i]
        j= j + 1
    i = i + 1
c=0
d=0
f=len(a)-1
d1=0
d2=0
while c<len(a):
    d1=d1 + a[c][d]
    d2=d2+a[c][f]
    c=c+1
    d=d+1
    f=f-1
if d1==d2==r_sum==c_sum:
    print("magic squre")
else:
       print("not magic square")
