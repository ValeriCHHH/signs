import fsb795
import zipfile
import os
import re
import pathlib



pattern_cer = r"\w+[- ]*\w*[ -.\s]?\w*[ -.\s]?\w*[ -.\s]?\w*[ -.\s]?\w*[ -.\s]?\w*[ -.\s]?\w*.cer"
pattern_zip = r"\w+[- ]*\w*[ -.\s]?\w*[ -.\s]?\w*.zip"

print (os.getcwd())
sequence_zip = str(os.listdir('./media'))

result_search = re.search(pattern_zip, sequence_zip).group()

path_zip = f'./media/{result_search}'

zipfile.is_zipfile(str(path_zip))
z = zipfile.ZipFile(path_zip, 'r')
sequence_cer = str(z.namelist())
#print(sequence_cer)

result_search_cert = re.search(pattern_cer, sequence_cer).group()


f = open(path_zip,'rb')
zfile = zipfile.ZipFile(f)
for zc in zfile.namelist():
    zfile.extract(result_search_cert,'./media', pwd = b'12345')


def get_cert_info (cert):
    tk_c = fsb795.Certificate(cert)
    valid = tk_c.validityCert()
    sub, usr_c = tk_c.subjectCert()
    iss, dst_c = tk_c.issuerCert()
    for key in sub.keys():
        lst = {key:sub[key]}
    for key in iss.keys():
        dst = {key:iss[key]}
#    print(lst.get('CN'), valid['not_after'], dst)
    sub_name = lst.get('CN')
    dst_name = dst.get('CN')
    end_date = valid['not_after']
    print (f'{sub_name} \n{dst_name} \n{end_date}')

get_cert_info ('/home/tomas/Рабочий стол/Averkina_pers/Аверкина Олеся Александровна.cer')
print (sequence_zip)
print (path_zip)
print (result_search_cert)
