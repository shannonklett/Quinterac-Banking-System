sed -i 's/Enter a valid account number:/Enter a valid account number to transfer from:/g' ap_tr*

#end after transfer amt (no command prompt)
cp ap_tr_num.txt ap_tr_num2.txt

cp ap_tr_dne.txt ap_tr_num2_dne.txt
cp ap_tr_num_big.txt ap_tr_num2_big.txt
cp ap_tr_num_str.txt ap_tr_num2_str.txt
cp ap_tr_num_neg.txt ap_tr_num2_neg.txt
cp ap_tr_num_dec.txt ap_tr_num2_dec.txt
cp ap_tr_num_zer.txt ap_tr_num2_zer.txt

#Account dne
cp ap_tr_num_zer.txt ap_tr_num_dne.txt

# rm ap_tr_dne.txt

sed -i 's/Enter a valid account number to transfer from:/Enter a valid account number to transfer from:\nEnter a valid account number to transfer to:/g' ap_tr_num2.txt ap_tr_amt.txt ap_tr_num2_dne.txt ap_tr_num2_big.txt ap_tr_num2_str.txt ap_tr_num2_neg.txt ap_tr_num2_dec.txt ap_tr_num2_zer.txt ap_tr_num_sml.txt ap_tr_xct.txt ap_tr_num_sml.txt ap_tr_amt_str.txt ap_tr_amt_dec.txt ap_tr_amt_neg.txt ap_tr_amt_zer.txt ap_tr_amt_big.txt ap_tr_amt_sml.txt



