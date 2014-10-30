DATE=$(date +'%m-%d:%H:%M:%S') #used to differentiate each test run
mkdir TestOutputs/$DATE
mkdir TestPrompts/$DATE

while read test; do
	#run test
	printf "running test $test\n"
	#Take account list from ValidAccounts (000001, 000002, etc
	#Output transaction summary to TestOutputs (01 0000001..., etc)
	#Read commands from Auto_Inputs (login, agent, etc.)
	#Output prompts to TestPrompts (Enter 'login', etc.) 
	python ../front_end_modified.py ValidAccounts/$test TestOutputs/$DATE/$test < Auto_Inputs/$test > TestPrompts/$DATE/$test
	
	#check against expected output file and prompts
	printf "checking output of test $test\n"
	diff -b TestOutputs/$DATE/$test ExpectedOutputs/$test
	diff -b TestPrompts/$DATE/$test ExpectedPrompts/$test
	printf "\n\n"

done <inputFiles.txt #list of all test cases in proper order


