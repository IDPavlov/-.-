import sys

ns = int(sys.argv[1]), int(sys.argv[3])
ms = int(sys.argv[2]), int(sys.argv[4])

def MCD(a, b):
    a, b = min(a, b), max(a, b)
    while a > 0:
        a, b = b % a, a
    return b

for i in range(2):
    n, m = ns[i], ms[i]
    
    cycle = ''.join(
        str(j) for j in range(1, n + 1)
    ) * ((m-1) // MCD(n, m-1))
    
    print(
        ''.join(cycle[j] for j in range(0, len(cycle), m-1)),
        end=''
    )
    
    
