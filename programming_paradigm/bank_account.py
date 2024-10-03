class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an initial balance.
        Default balance is 0 if not specified.
        """
        self._account_balance = initial_balance 
    def deposit(self, amount):
        """
        Deposits the specified amount to the acccount.
        :param amount: Amount to deposit(must be a positive number).
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.
        :param amount: Amount to withdraw.
        :return: True if withdrawal was successful, False if otherwise
        
        """
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        """
        Displays the current balance
        """
        print(f"Current Balance: ${self._account_balance:.2f}")


