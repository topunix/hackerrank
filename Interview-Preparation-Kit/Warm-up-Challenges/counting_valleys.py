import os

# Complete the countingValleys function below.
def countingValleys(n, s):
    steps = list(s)
    up = down = sea_level = valleys = 0
    for step in steps:
        if step == 'U':
            up += 1
        else:
            down += 1
        
        if up == down:
            if sea_level == -1:
                if up == 1 and step == 'U':
                    valleys += 1
            # reset
            sea_level = up = down = 0
            continue
        elif up > down:
            sea_level = 1
            continue
        elif down > up:
            # Below sea level
            if sea_level >= 0:
                sea_level = -1
                up = 0
                continue
            elif sea_level == -1:
                if up == 1 and step == 'U':
                    valleys += 1
                    continue
    
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
