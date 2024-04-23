import numpy as np
from scipy.stats import pearsonr



# Load data
kalman1 = 'alice_nlos.csv'
kalman2 = 'bob_nlos.csv'

kalman3 = 'kalvar_alice_nlos.csv'
kalman4 = 'kalvar_bob_nlos.csv'

data1 = np.loadtxt(kalman1, delimiter=',')
data2 = np.loadtxt(kalman2, delimiter=',')
data3 = np.loadtxt(kalman3, delimiter=',')
data4 = np.loadtxt(kalman4, delimiter=',')
# Calculate Pearson correlation coefficient and p-value
corr, p_value = pearsonr(data1, data2)
corr1, p_value = pearsonr(data3, data4)
print("Pearson correlation coefficient sebelum:", corr)
print("Pearson correlation coefficient sesudah:", corr1)