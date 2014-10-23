for FILE in ap_tr_num2_big.txt
do
	cp accountList_1_123456.txt $FILE
done

for FILE in ap_tr_xct.txt ap_dl_dep.txt ap_dl_wtd.txt ap_dp_xct.txt ap_dp_num_big.txt ap_wd_xct.txt ap_wd_num_big.txt ap_tr_num_big.txt 
do
	cp accountList_123456_223456.txt $FILE
done

for FILE in ap_dl_xct.txt ap_dl_num_big.txt 
do
	cp accountList_123456.txt $FILE
done

for FILE in rp_tr_cor.txt rp_tr_oos.txt rp_tr_zer.txt rp_tr_dec.txt rp_tr_neg.txt rp_tr_str.txt rp_tr_lng.txt ap_dl_tra.txt ap_tr_num2.txt ap_tr_amt.txt ap_tr_num2_str.txt ap_tr_num2_neg.txt ap_tr_num2_dec.txt ap_tr_num2_zer.txt ap_tr_sam.txt ap_tr_num_sml.txt ap_tr_amt_str.txt ap_tr_amt_dec.txt ap_tr_amt_neg.txt ap_tr_amt_zer.txt ap_tr_amt_big.txt ap_tr_amt_sml.txt 
do
	cp accountList_1_2.txt $FILE
done

for FILE in rp_dp_cor.txt rp_dp_oos.txt rp_dp_zer.txt rp_dp_neg.txt rp_wd_cor.txt rp_wd_oos.txt rp_wd_zer.txt rp_wd_neg.txt rp_tr_ivt.txt rp_dp_dec.txt rp_wd_dec.txt rp_dp_str.txt rp_wd_str.txt rp_wd_lng.txt rp_wd_lng.txt rp_wd_ovr.txt ap_cr_num_xst.txt ap_cr_tra.txt ap_dl_num.txt ap_dl_nam.txt ap_dl_num_sml.txt ap_dl_num_neg.txt ap_dl_num_dec.txt ap_dl_nam_sml.txt ap_dl_nam_big.txt ap_dl_nam_int.txt ap_dp_num.txt ap_dp_amt.txt ap_dp_num_sml.txt ap_dp_num_neg.txt ap_dp_num_dec.txt ap_dp_amt_str.txt ap_dp_amt_dec.txt ap_dp_amt_neg.txt ap_dp_amt_zer.txt ap_dp_amt_big.txt ap_dp_amt_sml.txt ap_wd_num.txt ap_wd_amt.txt ap_wd_num_sml.txt ap_wd_num_neg.txt ap_wd_num_dec.txt ap_wd_amt_str.txt ap_wd_amt_dec.txt ap_wd_amt_neg.txt ap_wd_amt_zer.txt ap_wd_amt_big.txt ap_wd_amt_sml.txt ap_tr_num.txt ap_tr_num_neg.txt ap_tr_num_dec.txt ap_tr_num2_dne.txt 
do
	cp accountList_1.txt $FILE
done

for FILE in rp_cr.txt rp_dt.txt rp_dp_inv.txt rp_dp_out.txt rp_wd_inv.txt rp_wd_out.txt rp_tr_ivf.txt rp_tr_out.txt rp_dp_qut.txt rp_wd_qut.txt rp_tr_qut.txt ap_li_cor.txt ap_lo_cor.txt ap_cr_qui.txt ap_cr_num.txt ap_cr_nam.txt ap_cr_num_xct.txt ap_cr_num_sml.txt ap_cr_num_big.txt ap_cr_num_str.txt ap_cr_num_neg.txt ap_cr_num_dec.txt ap_cr_num_zer.txt ap_cr_nam_sml.txt ap_cr_nam_big.txt ap_cr_nam_int.txt ap_cr_dep.txt ap_cr_wtd.txt ap_dl_qui.txt ap_dl_num_dne.txt ap_dl_num_str.txt ap_dl_num_zer.txt ap_dp_qui.txt ap_dp_dne.txt ap_dp_num_str.txt ap_dp_num_zer.txt ap_wd_qui.txt ap_wd_dne.txt ap_wd_num_str.txt ap_wd_num_zer.txt ap_tr_qui.txt ap_tr_num_dne.txt ap_tr_num_str.txt ap_tr_num_zer.txt general_no_login.txt general_double_login.txt general_login_while_logged_in.txt general_login_while_logged_in.txt general_quit_early.txt general_login_quit.txt
do
	cp accountList_empty.txt $FILE
done

