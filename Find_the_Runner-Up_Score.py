#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/submissions/code/415196918

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sayi = list(arr)

    sayilar = sorted(set(sayi))

    print(sayilar[-2])