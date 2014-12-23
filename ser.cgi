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

if ! [ -f /tmp/isrunning ]; then
        /www/cgi-bin/readuino.sh & 2>&1 >/dev/null
fi

echo "<pre>



</pre>"

echo "<font size=24><pre>"
echo -n "$cmd" > /dev/ttyUSB0
echo "$(cat /tmp/volts)"
echo "</pre></font></html>"
echo ""
#echo "<br/>"
#resp="$(head -c 30 /dev/ttyUSB0)"
#echo "v: $resp e"
#echo "Serial settings: "
#SERIAL_SETTINGS="$(stty -F /dev/ttyUSB0 -a)"
#echo "$SERIAL_SETTINGS"

#echo "<br/>"
#echo "end"
