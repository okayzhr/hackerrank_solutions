#https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())

    a = []
    b = ""
    for i in range(1, n + 1):
        a.append(i)

    b = ''.join(map(str, a))
    print(b)
