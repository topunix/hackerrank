# Complete the countSwaps function below.
def countSwaps(a):
    num_swaps = 0
    a_sorted = False
    while(a_sorted == False):
        a_sorted = True
        for i in range(len(a) - 1):
            j = i + 1
            if (a[i] > a[j]): 
                a[i], a[j] = a[j],a[i]
                num_swaps += 1
                a_sorted = False

    print(f'Array is sorted in {num_swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
