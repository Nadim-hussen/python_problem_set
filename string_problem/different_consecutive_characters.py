t = int(input())

while t>0:
    t -= 1
    n = int(input())
    s = input()
    if len(s) == n:
        result = 0
        for j in range(0,len(s)-1):
            if (s[j] == s[j+1]):
                result +=1
        print(result)