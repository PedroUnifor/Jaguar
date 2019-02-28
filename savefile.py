import csv
import re
import os
import urllib.request
from datetime import datetime
from time import sleep

log = open('driver_log.csv', 'w')
escrever = csv.writer(log)
j = 0
i = 0
b = 1
while os.path.exists("imagem%s.jpg" % i):
    i += 1
while b == 1:
    try:
        urllib.request.urlretrieve("https://image.tmdb.org/t/p/w600_and_h900_bestv2/m1UI4XnQF7NZHBXdfRBDhVQheIz.jpg", "imagem%s.jpg" % i)
        nomeimagem = os.getcwd()+"/imagem%s.jpg" % i
        print("imagem %s baixada com sucesso!" % i)
    except:
        print('ocorreu um erro no download da imagem %s' % i)
    #delay em segundos
    sleep(0.1)
    try:
        escrever.writerow((nomeimagem, 'direção','angulo'))
        print("imagem %s salva no arquivo de Log com sucesso!" % i)
    except:
        print('ocorreu um erro para salvar a imagem %s' % i)
    i += 1
    j += 1
    print ("j: %s" %j)
    if j >= 3:
        b = 0
    
print(os.getcwd())
log.close()