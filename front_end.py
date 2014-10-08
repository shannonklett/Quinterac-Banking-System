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

def create():
	return
	
def deposit():	
	print prompt_valid_account_num
	account_num = input()
	
	return 
	
#Main Execution
print prompt_login
print "heyy".ljust(15)+"boo"
deposit()