#global prompts
prompt_login = "Enter 'login' to begin:"
prompt_retail_agent = "Are you 'retail' or 'agent'?"
prompt_command = "Enter a valid command:"
prompt_new_account_num = "Enter a new account number:"
prompt_new_account_nam = "Enter a new account name:"
prompt_valid_account_num = "Enter a valid account number:"
prompt_valid_account_nam = "Enter a valid account name:"
prompt_deposit = "Enter deposit amount:"
prompt_withdraw = "Enter withdraw amount:"
prompt_transfer_from = "Enter a valid account number to transfer from:"
prompt_transfer_to = "Enter a valid account number to transfer to:"
prompt_transfer = "Enter transfer amount:"
prompt_finish = "If you would like to shut down, type 'Quit'"

#global errors
error_account_num = "Error: Account numbers must be 1-6 digits."
error_account_nam = "Error: Account names must be 1-15 characters."
error_retail_amount = "Error: Transactions above $1,000.00 are not accepted in 'retail' mode."
error_agent_amount = "Error: Transactions above $999,999.99 are not accepted in 'agent' mode."
error_amount_type = "Error: Amount must be entered in cents and greater than 0."
error_account_dne = "Error: Account does not exist."
error_permission = "Error: You do not have permission to do that."
error_account_exists = "Error: Account already exists."
error_account_neg = "Error: Account number must be greater than 0."
error_transfer_same ="Error: Cannot transfer to the same account."

Loggedin = False
Agent = False
Running = True
temp_transaction_summary = []

def inAccountFile(num):
	#check if account number is in master file
	return False

def checkAccountNum(num):
	try:
		num = int(num)
	except ValueError:
		print error_account_num
		return False	
	if num>999999:
		print error_account_num
	elif num<1:
		print error_account_neg
	elif inAccountFile(num):
		print error_account_exists
	else:
		return True
	return False #error has occured
	
def checkAccountName(name):
	if len(name)>15 or len(name)<1:
		print error_account_nam
	else:
		return True
	return False #error has occured	

def create():
	if Agent:
		print prompt_new_account_num
		account_num = raw_input()
		if checkAccountNum(account_num):
			print prompt_new_account_nam
			account_name = checkAccountName(raw_input())
	else:	#retail mode
		print error_permission
	return
	
def delete():
	if Agent:
		print prompt_valid_account_num
		account_num = raw_input()
		if checkAccountNum(account_num):
			print prompt_valid_account_nam
			account_name = checkAccountName(raw_input())
	else:	
		print error_permission
	return	
	
def deposit():	
	print prompt_valid_account_num
	account_num = raw_input()
	if (checkAccountNum(account_num)):
		while (len(account_num) < 6):
			account_num = "0" + account_num
	else:
		return None
	print prompt_deposit
	deposit_val = raw_input()
	try:
		int(deposit_val)
	except ValueError:
		print error_amount_type
		return None
	if Agent:
		if int(deposit_val) > 99999999:
			print error_agent_amount
			return None
		elif int(deposit_val) < 0:
			print error_amount_type
			return None
		else:
			print "Deposit Successful"
			return "01_" + account_num + "_000000_" + deposit_val + "_               "

	else:
		if int(deposit_val) > 100000:
			print error_retail_amount
			return None
		elif int(deposit_val) < 0:
			print error_amount_type
			return None
		else:
			print "Deposit Successful"
			return "01_" + account_num + "_000000_" + deposit_val + "_               "
	return None

def withdraw():	
	print prompt_valid_account_num
	account_num = raw_input()
	if (checkAccountNum(account_num)):
		while (len(account_num) < 6):
			account_num = "0" + account_num
	else:
		return None
	print prompt_withdraw
	withdraw_val = raw_input()
	try:
		int(withdraw_val)
	except ValueError:
		print error_amount_type
		return None
	if Agent:
		if int(withdraw_val) > 99999999:
			print error_agent_amount
			return None
		elif int(withdraw_val) < 0:
			print error_amount_type
			return None
		else:
			print "Withdraw Successful"
			return "02_" + "_000000_" + account_num + "_" +withdraw_val + "_               "
	else:
		if int(withdraw_val) > 100000:
			print error_retail_amount
			return None
		elif int(withdraw_val) < 0:
			print error_amount_type
			return None
		else:
			print "Withdraw Successful"
			return "02_" + "_000000_" + account_num + "_" +withdraw_val + "_               "
	return None
def transfer():	
	print prompt_transfer_from
	account_num_from = raw_input()
	if (checkAccountNum(account_num_from)):
		while (len(account_num_from) < 6):
			account_num_from = "0" + account_num_from
	else:
		return None
	print prompt_transfer_to
	account_num_to = raw_input()
	if (checkAccountNum(account_num_to)):
		while (len(account_num_to) < 6):
			account_num_to = "0" + account_num_to
	else:
		return None
	print prompt_transfer
	transfer_val = raw_input()
	try:
		int(transfer_val)
	except ValueError:
		print error_amount_type
		return None
	if Agent:
		if int(transfer_val) > 99999999:
			print error_agent_amount
			return None
		elif int(transfer_val) < 0:
			print error_amount_type
			return None
		else:
			print "Transfer Successful"
			return "03_" + account_num_from + "_" + account_num_to + "_" + transfer_val + "_               "
	else:
		if int(transfer_val) > 100000:
			print error_retail_amount
			return None
		elif int(transfer_val) < 0:
			print error_amount_type
			return None
		else:
			print "Transfer Successful"
			return "03_" + account_num_from + "_" + account_num_to + "_" + transfer_val + "_               "
	return None
	
#Main Execution\
while (Running):
	while (Loggedin == False):
		print prompt_login
		log = raw_input()
		while (log == 'Login' or log == 'login'):
			print prompt_retail_agent
			user_type = raw_input()
			if (user_type == 'Agent' or user_type == 'agent'):
				Loggedin = True
				Agent = True
				log = None
			elif (user_type == 'Retail' or user_type == 'retail'):
				Loggedin = True
				Agent = False
				log = None
			else:
				None
	while (Loggedin == True):
		print prompt_command
		com = raw_input()
		if (com == 'Deposit' or com == 'deposit'):
			summary = deposit()
			if (summary == None):
				None
			else:
				temp_transaction_summary.append(summary)
				summary = None
		elif(com == 'Withdraw' or com == 'withdraw'):
			summary = withdraw()
			if (summary == None):
				None
			else:
				temp_transaction_summary.append(summary)
				summary = None
		elif(com == 'Transfer' or com == 'transfer'):
			summary = transfer()
			if (summary == None):
				None
			else:
				temp_transaction_summary.append(summary)
				summary = None
		elif(com == 'Create' or com == 'create'):
			create()	
		elif(com == 'Delete' or com == 'delete'):
			delete()	
		elif(com == 'Logout' or com == 'logout'):
			Loggedin = False
			print temp_transaction_summary
		else:
			None
	print prompt_finish
	quit = raw_input()
	if (quit == 'Quit' or quit == 'quit'):
		Running = False
	else:
		None
