class BankAccount:
	def __init__(self, int_rate=0.01, balance=0): 
		self.int_rate=0.01
		self.balance=balance
		
	def deposit(self, amount):
		self.balance+=amount
		
	def withdraw(self, amount):
		self.balance -= amount
		if self.balance==0:
			print("Insufficient funds: Charging a $5 fee and deduct $5")
		
	def display_account_info(self):
		print("Balance:", self.balance)
		
	def yield_interest(self):
		self.balance+= self.balance*self.int_rate
		
mohammad=BankAccount(0.01,1000)
mohammad.deposit(100)
mohammad.deposit(200)
mohammad.deposit(300)
mohammad.withdraw(100)
mohammad.yield_interest()
print(mohammad.display_account_info())


Ahmad=BankAccount(0.01,3000)
Ahmad.deposit(100)
Ahmad.deposit(200)
Ahmad.withdraw(100)
Ahmad.withdraw(200)
Ahmad.withdraw(500)
Ahmad.withdraw(800)

print(Ahmad.display_account_info())