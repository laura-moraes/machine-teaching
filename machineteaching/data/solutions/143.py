def formula(D):
    # So it works using eval
    import math
    C = 50
    H = 30
    Q = round(math.sqrt(2*C*D/float(H)))
    return Q
