import os

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    c_num = 0
    intersection = set(a) & set(b)
    for i in intersection:
        c1 = list(a).count(i)
        c2 = list(b).count(i)
        if c1 == c2:
            continue
        else:
            rc = abs(c1 - c2)
            c_num += rc

    for item in itertools.chain(list(a),list(b)):
        if item not in intersection:
            c_num += 1

    return c_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
