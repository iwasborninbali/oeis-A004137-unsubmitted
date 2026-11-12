"""Difference witness and Wichmann gaps; OpenAI Codex, 2026-11-13."""
from itertools import accumulate
marks=(0,1,2,8,15,16,26,36,46,56,59,63,65,68)
differences={b-a for a in marks for b in marks if b>a}
assert differences==set(range(1,69))
gaps=tuple(b-a for a,b in zip(marks,marks[1:]))
print('marks:',len(marks),'segments:',len(gaps),'length:',marks[-1])
print('missing differences:',sorted(set(range(1,69))-differences))
for r in range(3):
    s=11-4*r
    for minor in (0,1):
        g=(1,)*r+(r+1,)+(2*r+1,)*(r+minor)+(4*r+3,)*s+(2*r+2,)*(r+1-minor)+(1,)*r
        assert len(g)==13
        assert g!=gaps and g[::-1]!=gaps
        print('r,s,minor,length:',r,s,minor,sum(g))
print('PASS: complete and neither listed Wichmann variant nor reflection')
