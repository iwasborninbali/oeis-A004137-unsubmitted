from itertools import combinations

def complete(a):
    L = a[-1]
    distances = {
        y-x for i,x in enumerate(a)
        for y in a[i+1:]
    }
    return distances == set(range(1, L+1))

def wichmann(r, s, minor=False):
    gaps = (
        [1]*r + [r+1]
        + [2*r+1]*(r+int(minor))
        + [4*r+3]*s
        + [2*r+2]*(r+1-int(minor))
        + [1]*r
    )
    a = [0]
    for g in gaps:
        a.append(a[-1] + g)
    return a

def exact_max(n):
    if n == 1:
        return 0
    for L in range(n*(n-1)//2, n-2, -1):
        for interior in combinations(range(1, L), n-2):
            if complete((0, *interior, L)):
                return L
    raise AssertionError(n)

C = [0,1,2,8,15,16,26,36,46,56,59,63,65,68]

print('counterexample: marks=%d segments=%d length=%d complete=%s' %
      (len(C),len(C)-1,C[-1],complete(C)))

print('counterexample gaps:',
      [y-x for x,y in zip(C,C[1:])])

possible = [
    wichmann(r, 11-4*r, minor)
    for r in range(3)
    for minor in (False, True)
]

print('Wichmann or reflected among 14-mark rulers:',
      any(C == a or
          C == [a[-1]-x for x in a[::-1]]
          for a in possible))

print('Wichmann 14-mark (r,s,length):',
      [(r,11-4*r,wichmann(r,11-4*r)[-1])
       for r in range(3)])

print('exhaustive max length n=1..8:',
      [exact_max(n) for n in range(1,9)])

assert all(
    complete(wichmann(r,s,minor))
    for r in range(21)
    for s in range(21)
    for minor in (False,True)
)

print('Wichmann completeness: PASS (r,s=0..20, both types: 882 rulers)')

print('Wichmann lower bounds n=27..32:',
      [max(wichmann(r,n-4*r-3)[-1]
           for r in range((n-3)//4+1))
       for n in range(27,33)])
