__author__ = 'Sergey Khrul'

#
# Seventh task of Section #2 - Class and objects
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


    @classmethod
    def franchise(cls, main_store):
        franchise_store = cls(main_store.store_name + ' - franchise')
        franchise_store.items = main_store.items.copy()
        return franchise_store

    @staticmethod
    def store_details(store):
        details_str = "{}, total stock price: {}".format(store.store_name, store.stock_price())
        return details_str

store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

print((Store.franchise(store)).store_name)  # returns a Store with name "Test - franchise"
print((Store.franchise(store2)).store_name)  # returns a Store with name "Amazon - franchise"

print(Store.store_details(store))  # returns "Test, total stock price: 0"
print(Store.store_details(store2))  # returns "Amazon, total stock price: 160"