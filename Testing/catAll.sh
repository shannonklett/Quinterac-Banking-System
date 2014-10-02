#echo "Expected Outputs:"

for FILE in ExpectedOutputs/*
do
echo -e "$FILE\n" 
cat $FILE 
echo -e "\n"
done

#echo "Expected Prompts:"

for FILE in ExpectedPrompts/*
do
echo -e "$FILE\n" 
cat $FILE 
echo -e "\n"
done

