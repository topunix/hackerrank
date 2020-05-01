import os
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    s = Counter(s)
    v = s.values()
    lv = list(v)
    sv = list(set(v))
    if len(sv) <= 1:
        return "YES"
    elif len(sv) == 2:
        if (lv.count(1) == 1) or (abs(sv[0] - sv[1]) == 1 and lv.count(max(sv)) == 1):
            return "YES"       
        else:
            return "NO"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
