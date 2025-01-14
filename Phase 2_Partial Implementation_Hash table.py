# This function checks if the product already exists in the inventory. 
# If it does not, the product is added with its corresponding attributes (name, quantity, price, and category).

def add_product(self, product_id, name, quantity, price, category):
    if product_id in self.products:
        print(f"Product {product_id} already exists.")
    else:
        self.products[product_id] = {
            'name': name,
            'quantity': quantity,
            'price': price,
            'category': category
        }
        print(f"Product {product_id} added.")