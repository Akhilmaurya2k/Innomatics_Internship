n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    a = list(input().split())
    if a[0] == 'remove':
        s.remove(int(a[-1]))
    if a[0] == 'discard':
        s.discard(int(a[-1]))
    if a[0] == 'pop':
        s.pop()
print(sum(s))
