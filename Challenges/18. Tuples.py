# For some reason, in Python 3 it's not working fine, it was returning negative value. Use pypy 3 instead!

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
