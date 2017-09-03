class Inventory:
    def check_inventory(self, order_id):
        return True

class Payment:
    def make_payment(self, payment_details, customer_address):
        return True

class Shipping:
    def ship_order(self, order_id, customer_address):
        return True

class Order:
    def __init__(self):
        self.inventory_manager = Inventory()
        self.payment_manager = Payment()
        self.shipment_manager = Shipping()

    def order(self, order_id, payment_details, customer_address):
        inventory_exists = self.inventory_manager.check_inventory(order_id)
        if inventory_exists:
            successful_payment = self.payment_manager.make_payment(payment_details, customer_address)
            if successful_payment:
                has_shipped = self.shipment_manager.ship_order(order_id, customer_address)
                return has_shipped
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    order_manager = Order()
    order_complete = order_manager.order(123, "Visa123", "123 Test Drive")
