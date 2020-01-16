# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path of the data file- path
data = pd.read_csv(path)
#Code starts here 

data['Gender'].replace('-', 'Agender', inplace=True)
gender_count = data.Gender.value_counts()
gender_count.plot(kind='bar')


# --------------
#Code starts here

alignment = data.Alignment.value_counts()
plt.pie(alignment, labels = alignment.index)
plt.title('Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.Strength.cov(sc_df.Combat)
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()

sc_pearson = sc_covariance/(sc_strength*sc_combat)

ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.Intelligence.cov(ic_df.Combat)
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance/(ic_intelligence*ic_combat)


# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)

super_best = data[data['Total'] > total_high]
super_best_names = [super_best['Name']]

print(super_best_names)


# --------------
#Code starts here

fig, (ax_1, ax_2) = plt.subplots(1,2, figsize=(20,10))
fig, (ax_3) = plt.subplots(1, figsize=(20,10))
ax_1.boxplot(super_best['Intelligence'])
ax_2.boxplot(super_best['Speed'])
ax_3.boxplot(super_best['Power'])


