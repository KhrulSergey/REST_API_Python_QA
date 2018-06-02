__author__ = 'Sergey Khrul'
#
# Sixth task of Section #2 - Class and objects
#
class Store:
    def __init__(self, store_name: str):

        self.store_name = store_name
        self.items = []

    def add_item(self, item_name: str, item_price: float):
        new_item = {'name': item_name, 'price': item_price}
        self.items.append(new_item)

    def stock_price(self):
        total_prices = sum(item["price"] for item in self.items)
        return total_prices


galaxy_store = Store("Galaxy Mart")
for x in range(10):
    galaxy_store.add_item("good" + x.__str__(), x+12.0)

print(*galaxy_store.items, sep="\n")
print(galaxy_store.stock_price())
