import fsb795

tk_c = fsb795.Certificate('/home/tomas/Рабочий стол/Averkina_pers/kazna_2024/Аверкина Олеся Александровна (1).cer')
valid = tk_c.validityCert()
print ('действительна до: ' + str(valid['not_after']))


sub, vlad_sub = tk_c.subjectCert()
#print ('vlad_sub=' + str(vlad_sub))
for key in sub.keys():
	lst = {key:sub[key]}
#	print (lst)
	name = lst.get('CN')
#work = lst.get('title')

print ('Владелец: ' + name)