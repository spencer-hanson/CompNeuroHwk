"""
P(S) = 0.1

P(F|S) = 1/2
P(F|!S) = 1/18

H(S) = -sum(P(S=s)log(p(S=s))

H(S) - E_f[H(S|F=f)]

H(F) - E_s[H(F|S=s)]


1/2*0.1/(1/18)

0.9
H(F) = -0.9*log2(0.9)
0.1366803

H(F|S) = -1/2*log2(1/2)
= 0.5
-0.9*log2(0.9)

-0.9*log2(0.9) - -1*(0.5*log2(0.5) + (1/18)*log2(1/18))

P(!S)*(H(F|!S)+H(!F|!S))
P(S)*( H(F|S) + H(!F|S))

F|!S = 1/18
!F|!S = 17/18
F|S = 1/2
!F|S = 1/2
"""
import math


def entropy(val):
    if isinstance(val, list):
        return sum([v*math.log2(v) for v in val]) * -1
    else:
        return -1 * val * math.log2(val)


if __name__ == "__main__":
    f_ns = 1 / 18
    nf_ns = 17 / 18
    f_s = 1 / 2
    nf_s = 1 / 2

    h_f_ns = entropy(f_ns)
    h_nf_ns = entropy(nf_ns)
    h_f_s = entropy(f_s)
    h_nf_s = entropy(nf_s)

    s = 0.1
    ns = 0.9

    avg_noise_entropy = s * h_f_s + s * h_nf_s + ns * h_f_ns + ns * h_nf_ns


    # P(S|F) = P(F|S)P(S) / P(F)
    # P(F) = P(F|S)P(S) / P(S|F)
    # Using bayes theorem:
    f = f_ns * ns + f_s * s
    nf = nf_ns * ns + nf_s * s

    # H(F) = -sum(P_f*log2(P_f))
    # - [f*log2(f) + nf*log2(nf)]
    h_f = entropy([f, nf])

    print(f"H(f) = {h_f}")
    print(f"Mutual Information: {h_f - avg_noise_entropy}")

