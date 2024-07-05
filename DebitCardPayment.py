class DebitCardPayment:
    def __init__(self, card_number, expiry_date, pin):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.pin = pin

    def process_payment(self, amount):
        # In a real implementation, you would process the payment using the card details
        print(f"Processing debit card payment of ${amount}...")
