class UPIPayment:
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def process_payment(self, amount):
        # In a real implementation, you would process the payment using UPI
        print(f"Processing UPI payment of ${amount} using ID {self.upi_id}...")
