# Verification certificate

## Claim

The displayed 14-mark length-68 ruler is complete and is neither of the listed major/minor Wichmann forms nor their reflections.

Given the published optimum A004137(14)=68, it is an optimal counterexample to the literal universal assertion for more than 12 segments.

## Evidence

| What | Program | Author and date | Coverage | Result |
|---|---|---|---|---|
| Producer | `programs/producer.py` | ChatGPT, 2026-11-12 | Witness differences, both variants, finite extra examples | Passed |
| Independent check | `verification/check.py` | OpenAI Codex, 2026-11-13 | Witness differences and six parameter/variant cases plus reflections | Passed |
| Human-checkable argument | `proof.md` | Adapted by OpenAI Codex from ChatGPT, 2026-11-12 | Conditional implication from published optimality | Not machine-checked |

The programs share the witness and family definitions but no code or data tables. The guide's review is recorded in `athanor-oeis/tasks/README.md`.

## Replayed for this repository

2026-11-13, Darwin arm64, Python 3.14.6: `python3 programs/producer.py` and `python3 verification/check.py` passed; the latter prints `missing differences: []` and six variant lengths. Outputs are in `verification/logs/`.

## Not covered

Optimality at 14 marks is reported from the published A004137 value, not independently established here. No claim about optimality of Wichmann rulers in unverified cases is resolved. The proof is not formally machine-checked.

## Guide's independent check

pending

## Verdict

partial — witness properties were independently replayed, but the necessary optimality bound is not independently certified here.
