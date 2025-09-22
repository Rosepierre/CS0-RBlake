#Kattis problem to get r2 from only r1 and s
#Roger Blake

def mean(r1,s):
    multiply = s * 2 
    r2 = multiply - r1
    return r2
r1, s = map(int, input().split())
print(mean(r1,s))