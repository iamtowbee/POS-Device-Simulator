__title__ = "POS Device Simulator"

__description__ = "Simulates actions like withdrawals, deposits, airtime/data, bill payments and mobile banking (culled from OPAY POS features.) Load bank account which means the bank must be a variable with account balance. The simulation loads customer banking data from a dictionary, not unlike a real-world poll of a bank's customer database."

__author__ = "Oluwatobi Oluyede"

import sys, time

pos_data = {
	"main_account": [1000000, ("Oluwatobi Oluyede", 1234567890, "First Bank of Nigeria")],
	"1357924680": 240000,
	"1111111111": 120000,
	"1010101010": 50000,
}

internet_data = {
	"MTN": {
		"40 MB": 100,
		"100 MB": 150,
		"200 MB": 250,
		"400 MB": 500,
		"1.5 GB": 2000,
		"5 GB": 10000,
		"Unlimited": 20000
	},
	"Moov": {
		"40 MB": 100,
		"100 MB": 150,
		"200 MB": 250,
		"400 MB": 500,
		"1.5 GB": 2000,
		"5 GB": 10000,
		"Unlimited": 20000
	}
}

def typewrite(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush
		time.sleep(0.01)

class POS:
	def __init__(self):
		self.account = pos_data["main_account"]
		balance = str(self.account[1][1])
		obfus_account = f"{balance[:4]}xxx{balance[-3:]}"
		typewrite("Initializing POS device...\n\n")
		typewrite(f"Linked account name: {self.account[1][0]}\n")
		typewrite(f"Linked account number: {obfus_account}\n")
		typewrite(f"Linked account balance: {self.account[0]}\n\n")
		typewrite("What would you like to do:\n1. Withdrawal\n2. Deposit\n3. Data\n\nPress 'q' to exit.\n\n")
		self.choice = input(">>> ")
	
	# TODO How to cast a function's argument to a specific type
	def withdrawal(self, account, amount):
		amount = int(amount)
		typewrite(f"You are withdrawing {amount} from your account {account}\n\n")
		acct_balance = pos_data[account]
		if amount > acct_balance:
			typewrite("Insufficient funds!\n")
		else:
			acct_balance -= amount
		typewrite("Withdrawal successful!\n")
		typewrite(f"New account balance for account {account}: {acct_balance}")
	
	def deposit(self, account, amount):
		amount = int(amount)
		typewrite(f"You are depositing {amount} into your account {account}\n\n")
		acct_balance = pos_data[account]
		acct_balance += amount
		typewrite("Deposit successful!\n")
		typewrite(f"New account balance for account {account}: {acct_balance}")
	
	def buy_internet(self, network):
		network_dict = internet_data[network]
		data_list = [(plan, amount) for plan, amount in network_dict.items()]
		index = 1

		typewrite(f"Available data plans for {network}:\n")
		for (plan, amt) in data_list:
			print(f"{index}. {plan} / {amt}", sep="")
			index += 1
		
		typewrite("Please choose a plan:\n")
		try:
			choice = int(input(">>> "))
		except ValueError:
			sys.exit("Wrong input!")

		if choice not in range(1,len(data_list)+1):
			sys.exit("Invalid choice!")
		
		chosen_plan = data_list[choice-1]
		typewrite(f"You have chosen {network}'s {chosen_plan[0]} data priced at {chosen_plan[1]}.\n")

		try:
			typewrite("Please enter your phone number:\n")
			number = int(input(">>> "))
		except ValueError:
			sys.exit("Wrong input!")
		
		valid_number = int("+234" + str(number)) if len(str(number)) == 10 else sys.exit("Invalid phone number!")

		typewrite(f"Recharging {chosen_plan[0]} data plan for {valid_number}\n")
		typewrite("Data recharge successful!")

	
tbigz_pos = POS()

if tbigz_pos:
	match tbigz_pos.choice:
		case "1":
			typewrite("You have chosen withdrawal!\nPlease enter your account number:\n")
			try:
				account = input(">>> ")
				typewrite(f"Your account number is {account} and your balance is {pos_data[account]}\n\n")
			except KeyError:
				typewrite("Account number not in database!\n")
				sys.exit()
			typewrite("Please enter withdrawal amount:\n")
			amount = input(">>> ")
			tbigz_pos.withdrawal(account, amount)

		case "2":
			typewrite("You have chosen deposit!\nPlease enter your account number:\n")
			try:
				account = input(">>> ")
				typewrite(f"Your account number is {account} and your balance is {pos_data[account]}\n\n")
			except KeyError:
				typewrite("Account number not in database!\n")
				sys.exit()
			typewrite("Please enter deposit amount:\n")
			amount = input(">>> ")
			tbigz_pos.deposit(account, amount)
		
		case "3":
			typewrite("You have chosen data subscription!\nPlease select a network:\n")
			for index, net in enumerate(internet_data.keys()):
				typewrite(f"{index+1}. {net}\n")
			network = input(">>> ")
			if network == "1":
				network = "MTN"
			elif network == "2":
				network = "Moov"
			else:
				sys.exit("Invalid input! Enter a number.")
			
			tbigz_pos.buy_internet(network)

		case "q":
			typewrite("Shutting down POS device.")
			sys.exit()