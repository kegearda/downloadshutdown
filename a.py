
import psutil
import time
import os
print("Otomatik indirme sonu bilgisayari kapatma programi")
print("Version 1.0")
print("By Kayra Ege ARDA")
print("Program siz kapatana kadar yada internet kullanimi yazilan deger altina dusene kadar acik kalacaktir")


userinput = input("Program sonunda Bilgisayari kapatmak icin `kapat` uyutmak icin ise `uyut`yaz:")
rate = input("Mbps cinsinden bilgisayarin kapanmasini/uyumasini istediginiz degeri yaziniz:")
rate = float(rate)
while True:

    interval = 1
    t0 = time.time()
    upload0 = psutil.net_io_counters().bytes_sent
    download0 = psutil.net_io_counters().bytes_recv
    time.sleep(interval)
    t1 = time.time()
    upload1 = psutil.net_io_counters().bytes_sent
    download1 = psutil.net_io_counters().bytes_recv
    upload = (upload1 - upload0) / (t1 - t0)
    download = (download1 - download0) / (t1 - t0)
    print('Upload (Mbps): ', round(upload/1000000, 3))
    print('Download (Mbps): ', round(download/1000000, 3))
    downr = round(download/1000000, 3)
    if downr < rate:
        print("5 dakika bekleniyor")
        time.sleep(360)
        interval = 1
        t0 = time.time()
        upload0 = psutil.net_io_counters().bytes_sent
        download0 = psutil.net_io_counters().bytes_recv
        time.sleep(interval)
        t1 = time.time()
        upload1 = psutil.net_io_counters().bytes_sent
        download1 = psutil.net_io_counters().bytes_recv
        upload = (upload1 - upload0) / (t1 - t0)
        download = (download1 - download0) / (t1 - t0)
        print('Upload (Mbps): ', round(upload/1000000, 3))
        print('Download (Mbps): ', round(download/1000000, 3))
        downr = round(download/1000000, 3)
        if downr < rate:
            print("Bilgisayar 1dk icinde kapatilacak/uyutulacak")
            if userinput == "kapat":
                os.system("shutdown /s /t 60")
            if userinput == "uyut":
                time.sleep(60)
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            break
        else:
         continue
