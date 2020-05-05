import os

def sherlockAndAnagrams(s):
    #1. Traverse all possible substrings within string
    #2. Check if any two substrings of equal length are anagrams
    a_count = 0
    combos = list(s[i:j+1] for i in range(len(s)) for j in range(i, len(s)))
    combos = sorted(combos, key=len)
    for n in range(len(combos) - 1):
        for m in range(n+1,len(combos)):
            if len(combos[n]) != len(combos[m]):
                break
            if sorted(combos[n]) == sorted(combos[m]):
                a_count+=1
    return a_count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
