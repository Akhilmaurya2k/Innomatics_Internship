def average(array):
    return format(sum(set(array))/len(set(array)), ".3f")

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
