#!/bin/bash
#
# CGI-script, (c) Copyright
#
# Start with outputting the HTTP headers.
#

echo "Content-type: text/html"
echo ""

#
# Start HTML content.
#

echo "$QUERY_STRING"
echo "<br/>"
cmd=${QUERY_STRING%%&*}
echo "$cmd"
echo "<br/>"

echo -n "$cmd" > /dev/ttyUSB0

#while [ 1 ]; do
#	if  ! [ -f /var/ardresprunning ]; then	 
#		break;
#	fi
#done
#echo "infoStr: $(cat /var/ardresp)"
#rm /var/ardresp
echo ""
