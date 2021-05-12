import math
import operator


class Price:
    def __init__(self, original_price: float, ind):
        self.original_price = original_price
        self.floor_original_price = math.floor(original_price)
        self.ceiling_original_price = math.ceil(original_price)
        if self.ceiling_original_price == self.original_price:
            self.to_ceiling = 1
        else:
            self.to_ceiling = self.ceiling_original_price - self.original_price

        self.index = ind
        self.sub_total = self.floor_original_price


prices = [5.40, 3.30, 5.00, 6.70, 5.30, 9.90, 2.20, 1.10, 4.30, 3.40, 5.50]
computed_prices = []
original_total_price = 0.0
floor_total_price = 0
total = 0

for index, price in enumerate(prices):
    computed_price = Price(price, index)
    computed_prices.append(computed_price)
    original_total_price += price
    floor_total_price += computed_price.floor_original_price


rounded_total_price = int(round(original_total_price, 0))
diff = rounded_total_price - floor_total_price
print("un-rounded total price:", original_total_price)
print("rounded total price:", rounded_total_price)
print("floor total price:", floor_total_price)
print("diff:", diff)

computed_prices.sort(key=operator.attrgetter('to_ceiling'))

for i in range(diff):
    computed_prices[i].sub_total += 1

computed_prices.sort(key=operator.attrgetter('index'))

for computed_price in computed_prices:
    print(computed_price.sub_total, end=' ')
    total += computed_price.sub_total

print()
print(total)
