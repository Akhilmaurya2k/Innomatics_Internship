if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr1 = []
    if n>=2 and n<=10:
        for i in arr:
            if arr[-1] != i:
                arr1.append(i)
        print(arr1[-1])
