def part1():
    f = open('day1.txt').read().splitlines()
    ints = list(map(int, f)) 
    count = 0
    for i in range(1, len(ints)):
        if ints[i] > ints[i-1]:
            count+= 1
    return count

print(part1())

def part2():
    f = open('day1.txt').read().splitlines()
    ints = list(map(int, f))
    count = 0
    for i in range(3, len(ints)):
        if sum(ints[i-3:i]) < sum(ints[i-2:i+1]): count += 1  
    return count
    
print(part2())
