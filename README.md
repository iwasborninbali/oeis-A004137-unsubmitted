# OEIS A004137: Wichmann ruler wording (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted** (lab registry, 14 Nov 2026).

- [A004137](https://oeis.org/A004137), hypothesis of Oct 09 2011 false as worded (example in A193802): **candidate** (2026-11-13: repository built (core c5)). Certificate: partial.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

## Definition

A complete ruler with n marks is a set 0=x₀<...<xₙ₋₁=L of integers whose positive differences contain every integer 1,...,L. A004137(n) is the maximum such L, equivalently the maximum number of edges of a graceful n-vertex graph; its offset is 1. A ruler with n marks has n-1 segments. Major and minor Wichmann families are defined by their gap strings in [proof.md](proof.md).

The snapshot `context/A004137.seq` and the live [entry](https://oeis.org/A004137), read 2026-11-13, quote Peter Luschny, October 9, 2011, updated October 1, 2015: “If the conjecture is true that an optimal ruler with more than 12 segments is a Wichmann ruler then the sequence continues 232, 251, 270, 289, 308, 327, ...” The entry does not record the previously published counterexample to the literal universal reading.

## Terms / result

| marks | segments | length | example |
|---:|---:|---:|---|
| 14 | 13 | 68 | 0,1,2,8,15,16,26,36,46,56,59,63,65,68 |

This is a complete non-Wichmann ruler even up to reflection; its optimality relies on the published A004137(14)=68. It was already recorded by Peter Luschny in A193802. It refutes the universal wording, not the weaker claim that an optimal Wichmann ruler exists, nor the proposed continuation.

## How it was obtained

The difference set verifies completeness; the finite parameter possibilities for both Wichmann variants exclude the witness and its reflection. See [proof.md](proof.md).

## Verification

Independent programs reproduce completeness and exclude the listed Wichmann forms. They do not independently establish the 14-mark optimum; that is a published result. The argument is human-checkable, not machine-checked. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

The witness is explicitly attributed to Luschny's A193802 entry. ChatGPT and Claude Code reviewed the wording distinction. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Run `python3 programs/producer.py` and `python3 verification/check.py`, together a few seconds on the recorded machine. The checker prints `missing differences: []` and ends `PASS: complete and neither listed Wichmann variant nor reflection`. Full logs are in `verification/logs/`.

## Provenance

Source `projects/science/athanor-oeis`, commit `7662d9a678c6d414685a899a631c63ac320f6840`, paths `tasks/2026-11-12-A004137-graceful-wichmann/answers/2026-11-12-chatgpt.md`, `context/A004137.seq`, and `TASK.md`. Guide review is recorded in `tasks/README.md`.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
