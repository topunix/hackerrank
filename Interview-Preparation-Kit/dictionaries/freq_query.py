import os
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    d = defaultdict(int)
    f = defaultdict(set)

    for (c,v) in queries:
        if c==3 : yield int( len(f[v])>0 ) ; continue
        
        f[d[v]].discard(v)
        
        if c==1 : d[v] += 1
        
        elif d[v]>0 : d[v] -= 1
        
        f[d[v]].add(v)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
