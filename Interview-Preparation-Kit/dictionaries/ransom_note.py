from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m = Counter(magazine)
    n = Counter(note)
    answer = "Yes"
    for w in n:
        if m.get(w):
            if n[w] > m[w]:
               answer = "No"  
        else:
            answer = "No"

    print(answer)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
