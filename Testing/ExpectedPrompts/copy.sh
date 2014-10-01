#full deposit output
DEP_FULL=ap_dp_amt.txt
#Command, num, error 1-6 digits, command
NUM_ERROR=ap_dl_num_neg.txt
#Command, num, dne, command
DNE=ap_dl_num_zer.txt
#Command, num, amt, cents >0, command
AMT_ERROR=ap_dp_amt_str.txt

for LABEL in ap_dp_xct.txt ap_dp_num_sml.txt
do
	cp "$DEP_FULL" "$LABEL"
done

for LABEL in ap_dp_num_dec.txt
do
	cp "$NUM_ERROR" "$LABEL"
done

for LABEL in ap_dp_num_zer.txt
do
	cp "$DNE" "$LABEL"
done

for LABEL in ap_dp_amt_dec.txt ap_dp_amt_neg.txt ap_dp_amt_zer.txt
do
	cp "$AMT_ERROR" "$LABEL"
done
