#!/usr/bin/env python3
"""Independent bitset audit of the 14-mark witness and Wichmann families.

No repository modules, tables, or algorithms are imported. Uses an OR of shifted
mark bitsets to build the full distance spectrum in one pass over the marks.
"""
from collections import Counter
from time import perf_counter

R = (0, 1, 2, 8, 15, 16, 26, 36, 46, 56, 59, 63, 65, 68)


def measured(marks):
    bits = sum(1 << p for p in marks)
    spectrum = 0
    for p in marks:
        spectrum |= bits >> p
    return spectrum & ~1


def complete(marks):
    end = marks[-1]
    return measured(marks) == ((1 << (end + 1)) - 2)


def ruler(r, s, variant):
    # Independently implement the run-length *mathematical definition*.
    runs = ((1, r), (r + 1, 1), (2 * r + 1, r + variant),
            (4 * r + 3, s), (2 * r + 2, r + 1 - variant), (1, r))
    positions = [0]
    for distance, multiplicity in runs:
        for unused in range(multiplicity):
            positions.append(positions[-1] + distance)
    return tuple(positions)


def main():
    start = perf_counter()
    assert len(R) == 14 and R[0] == 0 and R[-1] == 68
    assert len(set(R)) == 14 and list(R) == sorted(R)
    observed = measured(R)
    full = (1 << 69) - 2
    assert observed == full
    b = sum(1 << p for p in R)
    counts = Counter(((b >> d) & b).bit_count() for d in range(1, 69))
    assert sum(counts.values()) == 68 and 0 not in counts
    print('witness marks=14 segments=13 length=68')
    print('witness spectrum=1..68; missing=0; multiplicity_histogram=' + str(sorted(counts.items())))

    options = []
    for r in range(3):
        s = 11 - 4 * r
        for v in (0, 1):
            a = ruler(r, s, v)
            assert len(a) == 14
            assert R != a and R != tuple(68 - x for x in reversed(a))
            options.append((r, s, 'minor' if v else 'major', a[-1]))
    print('13-gap family cases (r,s,type,length)=' + str(options))
    print('witness Wichmann match including reflection=NO')

    tested = 0
    for r in range(101):
        for s in range(101):
            for v in (0, 1):
                a = ruler(r, s, v)
                assert len(a) == 4 * r + s + 3
                assert a[-1] == 4 * r * (r + s + 2) + 3 * (s + 1) - v
                assert complete(a), (r, s, v)
                tested += 1
    print(f'complete family cases r,s=0..100, major+minor: {tested}/{tested} PASS')

    checked = 0
    for k in range(2, 201):
        candidates = [ruler(r, k - 2 - 4 * r, 0)[-1]
                      for r in range((k - 2) // 4 + 1)]
        expected = (k * k - ((k % 6) - 3) ** 2) // 3 + k
        assert max(candidates) == expected, (k, candidates, expected)
        checked += 1
    print(f'maximal major Wichmann lengths vs A289761 formula: segments k=2..200, {checked}/{checked} PASS')
    print(f'elapsed_seconds={perf_counter() - start:.6f}')


if __name__ == '__main__':
    main()
