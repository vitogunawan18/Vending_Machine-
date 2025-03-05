from datetime import datetime

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item, expiry_date=None, price=None):
        self.items.append({"item": item, "expiry_date": expiry_date, "price": price})

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stock kosong"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stock Kosong"

    def count_item(self):
        return len(self.items)

    def get_all_items(self):
        return [(item_info["item"], item_info["expiry_date"]) for item_info in self.items]

    def get_all_items_with_price(self):
        return [(item_info["item"], item_info["price"]) for item_info in self.items]
