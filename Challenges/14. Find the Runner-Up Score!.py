if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    array = list(set(arr))
    array.remove(max(array))
    print(max(array))
