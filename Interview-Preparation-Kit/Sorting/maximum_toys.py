# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sorted(prices)
    curr_sum = 0
    for idx, p in enumerate(prices, start=1):
            curr_sum += p
            if (curr_sum > k):
                return idx - 1
    return len(prices)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
