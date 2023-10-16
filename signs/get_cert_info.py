import fsb795
import zipfile
import os
import re



pattern_cer = r"\w+[- ]?\w+[ -\.]?\w+[ -\.]?\w+[ -\.]?\w+[ -\.]?\w+[ -\.]?\w+[ -\.]?\w+\.cer"
pattern_zip = r"\w+[- ]*\w*[ -.\s]?\w*[ -.\s]?\w*.zip"

sequence_zip = str(os.listdir('./media'))
result_search = re.search(pattern_zip, sequence_zip).group()
path_zip = f'./media/{result_search}'
zipfile.ZipFile(str(path_zip))
z = zipfile.ZipFile(path_zip, 'r')
sequence_cer = str(z.namelist())
result_search_cert = re.search(pattern_cer, sequence_cer).group()
path_zip = f'./media/{result_search}'
zipfile.ZipFile(str(path_zip))
z = zipfile.ZipFile(path_zip, 'r')

f = open(path_zip,'rb')
zfile = zipfile.ZipFile(f, 'r')
for zc in zfile.namelist():
    zfile.extract(result_search_cert,'./media')
    sequence_cer_unzip = str(os.listdir('./media'))
    result_search_unzip_cert = re.search(pattern_cer, sequence_cer_unzip).group()

cert = f'./media/{result_search_unzip_cert}'





def get_cert_info (cert):
    tk_c = fsb795.Certificate(cert)
    valid = tk_c.validityCert()
    sub, usr_c = tk_c.subjectCert()
    iss, dst_c = tk_c.issuerCert()
    for key in sub.keys():
        lst = {key:sub[key]}
    for key in iss.keys():
        dst = {key:iss[key]}
    sub_name = lst.get('CN')
    dst_name = dst.get('CN')
    end_date = valid['not_after']
    print (f'{sub_name} \n{dst_name} \n{end_date}')
    

get_cert_info (cert)
#print (sequence_zip)
#print (path_zip)
#print (result_search_cert)
#print(sequence_cer_unzip)
#print(result_search_unzip_cert)