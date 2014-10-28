for file in ap_*
do
	mv "$file" "${file/ap_/a_}"
done

for file in rp_*
do
	mv "$file" "${file/rp_/r_}"
done
