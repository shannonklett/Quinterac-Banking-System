#full deposit output
DEP_FULL=ap_dp_amt.txt

for LABEL in ap_dp_xct.txt ap_dp_num_sml.txt ap_dp_amt_sml.txt
do
	cp "$DEP_FULL" "$LABEL"
done

#Command, valid num, error 1-6 digits, command
NUM_ERROR=ap_dl_num_neg.txt

for LABEL in ap_dp_num_dec.txt
do
	cp "$NUM_ERROR" "$LABEL"
done

#Command, num, dne, command
DNE=ap_dl_num_zer.txt

for LABEL in ap_dp_num_zer.txt
do
	cp "$DNE" "$LABEL"
done

#Command, num, amt, cents >0, command
AMT_ERROR=ap_dp_amt_str.txt

for LABEL in ap_dp_amt_dec.txt ap_dp_amt_neg.txt ap_dp_amt_zer.txt
do
	cp "$AMT_ERROR" "$LABEL"
done

#full create output
CR_FULL=ap_cr_nam.txt

for LABEL in ap_cr_num_sml.txt ap_cr_nam_sml.txt ap_cr_nam_big.txt ap_cr_nam_int.txt
do
	cp "$CR_FULL" "$LABEL"
done

#command, new num, error 1-6 digits, command
NEW_NUM_ERROR=ap_cr_num_big.txt

for LABEL in ap_cr_num_str.txt ap_cr_num_neg.txt ap_cr_num_dec.txt
do
	cp "$NEW_NUM_ERROR" "$LABEL"
done
