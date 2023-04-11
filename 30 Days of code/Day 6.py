# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(0,T):
    S = input().strip()
    
    index = 0
    stringLenght = len(S) - 1
    newString = ""
    
    while index <= stringLenght:
        newString += S[index]
        index += 2
        
    newString += " "
    index = 1
    while index <= stringLenght:
        newString += S[index]
        index += 2
    
    print(newString)