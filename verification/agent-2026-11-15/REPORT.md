# Independent verification report — 2026-11-15

Repository snapshot: `iwasborninbali/oeis-A004137-unsubmitted` at `d019e1b`. Source files read: `README.md`, `CERTIFICATE.md`, `PRIOR-ART.md`, `proof.md`, `programs/producer.py`, `verification/check.py`, and both original logs. All files in this directory were authored independently for this audit. No existing repository files were modified.

## Claim

`CERTIFICATE.md` claims that the 14-mark ruler **R = (0,1,2,8,15,16,26,36,46,56,59,63,65,68)** of length 68 is complete and is neither a major nor a minor Wichmann ruler (nor a reflection), and that, *conditional on the published* `A004137(14)=68`, it gives an optimal counterexample to a **universal** assertion for rulers with more than 12 segments. The certificate explicitly does **not** independently establish the 14-mark upper bound or resolve the existential Wichmann-optimality conjecture.

## Proof check

Referee examination by source line:

1. **Line 3, count and endpoints:** correct: 14 strictly increasing marks, 13 positive gaps, endpoints 0 and 68. No gap.
2. **Line 3, completeness delegated to a checker:** true, independently reproduced below, but the written proof gives no displayed covering table/derivation. **Fixable presentation gap:** include a per-distance bitset certificate or a 68-entry coverage table; a finite calculation suffices. Not a mathematical counterexample to the proof.
3. **Line 3, `A004137(14)=68`:** the proof *explicitly assumes* this published upper bound. OEIS A004137 and A193802 report it, but this audit did not independently certify nonexistence of a longer complete ruler with 14 marks. **Fixable gap for an unconditional, fully independent optimality proof**: supply a reproducible exhaustive exclusion of lengths >=69 with an auditable certificate, or an independently checked published upper-bound theorem. The conditional statement does not conceal this assumption.
4. **Lines 5–9, identification of Wichmann forms:** the definitions of major and minor variants match MathWorld's published constructions. But treating those as *all* possible rulers described as Wichmann requires specifying the definition; A193802 itself formally defines the major type, while MathWorld also gives the minor. **Fixable definitional gap:** quote and cite the exact convention, including equivalence under reflection. Under the certificate's explicit two-form definition, the enumeration is exhaustive.
5. **Lines 7–9, number of gaps and six cases:** correct. Both types have `4r+s+2` gaps, so 13 implies `4r+s=11` with nonnegative solutions `(0,11),(1,7),(2,3)`. The six lengths `36,35,64,63,68,67` are correct. No gap.
6. **Line 9, comparing gap strings and reflections:** correct. R's consecutive gaps are `(1,1,6,7,1,10,10,10,10,3,4,2,3)`, whereas the sole length-68 candidate has `(1,1,3,5,5,11,11,11,6,6,6,1,1)`. Reflection reverses gaps. Neither equality occurs. No gap.
7. **Line 11, interpretation of the source conjecture:** **fatal for any asserted refutation of the actual OEIS/Wichmann optimum conjecture**. A non-Wichmann optimal ruler refutes only `EVERY optimal ruler with >12 segments is Wichmann`. The OEIS A004137 sentence is an ambiguous indefinite, and its proposed sequence continuation needs only `EXISTS an optimal Wichmann ruler`. More decisively, Luschny's own *Perfect Rulers* page distinguishes (a) a **universal** conjecture restricted to **more than 13** segments from (b) an **existential** conjecture for **more than 12** segments. R has **exactly 13** segments, so it refutes neither. The new 2026 OEIS A395909 again states the stronger threshold as **more than 13**. **Not fixable using this witness**: restrict the contribution to the true conditional universal counterexample, or find a different witness satisfying the correct threshold/quantifier. The original certificate is carefully conditional, but the README's characterization of the A004137 conjecture as 'false as worded' is not established as a refutation of its intended meaning.
8. **Line 11, novelty:** the assertion that the example was previously published is correct and explicitly disclosed. A193802 (Peter Luschny, 2011) contains the **identical** ruler and explicitly labels it optimal and non-Wichmann; no novelty is present.

**Proof-check verdict: CORRECT WITH FIXABLE GAPS for the narrowly stated conditional universal proposition; NOT a refutation of either historically articulated Wichmann conjecture.** The source-conjecture interpretation is a fatal limitation if the report is read as a discovery disproving A004137's intended hypothesis.

## Independent computation

The audit programs were written afresh, without importing repository modules or copying its implementation.

- `independent.py` encodes each ruler as an integer-position bitset `B` and computes its entire positive-distance spectrum as the OR of `B >> p` over its marks `p`, with bit zero removed. It separately counts multiplicities with bit intersections, constructs Wichmann marks from run-length groups, and checks Wichmann lengths against a separately evaluated algebraic formula.
- **Witness:** 14 marks, 13 segments, length 68; all differences 1–68 occur, with no missing distances. Difference multiplicity histogram `(number of representations : number of distances)` is `1:50, 2:14, 3:3, 4:1`. Neither of the six 13-gap major/minor cases nor its reflection matches R. The case lengths, in major/minor order for `(r,s)=(0,11),(1,7),(2,3)`, are `36,35,64,63,68,67`.
- **Expanded parameter check:** both types for **all `0 <= r,s <= 100`**, totaling **20,402** complete rulers, all PASS. This strictly extends the producer's `0..20` parameter range (882 cases) and the original independent check's six 13-gap cases. Lengths and mark counts also match formulas.
- **Expanded Wichmann maximum:** for **every segment count `k=2..200`**, enumeration of all admissible major Wichmann parameters agrees with the closed formula recorded in OEIS A289761 (199/199 PASS); this extends the producer's 27–32 examples. This is a check **within the Wichmann family**, not an optimality proof among all rulers.
- `exhaustive_small.cpp` uses a separate recursive search with incremental 64-bit distance masks and an upper bound on how many unmeasured distances the remaining marks can cover. It establishes exact maxima for **1..11 marks**: `0,1,3,6,9,13,17,23,29,36,43` (860,041,459 recursive nodes), extending the producer's 1..8 brute-force check. A 12-mark attempt exceeded the execution budget and is **not** certified; no 14-mark exhaustive upper-bound claim is made.
- **Recorded run** (`output.log`): `independent.py` **10.106522 s**; `exhaustive_small.cpp` optimized C++ executable **12.414 s**, plus compilation. Timings vary by machine; platform is the provided Linux container, Python 3, `g++ -O3 -std=c++17`.

SHA-256 of local source and saved output bytes:

```
54eadadc95b764face89cbfe7ccbf365218edb3274a5a34825442fd2d6f9d7d9  independent.py
e21fe81f54333b79f67593016c879711c1907a30d5bf811064aaa46e4b8e04b4  exhaustive_small.cpp
b01decf00f6f16d1d549b762fb8c28895345238f26e6a83945585dddee64e76e  output.log
```

## Prior art

Direct evidence and cross-checks, accessed 2026-11-15:

- [OEIS A004137](https://oeis.org/A004137) and [internal format](https://oeis.org/A004137/internal): `a(14)=68`, the 2011 wording, and 2015 update. The internal record displays revision `#105` dated 2026-05-30. The [per-revision history endpoint](https://oeis.org/history?seq=A004137) returned HTTP 403 in the research tool; **full diff history was not accessible**. Therefore the dated comments were verified, not every historical revision.
- [OEIS A193802](https://oeis.org/A193802) (Luschny, 2011) and [A193803](https://oeis.org/A193803): exactly the same 14-mark, length-68 non-Wichmann example, paired with a 14-mark Wichmann optimum. **Decisive prior disclosure; not new.**
- [Luschny's OEIS Wiki *Perfect Rulers*](https://oeis.org/wiki/User:Peter_Luschny/PerfectRulers): contains the same example, the major family, and distinguishes the universal conjecture for **S>13** from the weaker existential one for **S>12**. [OEIS A395909](https://oeis.org/A395909) (2026) independently restates the `>13` threshold for the stronger claim.
- [A289761](https://oeis.org/A289761) supplies the maximal Wichmann-length formula and candidate numerical continuation; [A349978](https://oeis.org/A349978) lists lengths with no Wichmann optimum, and [A103294](https://oeis.org/A103294) gives ruler conventions. These do not furnish a refutation of Wichmann attainment beyond the known exceptions.
- [MathWorld, *Wichmann Ruler*](https://mathworld.wolfram.com/WichmannRuler.html) defines both major/minor constructions and explicitly says the optimality conjecture concerns **existence**, not every ruler.
- [Wichmann, *A Note on Restricted Difference Bases*](https://doi.org/10.1112/jlms/s1-38.1.465), *J. London Math. Soc.* 38 (1963), 465–466: original construction, not the non-Wichmann witness.
- [Robison, *Parallel Computation of Sparse Rulers* (2014)](https://web.archive.org/web/20160429004505/http://software.intel.com/articles/parallel-computation-of-sparse-rulers), and [Schwartau–Schröder–Wolf–Schoebel, *Large Minimum Redundancy Linear Arrays*](https://doi.org/10.1109/OJAP.2020.3043541), *IEEE OJAP* 2 (2021), 79–85: computational optimality literature; not independent certificates reproduced here.
- [Saarela–Vanhatalo, arXiv:2408.16335](https://arxiv.org/abs/2408.16335), later [*Electronic Journal of Combinatorics* 33(1), P1.40 (2026)](https://doi.org/10.37236/13806): directly states that it is conjectured Wichmann rulers achieve the longest length with `m>13` marks. Its separate counterexample pertains to partial words, **not** this 14-mark ruler.
- [Math StackExchange: *Sparse Ruler Conjecture*](https://math.stackexchange.com/questions/3279766/sparse-ruler-conjecture) (2019–2020): discusses **excess / minimal-mark bounds**, a different claim. Broader searches on MathOverflow, Math StackExchange, arXiv, zbMATH and journal indexes using `Wichmann`, `restricted difference bases`, `optimal ruler`, and the specific 14-mark pattern yielded no earlier *independent* publication of this identical witness beyond Luschny's 2011 OEIS record/wiki. No result in those searches changes the established priority. These are search results, not proof of exhaustive coverage of paywalled literature; zbMATH's full index was not independently browsable.

## Verdict

**PARTIAL.** The finite properties of the witness are independently confirmed; the example is **true and already published**, but no independent 14-mark optimality exclusion was supplied. The constructed ruler is **not** a counterexample to the historically explicit universal (`S>13`) or existential (`S>12`) conjectures. Presenting it as a *new* discovery or as a disproof of the intended A004137 conjecture would be incorrect. The only defensible mathematical claim is the stated conditional refutation of a **different, stronger universal proposition at S>12**, which the original certificate already labels as conditional and prior art.
