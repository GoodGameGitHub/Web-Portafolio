curl -X POST https://api.twilio.com/2010-04-01/Accounts/AC5c1d22ac7b06177c12d0b48ac7f4c74d/Messages.json  \
	--data-urlencode "Body=IP pública:${public_ip}" \
	--data-urlencode "From=+12727700339" \
	--data-urlencode "To=+528129025264"  \
	-u AC5c1d22ac7b06177c12d0b48ac7f4c74d:07dee28eae39175b639fa763496c5674


