t = int(input())
for _ in range(t):
    n = input()
    carry = True
    n_list = list(n)

    for i in range(len(n) - 1, -1, -1):
        if carry:
            if n_list[i] == '9':
                n_list[i] = '0'
            else:
                n_list[i] = str(int(n_list[i]) + 1)
                carry = False

    if carry:
        n_list.insert(0, '1')


    n = ''.join(n_list)
    print(n)