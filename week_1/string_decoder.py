from string import maketrans

def decoder():
	message = raw_input("what would you like to decode? ")
	table = str.maketrans(alpha, new_alpha)
	result = message.translate(table)
	print result
	
		
	

intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
trantab = maketrans(intab, outtab)

str = "Yms bgb gr! Cmlepyrsjyrgmlq! Dgb wms sqc qrpgle.kyicrpylq? Id wms bgbl'r wms qfmsjb npmzyzjw em afcai gr msr. Ir kyicq rfgq ksaf cyqgcp."
print str.translate(trantab)

#decoder()



