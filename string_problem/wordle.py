# cook your dish here
k = int(input())

while k > 0:
    k-=1
    i = 0
    S = input()
    T = input()
    result =""
    for i in range(0,5):
        if(S[i] == T[i]):
            result += 'G'
        else:
            result += 'B'

    print(result)