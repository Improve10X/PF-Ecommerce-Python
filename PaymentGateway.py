class PaymentGateway:
    def process_credit_card_payment(self, card_number, expiry_date, cvv):
        print("Processing credit card payment...")
        # In a real implementation, this would involve validation and communication with a payment provider
        print("Payment successful!")

    def process_debit_card_payment(self, card_number, expiry_date, pin):
        print("Processing debit card payment...")
        # In a real implementation, this would involve validation and communication with a payment provider
        print("Payment successful!")

    def process_cash_payment(self, amount_paid):
        print(f"Processing cash payment of ${amount_paid:.2f}...")
        # In a real implementation, this would involve handling cash transactions and change
        print("Payment successful!")

    def process_upi_payment(self, upi_id):
        print(f"Processing UPI payment with ID {upi_id}...")
        # In a real implementation, this would involve validation and communication with a UPI provider
        print("Payment successful!")
