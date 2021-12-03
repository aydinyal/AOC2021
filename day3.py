def part1():
    f = open('day3.txt').read().splitlines()
    gamma = ''
    epsilon = ''
    for i in range(len(f[0])):
        zero = 0
        one = 0
        for j in range(len(f)):
            if f[j][i] == '0':
                zero += 1
            elif f[j][i] == '1':
                one += 1
        if zero > one:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1' 
            epsilon += '0'

    return int(gamma, 2) * int(epsilon, 2)

print(part1())

def part2():
    f = open('day3.txt').read().splitlines()

    o2 = f[:]
    co2 = f[:]

    for i in range(len(o2[0])):
        zero = 0; one = 0
        for j in range(len(o2)):
            if o2[j][i] == '0': zero += 1
            else: one += 1

        m = '0' if zero > one else '1'
 
        r = 0

        if len(o2) > 1:   
            for j in range(len(o2)-r):
                if o2[j-r][i] != m:
                    o2.remove(o2[j-r])
                    r += 1


    for i in range(len(co2[0])):
        zero = 0; one = 0
        for j in range(len(co2)):
            if co2[j][i] == '0': zero += 1
            else: one += 1

        m = '0' if zero <= one else '1'

        r = 0

        if len(co2) > 1: 
            for j in range(len(co2)-r):
                if co2[j-r][i] != m:
                    co2.remove(co2[j-r])
                    r += 1
 
    return int(o2[0], 2) * int(co2[0], 2)

print(part2())