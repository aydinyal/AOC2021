def part1():
    f = open('day5.txt').read().splitlines()
    valid = []
    board = []
    maxY = 0; maxX = 0
    for l in f: 
        l = l.split(' -> ')
        a = tuple((list(map(int, l[0].split(',')))))
        b = tuple((list(map(int, l[1].split(',')))))
        
        if a[0] == b[0] or a[1] == b[1]: 
            maxX = max(maxX, max(a[0], b[0]))
            maxY = max(maxY, max(a[1], b[1]))

            valid.append([a,b])

    for i in range(maxY+1):
        board.append([0] * (maxX+1))

    for line in valid:       
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1] 
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1): 
                board[y1][x] += 1
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                board[y][x1] += 1
    total = 0
    for b in board:
        for p in b:
            if p > 1: total += 1

    return total

print(part1())

def part2():
    f = open('day5.txt').read().splitlines()
    valid = []
    board = []
    maxY = 0; maxX = 0
    for l in f: 
        l = l.split(' -> ')
        a = tuple((list(map(int, l[0].split(',')))))
        b = tuple((list(map(int, l[1].split(',')))))
        
        if a[0] == b[0] or a[1] == b[1] or abs((a[1]-b[1])/(a[0]-b[0])) == 1:
            maxX = max(maxX, max(a[0], b[0]))
            maxY = max(maxY, max(a[1], b[1]))

            valid.append([a,b])

    for i in range(maxY+1):
        board.append([0] * (maxX+1))

    for line in valid:       
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]

        minp = line[0] if x1 < x2 else line[1]
        maxp = line[0] if x1 > x2 else line[1]
        
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1): 
                board[y1][x] += 1
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                board[y][x1] += 1
        elif abs((y2-y1)/(x2-x1)) == 1: 
            if minp[1] < maxp[1]:
                i = 0
                for x in range(minp[0], maxp[0]+1):
                    board[minp[1]+i][minp[0]+i] += 1
                    i += 1 
            else:
                i = 0
                for x in range(minp[0], maxp[0]+1):
                    board[minp[1]-i][minp[0]+i] += 1
                    i += 1  
             
    total = 0

    for b in board:
        for p in b:
            if p > 1: total += 1

    return total

print(part2())
