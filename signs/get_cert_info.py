import fsb795
from zipfile import ZipFile

#cert = ()
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

get_cert_info ('/home/maverick/Рабочий стол/Averkina_pers/Аверкина Олеся Александровна.cer')