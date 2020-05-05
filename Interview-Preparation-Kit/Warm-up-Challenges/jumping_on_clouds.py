import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    num2Jumps = currCloud = 0
    # maximum number of '2' jumps wins
    for idx, cl in enumerate(c):
        try:
            if idx == currCloud:
                if (c[idx + 2] == 0):
                    num2Jumps += 1
                    currCloud = idx + 2
            elif idx > currCloud:
                currCloud = idx
                if (c[idx + 2] == 0):
                    num2Jumps += 1
                    currCloud = idx + 2
        except IndexError:
            pass
    
    numJumps = len(c) - 1 - num2Jumps
    
    return numJumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
