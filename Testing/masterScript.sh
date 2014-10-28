while read test; do
	echo "running test $test"
	DATE=$(date +'%m-%d:%H:%M')
	echo $DATE
	echo python ../front_end.py ValidAccounts/$test TestOutputs/$DATE/$test < Auto_Inputs/$test > TestPrompts/$DATE/$test
	
	echo "\nchecking output of test $test"
	diff TestOutputs/$DATE/$test ExpectedOutputs/$test
	diff TestPrompts/$DATE/$test ExpectedPrompts/$test
done <inputFiles.txt


