#!/usr/bin/lua

local function main()
    print("Content-Type: text/html")
    print("")
    print("<!DOCTYPE html>")
	print(math.modf(os.clock()))
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
	res=io.open("/var/ardres","r")
	while line==nil do
		line=res:read()
	end
	print(math.modf(os.clock()))
	print(line)

end

main()