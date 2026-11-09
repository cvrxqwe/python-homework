import json


class OrderSystem:
    def __init__(self):
        self.filename = "orders.json"
        self.orders = self.load_orders()

    # Read file on startup
    def load_orders(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # If the program is running for the first time and there is no file yet
            return []

    # Save list to file
    def save_orders(self):
        with open(self.filename, "w") as file:
            json.dump(self.orders, file, indent=4)

    # Add a new order
    def add_order(self, order_id, client, items, total):
        new_order = {
            "order_id": order_id,
            "client": client,
            "items": items,
            "total": total,
            "status": "new"  # Default status for all new orders
        }
        self.orders.append(new_order)
        self.save_orders()
        print(f"Added order #{order_id} for {client}.")

    # Find an order by ID
    def find_order(self, order_id):
        for order in self.orders:
            if order["order_id"] == order_id:
                print(f"Found: Order #{order_id} | Client: {order['client']} | Status: {order['status']}")
                return order

        print(f"Order #{order_id} not found.")
        return None

    # Change order status
    def change_status(self, order_id, new_status):
        order = self.find_order(order_id)  # Reusing the find_order method
        if order:
            order["status"] = new_status
            self.save_orders()
            print(f"Order #{order_id} status updated to '{new_status}'.")


# --- Testing ---
shop = OrderSystem()

print("=== Adding Orders ===")
shop.add_order(101, "Ivan", ["Laptop", "Mouse"], 1200)
shop.add_order(102, "Maria", ["Keyboard"], 50)

print("\n=== Searching ===")
shop.find_order(101)
shop.find_order(999)  # Testing a non-existent order

print("\n=== Updating Status ===")
shop.change_status(101, "processing")
shop.change_status(102, "completed")