'''
GLOBAL PROMPTS
'''
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

'''
GLOBAL ERROR PROMPTS
'''
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

'''
GLOBAL VARIABLES
'''
Loggedin = False
Agent = False
Running = True
temp_transaction_summary = [] #list of 41 character strings
account_list = [] #list of valid accounts numbers (in integer form)

'''
READ/WRITE FILE FUNCTIONS
'''

#creates list of valid accounts contained in file	
#Parameters: (String) filename: the complete name of the file containing the valid accounts list	
#Return Value: (int List) accounts: list of account numbers contained in the file
def readAccountFile(filename):
	#for each line in file, remove newline and convert number to an int
	accounts = [int(line.strip()) for line in open(filename)]
	return accounts

#writes transactions to the file Testing/Temp/output.txt
#Parameters: (String List) transactions: list of transaction strings from current session
#Return Value: None
def writeTransactionFile(transactions):
	f=open('Testing/Temp/output.txt', 'w+')
	for item in transactions:
		f.write("%s\n" % item) #write transaction string followed by newline
	f.write("%s" % makeTransactionString()) #end file with "00 000000 000000 0000000                "	
	f.close()
	return

#creates a 41 character transaction string in the form of "AA BBBBBB CCCCCC DDDDDDDD NNNNNNNNNNNNNNN". 
#Pads spaces and 0s as needed and uses default values if necessary.
#Parameters: (int) type: number in range 1-5 indicating transaction type
#(int) account1: account number of the "to" account
#(int) account2: account number of the "from" account
#(int) amount: value in cents of transaction
#(String) name: account name
#Return Value: (String) correctly formatted transaction string	
def makeTransactionString(type=00, account1=000000, account2=000000, amount=00000000, name=""):
	#pad 0s at beginning
	type = str(type).rjust(2, "0")
	account1 = str(account1).rjust(6, "0")
	account2 = str(account2).rjust(6, "0")
	amount = str(amount).rjust(8, "0")
	#pad spaces at end
	name = name.ljust(15)
	return "%s %s %s %s %s" %(type, account1, account2, amount, name)	

'''
INPUT CHECKING FUNCTIONS
'''

#checks if given account number is in the valid accounts list
#Parameters: (int) num: account number
#Return Value: (bool) true if  number is in valid accounts file
def checkAccountExists(num):
	return num in account_list

#checks user inputted account number to see if it is a 6 or less digit integer greater than 0. 
#If createMode is true, checks that account doesn't exist, otherwise checks that it does
#Parameters: (String) num: user inputted account number
#(bool) createMode: true if function called from create() method
#Return Value: (bool) true if account number is acceptable
def checkAccountNum(num, createMode=False):
	try:
		num = int(num)
	except ValueError:
		print error_account_num #must be 1-6 digits
		return False	
	if num>999999: 
		print error_account_num #must be 1-6 digits
	elif num<1:
		print error_account_neg #must be greater than 0
	elif not createMode and not checkAccountExists(num):
		#attempting to access account that doesn't exist
		print error_account_dne		
	elif createMode and checkAccountExists(num):
		#creating account that already exists
		print error_account_exists
	else:
		return True
	return False #error occured

#checks user inputted account number to see it is a string with 1-15 characters
#Parameters: (String) name: user inputted account number
#Return Value: (bool) true if account name is acceptable
def checkAccountName(name):
	if len(name)>15 or len(name)<1:
		print error_account_nam
	else:
		return True
	return False #error occured

#checks user inputted amount to ensure it is between 1 and 100000000 for Agent or 1 and 100001 for retail
#Parameters: (String) amount: user inputted amount
#Return Value: (bool) true if amount is acceptable
def checkAmount(val):
	if int(val) < 0:
		print error_amount_type #must be entered in cents and greater than 0
		return False
	if Agent and int(val) > 99999999:
		print error_agent_amount #transaction above $999,999.99 not accepted
		return False
	elif not Agent and int(val) > 100000:
		print error_retail_amount  #transaction above $1,000.00 not accepted
		return False
	#no errors found, return True	
	return True

'''
ACCOUNT CHANGING FUNCTIONS
'''

#checks if user is an agent or retail. If agent, then the user is asked to input a new account number, and new name. 
#This information will be used by the back-end to create a new account on file. If the user is a retail user, then an error is printed.
#Parameters: None
#Return Value: (String) formatted 41 character transaction string
def create():
	if Agent:
		#prompt for new account number
		print prompt_new_account_num
		account_num = raw_input()
		#check if input is valid
		if checkAccountNum(account_num, True):
			#prompt for new account name
			print prompt_new_account_nam
			account_name = raw_input()
			#check if input is valid
			if checkAccountName(account_name):
				#all inputs have been validated, return transaction string
				return makeTransactionString(4, account_num, name=account_name)
	else:	#retail mode
		print error_permission
	return None #error occured

#checks if user is an agent or retail. If agent, then the user is asked to input an existing account number, and name. 
#This information is used to remove account from valid accounts list and later by the back-end to delete an account on file. 
#If the user is a retail user, then an error is printed.
#Parameters: None
#Return Value: (String) formatted 41 character transaction string	
def delete():
	if Agent:
		#prompt for valid account number
		print prompt_valid_account_num
		account_num = raw_input()
		#check if input is valid
		if checkAccountNum(account_num):
			#prompt for valid account name
			print prompt_valid_account_nam
			account_name = raw_input()
			#check if input is valid
			if checkAccountName(account_name):
				#all inputs have been validated
				account_list.remove(int(account_num)) #prevents further transactions on account
				#return transaction string
				return makeTransactionString(5, account_num, name=account_name)	
	else:	#retail mode
		print error_permission
	return None #error occured	

'''
TRANSACTION FUNCTIONS
'''

#Deposit is called as result of a user input in the Main loop.
#Prompts the user to enter the number of the account they wish to interact with,
#followed by a value to be deposited into the requested account.
#Parameters: None
#Return Value: (String) formatted 41 character transaction string
def deposit():	
	#Requests the user to input a valid account number to deposit to
	print prompt_valid_account_num
	account_num = raw_input()
	#Passes the input account number to a function which checks its validity
	if (checkAccountNum(account_num) == False):
		return None
	#Prompts the user for an amount to deposit
	print prompt_deposit
	deposit_val = raw_input()
	#Checks that the value was an intager
	try:
		int(deposit_val)
	#Rejects non-numerical, negative and decimal numbers
	except ValueError:
		print error_amount_type
		return None
	#Passes the deposit value to a function which checks its validity
	#Specifically checking if it is within the range allowable for Agent/Retail
	if(checkAmount(deposit_val)):
		print "Deposit Successful"
		#Returns a string in the format of
		#CC_AAAAAA_BBBBBB_MMMMMMMM_NNNNNNNNNNNNNNN
		#By calling makeTransactionString and passing appropriate parameters
		return makeTransactionString(1, account_num, amount = deposit_val)
	else:
		return None
	return None

#Withdraw is called as a result of user input in the Main loop.
#Prompts the user to enter the number of the account they wish to interact with,
#followed by a value to be withdrawn from the requested account.
#Parameters: None
#Return Value: (String) formatted 41 character transaction string
def withdraw():	
	#Requests the user to input a valid account number to withdraw from
	print prompt_valid_account_num
	account_num = raw_input()
	#Passes the input account number to a function which checks its validity
	if (checkAccountNum(account_num) == False):
		return None
	#Requests the user for an amount to withdraw
	print prompt_withdraw
	withdraw_val = raw_input()
	#Checks that the value was an intager
	try:
		int(withdraw_val)
	#Rejects non-numerical, negative and decimal numbers
	except ValueError:
		print error_amount_type
		return None
	#Passes the trasfer value is passed to a function which checks its validity
	#Specifically checking if it is within the range allowable for Agent/Retail
	if (checkAmount(withdraw_val)):
		print "Withdraw Successful"
		#Returns a string in the format of
		#CC_AAAAAA_BBBBBB_MMMMMMMM_NNNNNNNNNNNNNNN
		#By calling makeTransactionString and passing appropriate parameters
		return makeTransactionString(2, account2 = account_num, amount = withdraw_val)
	else:
		return None
	return None

#Transfer is called as a result of user input in the Main loop.
#Prompts the user to enter the numbers of two accounts they wish to interact with,
#followed by a value to be transferred between the requested accounts.
#Parameters: None
#Return Value: (String) formatted 41 character transaction string
def transfer():	
	#Requests the user to input a valid account number to transfer from
	print prompt_transfer_from
	account_num_from = raw_input()
	#Passes the input account number to a function which checks its validity
	if (checkAccountNum(account_num_from) == False):
		return None
	#Requests the user to input a valid account number to transfer to
	print prompt_transfer_to
	account_num_to = raw_input()
	#Passes the input account number to a function which checks its validity
	if (checkAccountNum(account_num_to) == False):
		return None
	#Requests the user for an amount to transfer
	print prompt_transfer
	transfer_val = raw_input()
	#Checks that the value was an intager
	try:
		int(transfer_val)
	#Rejects non-numerical, negative and decimal numbers
	except ValueError:
		print error_amount_type
		return None
	#Passes the trasfer value is passed to a function which checks its validity
	#Specifically checking if it is within the range allowable for Agent/Retail
	if (checkAmount(transfer_val)):
		print "Transfer Successful"
		#Returns a string in the format of
		#CC_AAAAAA_BBBBBB_MMMMMMMM_NNNNNNNNNNNNNNN
		#By calling makeTransactionString and passing appropriate parameters
		return makeTransactionString(3, account_num_to, account_num_from, transfer_val)
	else:
		return None
	return None

'''
MAIN PROGRAM
'''

#Main begins by reading and saving a copy of the accounts list
#when the program is initiated.
#It then enters a loop which requests the user to input "Login" to begin.
#When the user has done so, it then requests if the user is in agent or retail mode.
#Once determined, main enters its second loop,
#which prompts the user for valid operations.
#The operations are named for the Account changing, Transaction, and logout functions.
#Entering the proper input, such as "create" will call that function.
#Logout is not actually calling a function however,
#as logging out is simply breaking the loop condition.
#Upon return from a function, Main will take the transaction string
#returned and store it in a temporary transaction list.
#Should the user logout, this temporary transaction list is copied 
#over to a transaction summary file. 

#An additional, outer, loop is currently being used.
#This is a loop that allows the user to keep the program running after logging out.
#This was implemented for manual testing during development,
#and will not be implemented in the final product.

#Running is the first loop condition, this was implemented to allow users to
#log back in without having to rerun the program each time. This has been implemented
#for manual testing of code during development and will not be featured
#in the final product.
while (Running):
	#Loggedin is parameter for Main's first major loop.
	#It checks if the user is actually succeded in logging in or not
	#and by extension, what kind of inputs are currently accepted
	while (Loggedin == False):
		#Informs the user what they need to do to login
		print prompt_login
		loginInput = raw_input().lower()
		while (loginInput == 'login'):
			#Requests what kind of account the user will use
			#Agent, or Retail?
			print prompt_retail_agent
			user_type = raw_input().lower()
			#if statement reads the user response, and sets Global variables
			#which are used to determine what commands the user can use later.
			if (user_type == 'agent'):
				Loggedin = True
				Agent = True
				loginInput = None
			elif (user_type == 'retail'):
				Loggedin = True
				Agent = False
				loginInput = None
	#user is now logged in			
	
	#read in a valid accounts file and turns it into a list for use by program
	account_list = readAccountFile('Testing/Inputs/accountList_1_2.txt')
						
	#The second loop 
	while (Loggedin == True):
		#Asks the user for a valid command
		print prompt_command
		commandInput = raw_input().lower()
		#If statement reads the users input and calls the appropriate
		#Function if possible.
		if (commandInput == 'deposit'):
			#Takes the String returned by deposit() and stores it in summary
			summary = deposit()
			#If deposit() was succesful, than the transaction summary string
			#will be stored in a temporary list of the day's transactions.
			if (summary != None):
				temp_transaction_summary.append(summary)
		#elif statements are functionally equivalent to if (commandInput == 'deposit')
		elif(commandInput == 'withdraw'):
			summary = withdraw()
			if (summary != None):
				temp_transaction_summary.append(summary)
		elif(commandInput == 'transfer'):
			summary = transfer()
			if (summary != None):
				temp_transaction_summary.append(summary)
		elif(commandInput == 'create'):
			summary = create()	
			if (summary != None):
				temp_transaction_summary.append(summary)
		elif(commandInput == 'delete'):
			summary = delete()
			if (summary != None):
				temp_transaction_summary.append(summary)
		#Logout is an additional input accepted.
		#If the user uses this input, than the Loggedin loop is broken.
		elif(commandInput == 'logout'):
			Loggedin = False
			#write to the Transaction Summary File (Testing/Temp/output.txt)
			writeTransactionFile(temp_transaction_summary)
	#After logging out, the users is asked if they want to terminate the program
	#Again, this is a temporary feature, and is not intended to be included
	#in the final iteration of this project.		
	print prompt_finish
	quit = raw_input().lower()
	if (quit == 'quit'):
		Running = False
