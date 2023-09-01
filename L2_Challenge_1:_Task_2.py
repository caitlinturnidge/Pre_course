n = 542

def digitize(n):
    n = str(n)
    array = []
    for i in range(len(n)):
        array.append(int(n[len(n)-i-1]))
    return array

print(digitize(n))