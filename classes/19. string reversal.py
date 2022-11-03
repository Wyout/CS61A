def reversal(S):
    if len(S) == 1:
        return S
    else:
        return reversal(S[1:]) + S[0]