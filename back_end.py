'''
CISC 327 Assignment 4
TEAM GLOBEX 
NEVEN GOLUBOVICH 10062175
SHANNON KLETT 10065230
'''

#Dictionary based on the Master account file
Master_Accounts_Dic = {}

'''
Takes in the Master account file
reads it line by line
creates a dictionary of accounts in the form of {account_number:(balance, name)}
'''
def read_master_account_file(filename):
	global Master_Accounts_Dic
	Master_Accounts_File = open(filename,'r')
	for line in Master_Accounts_File:
		line = line.split()
		#While not at EOF
		if len(line) > 0:
			#line[0] is the account number
			#line[1] is the account balance
			#line[2] is the account name
			Master_Accounts_Dic[(line[0])] = (line[1],line[2])

'''
Takes the MasterAccount file, and Valid account file
Prints to each one, the updated account information
Sorted in acending numerical order on Account numbers
'''
def write_account_files(masterfile, validfile):
	global Master_Accounts_Dic
	#gets a list of all the accounts currently in the dictonary
	#that is accounts that were not deleted/have been created
	Key_List = list(Master_Accounts_Dic.keys())
	#sorts the list of numbers
	Key_List.sort()
	New_Master_Accounts_File = open(masterfile, 'w+')
	New_Valid_Accounts_File = open(validfile,'w+')
	for account_number in Key_List:
		#Print to the new masters account file, "'number' 'balance' 'name'"
		balance = str(get_balance(account_number)).rjust(8, "0")
		name = get_name(account_number).ljust(15)
		New_Master_Accounts_File.write(account_number + " " + balance + " " + name + "\n")
		#Prints account numbers to the new valid accounts file
		New_Valid_Accounts_File.write(account_number + "\n")
	New_Valid_Accounts_File.write("000000")

'''
Given account number, returns current balance 
'''
def get_balance(accountnumber):
	return int(Master_Accounts_Dic[accountnumber][0])

'''
Given account number, returns corresponding account name
'''
def get_name(accountnumber):
	return Master_Accounts_Dic[accountnumber][1]

'''
Modifies the current balance of an account
It takes the current balance, and the amount 
being taken or added to the account as parameters
It either returns the current balance, or an updated balance
'''
def update_balance(currentbalance,transactionvalue):
	#If the transaction would cause a negative balance, reject it
	if (currentbalance + transactionvalue) < 0:
		print "Account was left with a negative balance from transaction"
		return currentbalance
	#If the transaction would cause an overflow balance, reject it
	elif (currentbalance + transactionvalue) > 99999999:
		print "Account was left with a balance too large to process"
		return currentbalance
	#Otherwise, return the balance as it would appear after the transaction
	else:
		return (currentbalance + transactionvalue)

'''
Adds an account to the master accounts dictionary
'''
def create_account(accountnumber,accountname):
	#If statement ensures we are not overwritting an existing account
	if accountnumber not in Master_Accounts_Dic.keys():
		Master_Accounts_Dic[accountnumber] = (0,accountname)
	else:
		print "The account already exists"

'''
Removes an existing account from the master accounts dictionary.
Checks if account name and number match, and if balance is 0.
'''
def delete_account(accountnumber,accountname):
	#Checks that the name of the account is the same as given
	if get_name(accountnumber) == accountname:
		#Ensures the account is at a 0 balance
		if get_balance(accountnumber) == 0:
			#If both conditions are met, delete the account from the dictionary
			del Master_Accounts_Dic[accountnumber]
		else:
			print "Account balance was not 0"
	else:
		print "Account name was invalid"

'''
MAIN PROGRAM:
Purpose: Implemenation of the back end of Quinterac. 
Processes transactions and maintains account information.
Implemenation:
Initially this program reads in the master account file, and stores 
information in a dictionary. Entries are in the form {account_number: (balance, name)}. 
Then it reads in the transaction log for a days transactions. 
For each transaction completed, the program determines which transaction type 
is being completed and then reflects the change in the masters account dictionary. 
Finally, a call is made to write the new Masters Account file and the new Valid Accounts file
'''

#Calls the method to create the Account dictionary
read_master_account_file("masterAccount.txt")

#Begins the process of reading in a days transaction log
Transaction_List = open("transactionfile.txt",'r')

#For each transaction in the log
for line in Transaction_List:

	#The type of action performed
	action = line[0:2]
	#The account a transaction happens to
	to_account = line[3:9]
	#If money is being taken from an account, it is from this account
	from_account = line[10:16]
	#The amount of money being enacted on the account
	transaction_amount = int(line[17:25])
	#The name of the account
	account_name = line[26:41]

	#If deposit
	if action == "01":
		new_balance = update_balance(get_balance(to_account),transaction_amount)
		Master_Accounts_Dic[to_account] = (str(new_balance),get_name(to_account))
	#If withdraw
	elif action == "02":
		new_balance = update_balance(get_balance(from_account),-transaction_amount)
		Master_Accounts_Dic[from_account] = (str(new_balance),get_name(from_account))
	#If transfer
	elif action == "03":
		new_balance_from = update_balance(get_balance(from_account),-transaction_amount)
		#If taking the money out of the first account was succesful
		#Then continue the transaction
		if new_balance_from != get_balance(from_account):
			Master_Accounts_Dic[from_account] = (str(new_balance_from),get_name(from_account))
			new_balance_to = update_balance(get_balance(to_account),transaction_amount)
			Master_Accounts_Dic[to_account] = (str(new_balance_to),get_name(from_account))
	#If create
	elif action == "04":
		create_account(to_account,account_name)
	#If delete
	elif action == "05":
		delete_account(to_account,account_name)
	elif action == "00":
		None
	else:
		print "Error: Invalid Input"
		print line

#writes out the new masters account file and new valid accounts list
write_account_files("masterAccount2.txt","output.txt")

