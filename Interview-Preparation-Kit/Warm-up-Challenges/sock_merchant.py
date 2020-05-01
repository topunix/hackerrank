from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    return sum(v // 2 for v in Counter(ar).values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
