cp ao_dp_amt_sml.txt ao_tr_amt_sml.txt
cp ao_dp_num_sml.txt ao_tr_num_sml.txt
cp ao_dp_xct.txt ao_tr_xct.txt

sed -i 's/01/03/g' ao_tr*
sed -i 's/003/001/g' ao_tr*
