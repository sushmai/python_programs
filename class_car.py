class Customer(object):
    """
    Bank Customer Properties :
    Arributes
    name - string
    balnace - float
    """

    def __init__(self, name, balance = 0.0):
        
    """
    return a customer whose name is name and balance startine "Balance"
    """
        self.name = name
        self.balance = balance

    def withdraq(self, amount):
        if amount > self.balance:
            
    
