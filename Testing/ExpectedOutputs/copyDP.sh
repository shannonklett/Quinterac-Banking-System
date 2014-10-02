cp ao_dp_amt_sml.txt ao_wd_amt_sml.txt
cp ao_dp_num_sml.txt ao_wd_num_sml.txt
cp ao_dp_xct.txt ao_wd_xct.txt

sed -i 's/01/02/g' ao_wd*
sed -i 's/002/001/g' ao_wd*
