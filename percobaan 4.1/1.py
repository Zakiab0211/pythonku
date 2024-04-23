# sourcery skip: for-append-to-extend, remove-redundant-if, remove-zero-from-range
import itertools
import xlrd
import xlsxwriter
import numpy as np

workbook = xlrd.open_workbook('data.xlsx', on_demand=True)
worksheet = workbook.sheet_by_index(0)
first_row=[]
for col in range(0,worksheet.ncols):
   first_row.append(worksheet.cell(0,col))
print(first_row)


rss_alice=[]
for row in range(1,(int (worksheet.nrows))):
    elm = {}
    for col in range(2):
        elm=worksheet.cell_value( row, col)
    rss_alice.append(elm)


rss_bob=[]
for row in range(1,(int (worksheet.nrows))):
    elm = {}
    for col in range(2):
        elm=worksheet.cell_value( row, col)
    rss_bob.append(elm)


A = np.reshape(rss_alice, (200, 50))

rata = []
varian = []

for i in range(50):
    rata.append(np.mean(A[i]))
    varian.append(np.var(A[i]))

for j, i in itertools.product(range(200), range(50)):
    if A[j,i] <= rata[i]-(varian[i]/2):
        A[j,i]=1;
    elif A[j, i] > rata[i]-(varian[i]/2) and A[j, i] < rata[i] :
        A[j,i]=2;
    elif A[j, i] < rata[i] and A[j,i] < rata[i]+(varian[i]/2):
        A[j,i]=3;
    elif A[j, i] < rata[i] + (varian[i] / 2):
        A[j,i]=4;
    else:
        A[j,i]=5;

AA=[]
for i, j in itertools.product(range(0,200), range (0,50)):
   AA.append(A[i,j])

rss_alice=[]
for i in range (0,len(AA)):
   if AA[i]==1:
      rss_alice.extend((0, 0))
   elif AA[i]==2:
      rss_alice.extend((0, 1))
   elif AA[i]==3:
      rss_alice.extend((1, 1))
   elif AA[i]==4:
      rss_alice.extend((1, 0))
    
    
B = np.reshape(rss_bob, (200, 50))

rata = []
varian = []

for i in range(50):
    rata.append(np.mean(B[i]))
    varian.append(np.var(B[i]))

for j, i in itertools.product(range(0,200), range(50)):
    if B[j,i] <= rata[i]-(varian[i]/2):
        B[j,i]=1;
    elif B[j, i] > rata[i]-(varian[i]/2) and B[j, i] < rata[i] :
        B[j,i]=2;
    elif B[j, i] < rata[i] and B[j,i] < rata[i]+(varian[i]/2):
        B[j,i]=3;
    elif B[j, i] < rata[i] + (varian[i] / 2):
        B[j,i]=4;
    else:
        B[j,i]=5;

BB=[]
for i, j in itertools.product(range(0,200), range (0,50)):
   BB.append(B[i,j])

rss_bob=[]
for i in range (0,len(BB)):
   if BB[i]==1:
      rss_bob.extend((0, 0))
   elif BB[i]==2:
      rss_bob.extend((0, 1))
   elif BB[i]==3:
      rss_bob.extend((1, 1))
   elif BB[i]==4:
      rss_bob.extend((1, 0))
      
workbook_alice = xlsxwriter.Workbook('alicequan.xlsx')
worksheet_alice = workbook_alice.add_worksheet('alicequan')
row = 0
column = 0
worksheet_alice.write(row, column, 'Alice')

# Write Alice's data to the Excel file
for i in range (1,len(rss_alice)+1):
    worksheet_alice.write(row, column,rss_alice[i-1])
    row += 1

# Close the Excel file for Alice's data
workbook_alice.close()

# Create a new Excel file for Bob's data
workbook_bob = xlsxwriter.Workbook('bobquan.xlsx')
worksheet_bob = workbook_bob.add_worksheet('bobquan')
row = 0
column = 0
worksheet_bob.write(row, column, 'Bob')

# Write Bob's data to the Excel file
for i in range (1,len(rss_bob)+1):
    worksheet_bob.write(row, column,rss_bob[i-1])
    row += 1

# Close the Excel file for Bob's data
workbook_bob.close()