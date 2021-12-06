from collections import deque

def part1(): # Thought I was really smart with this situation >:(
    f = list(map(int, open('day6.txt').read().split(',')))

    for i in range(80):
        for x in range(len(f)):  
            if f[x] == 0:
                f[x] = 7
                f.append(8)

            f[x] -= 1

    return(len(f))
    
print(part1())

def part2(): # Learned about deque which is like a looped array
    f = list(map(int, open('day6.txt').read().split(',')))

    q = deque([0] * 9)
    
    for x in f:
        q[x] += 1   
    
    for i in range(256):
        zero = q.popleft()
        q[6] += zero
        q.append(zero)

    return sum(q)

print(part2())
