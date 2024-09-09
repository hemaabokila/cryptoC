#!/usr/bin/python3
from optparse import OptionParser
class caesar():
    def encryption(plaintex,key):
        ctext=""
        for i in plaintex:
            if i.isalpha():
                isupper=i.isupper()
                cipher=chr((ord(i)-ord("A" if isupper else "a") +int(key))%26+ord("A" if isupper else "a"))
                ctext += cipher
        print(ctext)
        return ctext
    def decryption(cipher,key):
        return caesar.encryption(cipher,-key)

pars= OptionParser("""
                       _         ____ 
  ___ _ __ _   _ _ __ | |_ ___  / ___|
 / __| '__| | | | '_ \| __/ _ \| |    
| (__| |  | |_| | |_) | || (_) | |___ 
 \___|_|   \__, | .__/ \__\___/ \____|
           |___/|_|                   
                       
---------------------------
!!!CryptoC is a tool that encrypts text data using the Caesar cipher
---------------------------
cryptroC -t + text -k +key
Developed by: Ibrahem abo kila
""")
pars.add_option("-t", "--text", dest="text")
pars.add_option("-k", "--key", dest="key")
(options ,args) = pars.parse_args()
if options.text == None:
    print(pars.usage)
elif options.text == None:
    print(pars.usage)
else:
    print("""
                       _         ____ 
  ___ _ __ _   _ _ __ | |_ ___  / ___|
 / __| '__| | | | '_ \| __/ _ \| |    
| (__| |  | |_| | |_) | || (_) | |___ 
 \___|_|   \__, | .__/ \__\___/ \____|
           |___/|_|                   
                       
---------------------------
""")
    caesar.encryption(options.text,options.key)
