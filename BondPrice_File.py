def getBondPrice(y, face, couponRate, m, ppy=1):
    periodic_y = y / ppy
    n = m * ppy
    periodic_coupon = face * couponRate / ppy
    coupon_pv = periodic_coupon * (1 - (1 + periodic_y) ** -n) / periodic_y
    face_pv = face / (1 + periodic_y) ** n
    bondPrice = coupon_pv + face_pv
    return bondPrice

y = 0.03
face = 2000000
couponRate = 0.04
m = 10

ppy1 = getBondPrice(y, face, couponRate, m, ppy=1)
print("ppy=1:", ppy1)

ppy2 = getBondPrice(y, face, couponRate, m, ppy=2)
print("ppy=2:", ppy2)

ppy_default = getBondPrice(y, face, couponRate, m)
print("no input ppy:", ppy_default)