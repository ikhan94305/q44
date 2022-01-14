def solution(k, a, b):
    a.sort()
    b.sort()
    for i in range(k):
        if a[i] >= b[-1-i]:
            break
        a[i] = b[-1-i]
    return sum(a)

k = 3
a = [100,100,20,50,60]
b = [1,1,1,1,1]
answer = solution(k, a, b)
print(answer)
