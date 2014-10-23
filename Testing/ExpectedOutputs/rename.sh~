for file in ap_cr_num_big.txt ap_cr_num_dec.txt ap_cr_num_neg.txt ap_cr_num_str.txt ap_cr_num_xst.txt ap_cr_num_zer.txt ap_dl_nam_big.txt ap_dl_num_dec.txt ap_dl_num_neg.txt ap_dl_num_str.txt ap_dl_num_zer.txt ap_dp_amt_big.txt ap_dp_amt_dec.txt ap_dp_amt_neg.txt ap_dp_amt_str.txt ap_dp_amt_zer.txt ap_dp_dne.txt ap_dp_num_big.txt ap_dp_num_dec.txt ap_dp_num_neg.txt ap_dp_num_str.txt ap_dp_num_zer.txt ap_lo_cor.txt ap_tr_amt_big.txt ap_tr_amt_dec.txt ap_tr_amt_neg.txt ap_tr_amt_str.txt ap_tr_amt_zer.txt ap_tr_num_big.txt ap_tr_num_dec.txt ap_tr_num_dne.txt ap_tr_num_neg.txt ap_tr_num_str.txt ap_tr_num_zer.txt ap_tr_num2_big.txt ap_tr_num2_dec.txt ap_tr_num2_dne.txt ap_tr_num2_neg.txt ap_tr_num2_str.txt ap_tr_num2_zer.txt ap_tr_sam.txt ap_wd_amt_big.txt ap_wd_amt_dec.txt ap_wd_amt_neg.txt ap_wd_amt_str.txt ap_wd_amt_zer.txt ap_wd_dne.txt ap_wd_num_big.txt ap_wd_num_dec.txt ap_wd_num_neg.txt ap_wd_num_str.txt ap_wd_num_zer.txt general_double_login.txt general_login_quit.txt general_login_while_logged_in.txt general_login_while_logged_in.txt general_no_login.txt general_quit_early.txt rp_cr.txt rp_dp_dec.txt rp_dp_inv.txt rp_dp_neg.txt rp_dp_oos.txt rp_dp_qut.txt rp_dp_str.txt rp_dp_zer.txt rp_dt.txt rp_tr_dec.txt rp_tr_ivf.txt rp_tr_ivt.txt rp_tr_lng.txt rp_tr_neg.txt rp_tr_oos.txt rp_tr_qut.txt rp_tr_str.txt rp_tr_zer.txt rp_wd_dec.txt rp_wd_inv.txt rp_wd_lng.txt rp_wd_lng.txt rp_wd_neg.txt rp_wd_oos.txt rp_wd_qut.txt rp_wd_str.txt rp_wd_zer.txt ap_dl_num_big.txt
do
	cp empty.txt $file
done

for file in ao_*
do
	mv "$file" "${file/ao_/a_}"
done

for file in ro_*
do
	mv "$file" "${file/ro_/r_}"
done

for file in ap_*
do
	mv "$file" "${file/ap_/a_}"
done

for file in rp_*
do
	mv "$file" "${file/rp_/r_}"
done
