if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        number = str(input())
        if number.isdigit():
            if len(number) == 10:
                if number[0] in ['7', '8', '9']:
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            print("NO")
