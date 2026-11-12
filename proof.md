# Counterexample conditional on the published optimum

Let R=(0,1,2,8,15,16,26,36,46,56,59,63,65,68). It has 14 marks, 13 gaps, and length 68. The finite difference checker confirms that all differences 1,...,68 occur. The reported established value A004137(14)=68 implies this ruler is optimal. That optimality is taken from the published entry, not independently established here.

For nonnegative integers r,s, the standard major Wichmann gap string is

    1^r, (r+1), (2r+1)^r, (4r+3)^s, (2r+2)^(r+1), 1^r,

where exponent denotes repetition. The minor variant changes the exponents of (2r+1) and (2r+2) to r+1 and r, respectively. Both have 4r+s+2 gaps. Thus 13 gaps require 4r+s=11, giving (r,s)=(0,11),(1,7),(2,3). The corresponding major lengths are 36,64,68 and minor lengths 35,63,67. Hence only the major variant at (2,3) could have the witness's length. Its gaps are (1,1,3,5,5,11,11,11,6,6,6,1,1), whereas the witness has gaps (1,1,6,7,1,10,10,10,10,3,4,2,3). Reflection reverses gaps, so neither this ruler nor its reflection is that Wichmann ruler. The independent checker tests all six strings and their reversals.

Accordingly, conditional on the published optimum, the literal assertion that every optimal ruler with more than 12 segments is Wichmann is false. This does not disprove that some Wichmann ruler attains each optimum, nor the conjectured numerical continuation. This is a previously published counterexample, not a new discovery. The argument is human-checkable and not formally machine-checked.
