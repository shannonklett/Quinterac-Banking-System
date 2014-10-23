while read test; do
	echo "running test $test"
	python ../front_end.py ValidAccounts/$test TestOutputs/$test < TestInputs/$test > TestPrompts/$test
	
	echo "\nchecking output of test $test"
	diff TestOutputs/$test ExpectedOutputs/$test
	diff TestPrompts/$test ExpectedPrompts/$test
done <inputFiles1.txt


