# Enter your code here. Read input from STDIN. Print output to STDOUT

size = input().split()

height = int(size[0])
width = int(size[1])

verticle = int((height-1)/2)
horizontal = int((width-3)/2 )

rowsDone = 0

dotBetween = 1

while rowsDone < height:
    
    while rowsDone < verticle:
        print("-"*horizontal + ".|." * dotBetween + "-"*horizontal)
        horizontal -= 3
        dotBetween +=2
        rowsDone += 1
    print("-" * int((width -7)/2) + "WELCOME" + "-" * int((width-7)/2)  )
    rowsDone += 1
    horizontal += 3
    dotBetween -= 2
    while rowsDone < height:
        print("-"*horizontal + ".|." * dotBetween + "-"*horizontal)
        horizontal += 3
        dotBetween -=2
        rowsDone += 1


