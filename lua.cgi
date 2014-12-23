#!/usr/bin/lua

local function main()
    print("Content-Type: text/html")
    print("")
    print("<!DOCTYPE html>")
    print("Hello World! ... wenn nicht.")
	wserial=io.open("/dev/ttyUSB0","w")
	wserial:write("iziz")
	wserial:flush()
	rserial=io.open("/dev/ttyUSB0","r")
	while chaine==nil do
        chaine=rserial:read()
        rserial:flush()
	end
	print(chaine)
end

main()