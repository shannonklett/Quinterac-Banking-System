cp ap_dp_amt_big.txt ap_tr_amt_big.txt
cp ap_dp_amt_dec.txt ap_tr_amt_dec.txt
cp ap_dp_amt_neg.txt ap_tr_amt_neg.txt
cp ap_dp_amt_sml.txt ap_tr_amt_sml.txt
cp ap_dp_amt_str.txt ap_tr_amt_str.txt
cp ap_dp_amt.txt ap_tr_amt.txt 
cp ap_dp_amt_zer.txt ap_tr_amt_zer.txt
cp ap_dp_dne.txt ap_tr_dne.txt
cp ap_dp_num_big.txt ap_tr_num_big.txt
cp ap_dp_num_dec.txt ap_tr_num_dec.txt
cp ap_dp_num_neg.txt ap_tr_num_neg.txt
cp ap_dp_num_sml.txt ap_tr_num_sml.txt
cp ap_dp_num_str.txt ap_tr_num_str.txt
cp ap_dp_num.txt ap_tr_num.txt
cp ap_dp_num_zer.txt ap_tr_num_zer.txt
cp ap_dp_qui.txt ap_tr_qui.txt
cp ap_dp_xct.txt ap_tr_xct.txt

sed -i 's/deposit/transfer/g' ap_tr*

