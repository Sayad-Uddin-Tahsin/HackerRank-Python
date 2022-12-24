if __name__ == '__main__':
    scores = []
    data = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        data.append([name,score])
    
    s = sorted(list(set(scores)))[1]
    data.sort()
    for _ in data:
        if _[1] == s:
            print(_[0])
