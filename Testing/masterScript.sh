DATE=$(date +'%m-%d:%H:%M:%S')
mkdir TestOutputs/$DATE
mkdir TestPrompts/$DATE

while read test; do
	printf "running test $test\n"
	python ../front_end_modified.py ValidAccounts/$test TestOutputs/$DATE/$test < Auto_Inputs/$test > TestPrompts/$DATE/$test
	
	printf "\nchecking output of test $test\n"
	diff -b TestOutputs/$DATE/$test ExpectedOutputs/$test
	diff -b TestPrompts/$DATE/$test ExpectedPrompts/$test
done <inputFiles.txt


