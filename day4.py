from copy import deepcopy

def part1():
    f = open('day4.txt').read().splitlines()

    nums = f[0].split(',') 
    
    f.append('')
 
    boards = []
    board = []

    # read boards
    for i in range(2, len(f)):
        if f[i] == '':
            boards.append(board)
            board = []
        else:
            board.append(f[i].split()) 
     
    for num in nums:
        for j in range(len(boards)):
            for k in range(len(boards[j])):
                for l in range(len(boards[j][k])):
                    if boards[j][k][l] == num:
                        boards[j][k][l] = '*'
                        check1 = True
                        check2 = True

                        for i in range(len(boards[j][k])):
                            if boards[j][k][i] != '*': check1 = False
                        for i in range(len(boards[j])):
                            if boards[j][i][l] != '*': check2 = False

                        
                        if check1 or check2:
                            sum = 0 
                            for i in range(len(boards[j])):
                                for h in range(len(boards[j][i])):
                                    if boards[j][i][h] != '*':
                                        sum += int(boards[j][i][h])
                            return sum * int(num)
           
print(part1())

def part2():
    f = open('day4.txt').read().splitlines()

    nums = f[0].split(',') 
    
    f.append('')
 
    boards = []
    board = []

    # read boards
    for i in range(2, len(f)):
        if f[i] == '':
            boards.append(board)
            board = []
        else:
            board.append(f[i].split()) 
    win = 0
    winners = []
    for num in nums:
        for j in range(len(boards)):
            for k in range(len(boards[j])):
                for l in range(len(boards[j][k])):
                    if boards[j][k][l] == num:
                        boards[j][k][l] = '*'
                        check1 = True
                        check2 = True

                        for i in range(len(boards[j][k])):
                            if boards[j][k][i] != '*': check1 = False
                        for i in range(len(boards[j])):
                            if boards[j][i][l] != '*': check2 = False

                        if (check1 or check2) and j not in winners:
                            win += 1
                            winners.append(j)

                        if (check1 or check2) and win == len(boards):
                            sum = 0 
                            for i in range(len(boards[j])):
                                for h in range(len(boards[j][i])):
                                    if boards[j][i][h] != '*':
                                        sum += int(boards[j][i][h])
                            return sum * int(num)

print(part2())
