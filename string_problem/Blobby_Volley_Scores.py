t = int(input())

while t > 0:
    n = int(input())
    s = input()
    alice = 0
    bob = 0
    server = 'A'
    for i in range(n):
        if server == s[i]:
            if s[i] == 'A':
                alice += 1
            else:
                bob += 1
        else:
            server = s[i]
    print(alice,bob)
    # Your code goes here
    t -= 1
