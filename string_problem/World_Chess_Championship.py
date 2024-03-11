# cook your dish here
t = int(input())

while t>0:
    t-=1
    x = int(input())
    s = str(input())
    c=0
    d=0
    n=0
    for i in range(0,len(s)):
        if(s[i] == "C"):
            c+=1
        elif(s[i] == "D"):
            d+=1
        else:
            n+=1

    c = 2*c + d
    n = 2*n + d
    if(c>n):
        print(60*x)
    elif(n>c):
        print(40*x)
    else:
        print(55*x)

