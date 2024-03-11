
# Online Python - IDE, Editor, Compiler, Interpreter
dictionary = {
    "00" : "A",
    "01" : "T",
    "10" : "C",
    "11" : "G",
}
t = int(input())
while t > 0:
    t -= 1
    # n,s=map(int,input().split())
    n = int(input())
    s = input()

    # Your code goes here
    result = ''

    for i in range(0,n,2):
        section = dictionary[f"{s[i]}{s[i+1]}"]
        result = f"{result}{section}"

    print(result)