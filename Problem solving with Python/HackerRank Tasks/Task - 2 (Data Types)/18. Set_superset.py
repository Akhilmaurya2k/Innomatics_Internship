a = set(input().split())
counter = 0
n = int(input())
for i in range (n):
        b = set(input().split())
        if a.issuperset(b) :
                counter += 1
print(counter == n)
