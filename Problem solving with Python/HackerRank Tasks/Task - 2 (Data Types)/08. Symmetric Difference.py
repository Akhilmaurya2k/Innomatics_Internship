M = int(input())
M = set(map(int, input().split()))
N = int(input())
N = set(map(int, input().split()))
a = M.symmetric_difference(N)
b = list(a)
b.sort()
for i in b:
    print(i)
