'''
def primeSieve(n):
    p = [0 for i in range(n+1)]
    
    for i in range(2, n+1):
        if p[i] == 0:
            for j in range(i*i, n+1, i):
                p[i] = 1
    print(p)
                
def spf(n):
    spf = [i for i in range(n+1)]
    
    for i in range(2, n+1):
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i
    print(spf)


primeSieve(100)
spf(42)
'''


'''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def primeSieve(n):
    global p
    p = [0 for i in range(n)]
    
    
    for i in range(2, n+1):
        if p[i] == 0:
            for j in range(i*i, n+1, i):
                p[i] = 1
                
def spf(n):
    global spf
    spf = [i for i in range(n)]
    
    for i in range(2, n+1):
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i


def main():
    primeSieve(1000000000000)
    spf(1000000000000)
    n = int(input())
    nums = list(map(int, input().split(' ')))
    totalSum = 0 
    for num in nums:
        if p[num] == 0:
            totalSum += (num+1)
        else:
            totalSum += (num + (num//spf[num] + 1)
    print(totalSum)

    

main()

'''




import math
def main():
    n = int(input())
    nums = list(map(int, input().split(' ')))
    totalSum = 0
    for num in nums:
        flag = 0
        if num % 2 == 0:
            totalSum += (num+(num//2+1))
        continue
        for i in range(3, math.sqrt(num)+1):
            if num % i == 0:
                totalSum += (num+(num//i+1))
                flag = 1
                continue
        if flag == 0:
            totalSum += (num+1)
    print(totalSum)
