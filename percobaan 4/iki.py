#Kuantisasi Ambekar oleh Mike Yuliana
#from xlwt import Workbook
import xlrd
import xlsxwriter
import numpy as np

#======pengambilan data==============
# workbook = xlrd.open_workbook ('data.xlsx', on_demand = True)
import pandas as pd
df = pd.read_excel('data.xlsx')
worksheet = workbook.sheet_by_index (0) #Ambil Workbook dinamisl
first_row = [] # Header
for col in range(0, worksheet.ncols):
    first_row.append( worksheet.cell_value (0, col))
    #transform the workbook to a list of dictionnaries
print (first_row)
#Mengambil nilai dari excel ke rss_alice
rss_alice =[]
#for row in range (1, worksheet.nrows):
for row in range (1, (int (worksheet.nrows))):
    elm = {}
    for col in range(1) :
        elm=worksheet.cell_value (row,col)
    rss_alice.append(elm)
    
#Mengambil nilai dari excel ke rss_bob
rss_bob =[]
for row in range (1, (int(worksheet.nrows))):
    elm = {}
    for col in range (2):
        elm=worksheet.cell_value(row,col)
    rss_bob.append(int(elm))
#======kuantisasi ambekar===========
#ALICE
A = np.reshape(rss_alice,(200,50))

rata = []
varian = []

for i in range (0,200) :
    rata.append(np.mean(A[i]))
    varian.append(np.var(A[i]))
for j in range (0,200) :
    for i in range (0,50) :
        if A[j,i] <= rata[i]-(varian[i]/2):
            A[j,i]=1;
        elif A[j,i] > rata[i]-(varian[i]/2) and A[j,i] < rata[i]:
            A[j,i]=2;
        elif A[j,i] >= rata[i] and A[j,i] < rata[i]+(varian[i]/2):
            A[j,i]=3;
        elif A[j,i] >= rata[i]+(varian[i]/2):
            A[j,i]=4;
        else:
            A[j,i]=5;
AA=[]
for i in range (0,200):
    for j in range (0,50):
        AA.append (A[i][j])
        
rss_alice=[]
for i in range (0,len(AA)):
    if AA[i]==1:
        rss_alice.append(0)
        rss_alice.append(0)
    elif AA[i]==2:
        rss_alice.append(0)
        rss_alice.append(1)
    elif AA[i]==3:
        rss_alice.append(1)
        rss_alice.append(1)
    elif AA[i]==4:
        rss_alice.append(1)
        rss_alice.append(0)
#BOB
B = np.reshape (rss_bob, (200,50))

rata = []
varian = []

for i in range (0,200) :
    rata.append(np.mean(B[i]))
    varian.append(np.var(B[i]))
    
for j in range (0,200) :
    for i in range (0,50) :
        if B[j,i] <= rata[i]-(varian[i]/2):
            B[j,i]=1;
        elif B[j,i] > rata[i]-(varian[i]/2) and B[j,i] < rata[i]:
            B[j,i]=2;
        elif B[j,i] >= rata[i] and B[j,i] < rata[i] + (varian [i]/2):
            B[j,i]=3;
        elif B[j,i] >= rata[i]+(varian[i]/2):
            B[j,i]=4;
        else:
            B[j,i]=5;
BB=[]
for i in range (0,200):
    for j in range (0,50):
        BB.append(B[i][j])
        
rss_bob = []
for i in range (0,len(BB)):
    if BB[i]==1:
        rss_bob.append(0)
        rss_bob.append(0)
    elif BB[i]==2:
        rss_bob.append(0)
        rss_bob.append(1)
    elif BB[i]==3:
        rss_bob.append(1)
        rss_bob.append(1)
    elif BB[i]==4:
        rss_bob.append(1)
        rss_bob.append(0)
        
#SAVE TO EXCEL
#ALICE
workbook = xlsx.writer.Workbook('alicequan.xlsx')
worksheet = workbook.add_worksheet('alicequan')
row = 0
column=0
worksheet.write (row,column,'Alice')
# iterating through content list
row=1
for i in range (1,len(rss_alice)+1) :
    worksheet.write(row, column, rss_alice [i-1])
    row += 1
workbook.close()
#BOB
workbook = xlsxwriter.Workbook('bobquan.xlsx')
worksheet = workbook.add_worksheet('bobquan')
row = 0
column = 0
worksheet.write(row, column, 'Bob')
# iterating through content list
row=1
for i in range (1, len (rss_bob)+1) :
    worksheet.write (row, column, rss_bob[i-1])
    row += 1
workbook.close()







