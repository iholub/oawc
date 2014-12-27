#!/usr/bin/lua

local function main()
    print("Content-Type: text/html")
    print("")
    print("<!DOCTYPE html>")
    qs = os.getenv'QUERY_STRING'
	print(qs)
	i, j = string.find(qs, "&")
	cmd = string.sub(qs, 1, j - 1)
	print(cmd)
	wserial=io.open("/dev/ttyUSB0","w")
  	wserial:write(cmd)
	wserial:flush()
	wserial:close()
	res=io.open("/var/ardres","r")
	while line==nil do
		line=res:read()
	end
	print(line)
	ok, err = os.remove ("/var/ardres")
	print(ok .. err)
	print("end")

end

main()