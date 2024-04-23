#kalman filter

import numpy as np
import csv

#data Alice dan Bob
print("Program Kalman")
#kalman='alice_nlos.csv'
kalman='bob_nlos.csv'

#Proses Alice
RSSI=[]
with open(kalman) as f:
    dataalice = csv.reader(f)
    for row in dataalice:
        RSSI.append(row)
RSSI=np.array(RSSI)

RSSI2=[]
for i in range (len(RSSI)):
    RSSI2.append(int(RSSI[i][0]))
RSSI2=np.array(RSSI2)
RSSI=RSSI2.reshape(4000,1)

#Proses kalman
a=2.13
h=2.13
R=4.6
Q=0.0001
#====estimasi awal=====#
xaposteriori_0=0
paposteriori_0=1
#======================#
xapriori=[] 
residual=[]
papriori=[]
k=[]
paposteriori=[]
xaposteriori=[]

for m in range(1):
    xapriori.append(a*xaposteriori_0)
    residual.append(RSSI[m]-h*xapriori[m])
    papriori.append(a*a*paposteriori_0+Q)
    k.append(papriori[m]*h/(h*h*papriori[m]+R))
    paposteriori.append(papriori[m]*(1-k[m]*h))
    xaposteriori.append(xapriori[m]+k[m]*residual[m])
    for n in range (1,len(RSSI)):
        xapriori.append(xaposteriori[n-1])
        residual.append(RSSI[n]-h*xapriori[n])
        papriori.append(a*a*paposteriori[n-1]+Q)
        k.append(papriori[m]*h/(h*h*papriori[n]+R))
        paposteriori.append(papriori[n]*(1-k[n]*h))
        xaposteriori.append(xapriori[n]+k[n]*residual[n])
xaposteriori=np.array(xaposteriori)
final_kalman=xaposteriori.reshape(len(xaposteriori),1)
np.savetxt("kalvar_"+kalman,xaposteriori,delimiter=",",fmt='%10.5f')
