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

        m = ''
        if zero > one: m = '0'
        else: m = '1' 

        o2_temp = o2[:]

        if len(o2) > 1:   
            for j in range(len(o2_temp)):
                if o2_temp[j][i] != m: o2.remove(o2_temp[j]) 


    for i in range(len(co2[0])):
        zero = 0; one = 0
        for j in range(len(co2)):
            if co2[j][i] == '0': zero += 1
            else: one += 1

        m = ''
        if zero <= one: m = '0'
        else: m = '1' 

        co2_temp = co2[:]

        if len(co2) > 1: 
            for j in range(len(co2_temp)):
                if co2_temp[j][i] != m: co2.remove(co2_temp[j])
 
    return int(o2[0], 2) * int(co2[0], 2)

print(part2())