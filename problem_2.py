# finding longest prefix from an array
arr = ['apple','apply','app','ape','apache','apemen']

def prefix(arr):
    # print(arr)
    prefix = ''
    for i in range(len(arr[0])):
        # print(arr[i])
        character = arr[0][i]
        for j in range(len(arr)):
            if arr[j][i] != character:
                return prefix

        prefix = prefix + character
    return prefix

print(prefix(arr))