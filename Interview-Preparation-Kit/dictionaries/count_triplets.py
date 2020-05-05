import os
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    num_triplets = 0
    r3 = defaultdict(int)
    r2 = defaultdict(int)
    for v in arr:
        num_triplets += r3[v]
        r3[v*r] += r2[v]
        r2[v*r] += 1
    return num_triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
