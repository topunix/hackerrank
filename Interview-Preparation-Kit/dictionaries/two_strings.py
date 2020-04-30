# Complete the twoStrings function below.
def twoStrings(s1, s2):
    a = {i:0 for i in s1}
    b = {i:0 for i in s2}
    for x in a:
        if b.get(x) != None:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
