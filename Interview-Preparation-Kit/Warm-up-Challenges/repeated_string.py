import os
from collections import Counter

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    counts = Counter(s)
    nd = n//l
    rm = n - (l * nd)
    counta = Counter(s[:rm])
    na = counta['a'] + (nd * counts['a']) 
    return na
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
