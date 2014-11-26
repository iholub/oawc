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
echo "$cmd" > /dev/ttyUSB0

