class CreditCardPayment:
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self, amount):
        # In a real implementation, you would process the payment using the card details
        print(f"Processing credit card payment of ${amount}...")
