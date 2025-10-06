def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    periodic_coupon = face * couponRate
    for t, y in enumerate(yc, 1):
        if t < m:
            cf = periodic_coupon
        else:
            cf = periodic_coupon + face
        pv = cf / (1 + y) ** t
        bondPrice += pv
    return bondPrice

yc = [0.010, 0.015, 0.020, 0.025, 0.030]
face = 2000000
couponRate = 0.04
m = 5

bond_price = getBondPrice_E(face, couponRate, m, yc)
print("priceE", bond_price)