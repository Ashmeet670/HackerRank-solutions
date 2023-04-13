# Enter your code here. Read input from STDIN. Print output to STDOUT

entries = int(input())
phoneBook = {}

for i in range(0,entries):
    entry = input().strip().split()
    phoneBook[entry[0]] = entry[1]
    
queries = []

while True:
    try:
        queries.append(input())
    except EOFError:
        break
    
        
for i in queries:
    if i in phoneBook:
        print(f"{i}={phoneBook[i]}")
    else:
        print("Not found")
    
    