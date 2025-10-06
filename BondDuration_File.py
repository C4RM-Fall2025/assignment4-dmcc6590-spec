def getBondDuration(y, face, couponRate, m, ppy=1):
    periodic_y = y / ppy
    n = m * ppy
    periodic_coupon = face * couponRate / ppy
    bondPrice = 0
    weighted_sum = 0
    for t in range(1, n + 1):
        if t < n:
            cf = periodic_coupon
        else:
            cf = periodic_coupon + face
        pvcf = cf / (1 + periodic_y) ** t
        bondPrice += pvcf
        weighted_sum += pvcf * t
    bondDuration = weighted_sum / bondPrice
    return bondDuration

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

duration = getBondDuration(y, face, couponRate, m, ppy)
print("getBondDuration:", duration)