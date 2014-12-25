#!/usr/bin/lua

local function main()
    print("Content-Type: text/html")
    print("")
    print("<!DOCTYPE html>")
    qs = os.getenv'QUERY_STRING'
	i, j = string.find(qs, "&")
	cmd = string.sub(qs, 1, j - 1)
	print(cmd)
	wserial=io.open("/dev/ttyUSB0","w")
	wserial:write(cmd)
	wserial:flush()
	rserial=io.open("/dev/ttyUSB0","r")
	while chaine==nil do
        chaine=rserial:read()
        rserial:flush()
	end
	print("response: ")
	print(chaine)
end

main()