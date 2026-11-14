// Independently find exact maximum complete-ruler lengths up to 11 marks.
// Built around incremental coverage masks and a combinatorial pruning bound.
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

static uint64_t visited = 0;
static int target;
static vector<int> chosen;

static bool extend(int next, int left, uint64_t distances) {
    ++visited;
    if (!left) {
        return __builtin_popcountll(distances) == target;
    }
    const int fixed = (int)chosen.size();
    const int new_pair_capacity = left * fixed + left * (left - 1) / 2;
    if (__builtin_popcountll(distances) + new_pair_capacity < target)
        return false;
    for (int p = next; p <= target - left; ++p) {
        uint64_t d = distances;
        for (int q : chosen) {
            const int gap = p > q ? p - q : q - p;
            d |= uint64_t(1) << gap;
        }
        chosen.push_back(p);
        if (extend(p + 1, left - 1, d)) return true;
        chosen.pop_back();
    }
    return false;
}

static bool can_measure(int marks, int length) {
    if (marks == 1) return length == 0;
    target = length;
    chosen = {0, length};
    uint64_t initial = uint64_t(1) << length;
    return extend(1, marks - 2, initial);
}

int main() {
    using clock = chrono::steady_clock;
    auto t0 = clock::now();
    cout << "exact maxima by independent exhaustive search (n:length):";
    for (int n = 1; n <= 11; ++n) {
        int answer = -1;
        for (int length = n * (n - 1) / 2; length >= max(0, n-1); --length) {
            if (can_measure(n, length)) {
                answer = length;
                break;
            }
        }
        if (answer < 0) return 1;
        cout << " " << n << ":" << answer;
    }
    cout << "\nrecursive_nodes=" << visited << "\n";
    auto ms = chrono::duration_cast<chrono::milliseconds>(clock::now() - t0).count();
    cout << "elapsed_seconds=" << (double(ms) / 1000.0) << "\n";
}
