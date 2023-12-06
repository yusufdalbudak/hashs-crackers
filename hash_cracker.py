import subprocess
import crypt

shadow = subprocess.check_output("cat /etc/shadow", shell=True).decode()

#print(shadow)

passwd_list = shadow.split("\n")
f = open("unix_passwords.txt","r")



#yescrypt
#kali:$y$j9T$7X9YlJ7c4u44URQvzTxxT0$BisyVCLhoPfP22Svis.KFV5tMwCFEJgT7yJIRCHp3G/:19426:0:99999:7:::



for passwd in passwd_list:
    #print(passwd)

    if "kali" in passwd:
        s = passwd.split("$")
        salt = "$"+s[1]+"$"+s[2]+"$"+s[3]
        #print(salt)

        for passwd_try in f:
            tmp_passwd = crypt.crypt(passwd_try.strip(),salt)
            #print(tmp_passwd)
            if tmp_passwd in passwd:
                print("Password is :",passwd_try.strip())
                break

        


            