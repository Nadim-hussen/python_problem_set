t = int(input())

while t > 0:
    t -= 1
    s = str(input())
    sum = 0
    for i in range(0,len(s)):

        if(s[i] =='a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
            sum +=1;
        else :
            if(sum <= 2):
                sum = 0



    if( sum > 2):
        print('Happy')
    else:
        print('Sad')
