cp ap_dp_amt_big.txt ap_wd_amt_big.txt
cp ap_dp_amt_dec.txt ap_wd_amt_dec.txt
cp ap_dp_amt_neg.txt ap_wd_amt_neg.txt
cp ap_dp_amt_sml.txt ap_wd_amt_sml.txt
cp ap_dp_amt_str.txt ap_wd_amt_str.txt
cp ap_dp_amt.txt ap_wd_amt.txt 
cp ap_dp_amt_zer.txt ap_wd_amt_zer.txt
cp ap_dp_dne.txt ap_wd_dne.txt
cp ap_dp_num_big.txt ap_wd_num_big.txt
cp ap_dp_num_dec.txt ap_wd_num_dec.txt
cp ap_dp_num_neg.txt ap_wd_num_neg.txt
cp ap_dp_num_sml.txt ap_wd_num_sml.txt
cp ap_dp_num_str.txt ap_wd_num_str.txt
cp ap_dp_num.txt ap_wd_num.txt
cp ap_dp_num_zer.txt ap_wd_num_zer.txt
cp ap_dp_qui.txt ap_wd_qui.txt
cp ap_dp_xct.txt ap_wd_xct.txt

sed -i 's/deposit/withdraw/g' ap_wd*
