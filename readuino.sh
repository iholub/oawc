#!/bin/sh
#/usr/bin/readuino.sh
# simple script to tail newline terminated messages from the arduino
# adjust the head number depending on your arduino messages
echo "aaaa"
if  ! [ -f /tmp/isrunning ]; then
  echo "a1"
  if  [ -c /dev/ttyUSB0 ]; then
      echo "a2"
      echo $$ > /tmp/isrunning                   
      while [ 1 ]; do                        
              if [ -c /dev/ttyUSB0 ]; then
                      head -n 1 /dev/ttyUSB0 >/tmp/volts
                      sleep 1         
              else
                      # USB dissapeared. 
                      echo "Arduino no longer attached" >/tmp/volts
                      rm /tmp/isrunning
                      exit            
              fi
      done
  else
      echo "Arduino not yet  attached" >/tmp/volts
  fi
fi