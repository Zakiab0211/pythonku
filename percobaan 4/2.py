
#ALICE
A = np.reshape(rss_alice, (200,50))

rata = []
varian = []

for i in range(50):
    rata.append(np.mean(A[:,i]))
    varian.append(np.var(A[:,i]))

for j, i in itertools.product(range(200), range(50)):
    if A[j,i] < rata[i]-(varian[i]/2):
        A[j,i]=1;
    elif A[j, i] < rata[i]:
        A[j,i]=2;
    elif A[j, i] < rata[i] + (varian[i] / 2):
        A[j,i]=3;
    else:
        A[j,i]=4;

AA = []
for i in range(0,200):
    for j in range(0,50):
        AA.append(A[i][j])
        
rss_alice = []
for i in range(0,len(AA)):
    if AA[i] == 1:
        rss_alice.append(0)
        rss_alice.append(0)
    elif AA[i] == 2:
        rss_alice.append(0)
        rss_alice.append(2)
    elif AA[i] == 3:
        ras_alice.append(1)
        rss_alice.append(0)
    elif AA[i] == 4:
        ras_alice.append(1)
        rss_alice.append(1)
    else:
        rss_alice.append(1)
        rss_alice.append(0)
        
#BOB      
B = np.reshape(rss_bob, (200, 50))

rata = []
varian = []

for i in range(0, 200):
    rata.append(np.mean(B[i]))
    varian.append(np.var(B[i]))

for j in range(0, 200):
    for i in range(0, 50):
        if B[j, i] < rata[i] - (varian[i]/2):
            B[j, i] = 1
        elif B[j, i] >= rata[i] - (varian[i]/2) and B[j, i] < rata[i]:
            B[j, i] = 2
        elif B[j, i] >= rata[i] and B[j, i] < rata[i] + (varian[i]/2):
            B[j, i] = 3
        elif B[j, i] >= rata[i] + (varian[i]/2):
            B[j, i] = 4
        else:
            B[j, i] = 5
