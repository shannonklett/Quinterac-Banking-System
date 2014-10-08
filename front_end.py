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

#TO PAD SPACES use "hey".ljust(15)

Loggedin = False
Agent = False
Running = True

def create():
	return
	
def deposit():	
	print prompt_valid_account_num
	account_num = raw_input()
	print prompt_deposit
	deposit_val = raw_input()
	if Agent:
		if deposit_val > 99999999:
			print error_agent_amount
		else:
			print "Deposit Successful"
	else:
		if deposit_val > 100000:
			print error_retail_amount
		else:
			print "Deposit Successful"

	
	return 
	

def transfer():	
	print prompt_transfer_from
	account_num_from = raw_input()
	print prompt_transfer_to
	account_num_to = raw_input()
	print prompt_transfer
	transfer_val = raw_input()
	if Agent:
		if transfer_val > 99999999:
			print error_agent_amount
		else:
			print "Transfer Successful"
	else:
		if tranfer_val > 100000:
			print error_retail_amount
		else:
			print "Transfer Successful"
	return

def withdraw():	
	print prompt_valid_account_num
	account_num = raw_input()
	print prompt_deposit
	transfer_val = raw_input()
	if Agent:
		if withdraw_val > 99999999:
			print error_agent_amount
		else:
			print "Withdraw Successful"
	else:
		if withdraw_val > 100000:
			print error_retail_amount
		else:
			print "Withdraw Successful"
	return 
	
#Main Execution\
while (Running):
	while (Loggedin == False):
		print prompt_login
		log = raw_input()
		if (log == 'Agent' or log == 'Agent'):
			Loggedin = True
			Agent = True
		elif (log == 'Retail' or log == 'retail'):
			Loggedin = True
			Agent = False
		else:
			None
	while (Loggedin == True):
		print prompt_command
		com = raw_input()
		if (com == 'Deposit' or com == 'deposit'):
			deposit()
		elif(com == 'Withdraw' or com == 'withdraw'):
			withdraw()
		elif(com == 'Transfer' or com == 'transfer'):
			transfer()
		elif(com == 'Logout' or com == 'logout'):
			Loggedin = False
		else:
			None			
	Running = False
