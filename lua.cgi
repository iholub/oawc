#!/usr/bin/lua

local function main()
    print("Content-Type: text/html")
    print("")
    print("<!DOCTYPE html>")
    qs = os.getenv'QUERY_STRING'
	i, j = string.find(qs, "&")
	cmd = string.sub(qs, 1, j - 1)
	print(cmd)
	print(math.modf(os.clock()))
	wserial=io.open("/dev/ttyUSB0","w")
	print(math.modf(os.clock()))
  
	wserial:write(cmd)
	print(math.modf(os.clock()))
	wserial:flush()
	print(math.modf(os.clock()))
	rserial=io.open("/dev/ttyUSB0","r")
	print(math.modf(os.clock()))
	while chaine==nil do
        chaine=rserial:read()
        rserial:flush()
	end
	print(math.modf(os.clock()))
	print("response: ")
	print(chaine)
end

main()