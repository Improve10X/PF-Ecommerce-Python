class CashPayment:
    def __init__(self, amount_paid):
        self.amount_paid = amount_paid

    def process_payment(self, amount):
        # In a real implementation, you would handle cash payment
        print(f"Processing cash payment of ${amount}...")
        if self.amount_paid >= amount:
            print("Payment successful! Change:", self.amount_paid - amount)
        else:
            print("Insufficient cash. Payment failed.")
