class CourierDelivery:
    def calculate_cost(self, weight):
        # Courier: base price 100 UAH + 20 UAH per kilogram
        return 100 + (weight * 20)


class PostDelivery:
    def calculate_cost(self, weight):
        # Post: base price 50 UAH + 10 UAH per kilogram
        return 50 + (weight * 10)


class PickupDelivery:
    def calculate_cost(self, weight):
        # Pickup: always free, regardless of weight
        return 0


def show_delivery_costs(delivery_methods, weight):
    print(f"--- Вартість доставки для замовлення вагою {weight} кг ---")

    for delivery in delivery_methods:
        # Get the class name (e.g., "PostDelivery") for output formatting
        method_name = delivery.__class__.__name__

        # Polymorphism in action:
        # The loop doesn't know the exact class, it just calls the calculate_cost method
        cost = delivery.calculate_cost(weight)

        if cost == 0:
            print(f"{method_name}: Безкоштовно")
        else:
            print(f"{method_name}: {cost} грн")


# Create a list of objects (instances) of different delivery classes
available_deliveries = [CourierDelivery(), PostDelivery(), PickupDelivery()]

# Test for a weight of 2 kg
show_delivery_costs(available_deliveries, 2)

# Test for a weight of 10 kg
show_delivery_costs(available_deliveries, 10)