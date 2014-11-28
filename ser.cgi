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

#echo "<br/>"
#echo "Serial settings: "
#SERIAL_SETTINGS="$(stty -F /dev/ttyUSB0 -a)"
#echo "$SERIAL_SETTINGS"

echo "<br/>"
echo "end"
