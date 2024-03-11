t = int(input())

while t > 0:
    t -= 1
    st = input()
    a = st.split(' ')
    for i in range(0,len(a)):
        if (a[i] == "fOx"):
            a[i] = "fox"
        if(len(a[i])>1):
            a[i] = a[i][0].upper() + a[i][1:]
        else:
            a[i] = a[i].upper()
    result = " ".join(a)
    print(result)