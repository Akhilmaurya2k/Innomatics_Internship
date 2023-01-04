a = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    b = list(input().split())
    b1 = set(map(int, input().split()))
    if b[0] == 'intersection_update':
        A.intersection_update(b1)
    if b[0] == 'difference_update':
        A.difference_update(b1)
    if b[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(b1)
    if b[0] == 'update':
        A.update(b1)
print(sum(A))
