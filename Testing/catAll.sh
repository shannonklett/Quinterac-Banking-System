#echo "Inputs:"

for FILE in Inputs/*.txt
do
echo -e "$FILE\n" 
cat $FILE 
echo -e "\n"
done

#echo "Expected Prompts:"

for FILE in ExpectedPrompts/*.txt
do
echo -e "$FILE\n" 
cat $FILE 
echo -e "\n"
done

#echo "Expected Outputs:"

for FILE in ExpectedOutputs/*.txt
do
echo -e "$FILE\n" 
cat $FILE 
echo -e "\n"
done



