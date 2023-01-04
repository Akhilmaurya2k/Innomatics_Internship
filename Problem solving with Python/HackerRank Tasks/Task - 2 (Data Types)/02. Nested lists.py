if __name__ == '__main__':
    n = int(input())
    if n>=2 and n<=5:
        records = []
        scores = []
        for i in range(n):
            name = input()
            score = float(input())

            records.append([name,score])
            scores.append(score)
            records.sort(key = lambda x: x[1])
        a = sorted(list(set(scores)))[1]

        for i,j in sorted(records):
            if j == a:
                print(i)
