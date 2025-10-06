def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    cash_flows = [coupon] * (len(times) - 1) + [coupon + face]
    present_values = [cf / (1 + rate) ** t for cf, rate, t in zip(cash_flows, yc, times)]
    bondPrice = sum(present_values)
    
    return bondPrice

yc = [0.010, 0.015, 0.020, 0.025, 0.030]
times = [1, 1.5, 3, 4, 7]
face = 2000000
couponRate = 0.04

bond_price = getBondPrice_Z(face, couponRate, times, yc)
print(“PriceZ:".,bond_price)