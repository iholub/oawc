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

#head -n 1 /dev/ttyUSB0 >/tmp/volts &
#bgPid=$!
#echo "pid: $bgPid"
echo -n "$cmd" > /dev/ttyUSB0
#infoStr=$(cat /tmp/volts)
#echo "infoStr: $infoStr"
#kill $bgPid
echo ""
#echo "<br/>"
#resp="$(head -c 30 /dev/ttyUSB0)"
#echo "v: $resp e"
#echo "Serial settings: "
#SERIAL_SETTINGS="$(stty -F /dev/ttyUSB0 -a)"
#echo "$SERIAL_SETTINGS"

#echo "<br/>"
#echo "end"
