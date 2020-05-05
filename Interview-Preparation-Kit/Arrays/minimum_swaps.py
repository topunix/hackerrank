import os

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # Find the index and find if it's in the right place
    min_swap = 0
    been_relocated = {}

    
    for idx,e in enumerate(arr):
        correct = idx + 1
        if correct != e:
            if correct in been_relocated:
                idx2 = been_relocated[correct]
            else:
                idx2 = arr.index(correct, correct)

            been_relocated[e] = idx2
            arr[idx], arr[idx2] = arr[idx2], arr[idx]
            min_swap += 1
    
    return min_swap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
