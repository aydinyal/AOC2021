def part1():
    f = open('day2.txt').read().splitlines()
    h = 0; d = 0
    for line in f:
        line = line.split()
        word = line[0]
        amt = int(line[1])

        if word == 'forward': h += amt
        elif word == 'down': d += amt
        elif word == 'up': d -= amt
    return h * d

print(part1())

def part2():
    f = open('day2.txt').read().splitlines()
    a = 0; d = 0; h = 0
    for line in f:
        line = line.split()
        word = line[0]
        amt = int(line[1])

        if word == 'forward':
            h += amt
            d += (amt * a)
        elif word == 'down': a += amt
        elif word == 'up': a -= amt
    return h * d 
   
print(part2())
