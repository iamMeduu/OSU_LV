import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data_C02_emission.csv")
# a) Histogram emisije CO2
plt.figure(figsize=(8, 5))
data['CO2 Emissions (g/km)'].plot(kind='hist', bins=25, edgecolor='black', color='magenta')
plt.title('Histogram emisije CO2 plinova')
plt.xlabel('Emisija CO2 (g/km)')
plt.ylabel('Broj vozila')


# b) Dijagram raspršenja (odnos gradske potrošnje goriva i emisije CO2 obojeno prema tipu goriva)
plt.figure(figsize=(8, 5))
tipovi_goriva = data['Fuel Type'].unique()
boje = plt.cm.get_cmap('Set2', len(tipovi_goriva))

for i, gorivo in enumerate(tipovi_goriva): 
    subset = data[data['Fuel Type'] == gorivo]
    plt.scatter(subset['Fuel Consumption City (L/100km)'], subset['CO2 Emissions (g/km)'],
        color=boje(i), label=gorivo, alpha=0.6, )

plt.title('Odnos gradske potrošnje goriva i emisije CO2')
plt.xlabel('Gradska potrošnja (L/100km)')
plt.ylabel('Emisija CO2 (g/km)')
plt.legend(title='Tip goriva')


# c) Kutijasti dijagram (boxplot) - razdioba izvangradske potrošnje s obzirom na tip goriva
plt.figure(figsize=(8, 5))
data.boxplot(column='Fuel Consumption Hwy (L/100km)', by='Fuel Type', grid=False)
plt.title('Izvangradska potrošnja obzirom na tip goriva')
plt.xlabel('Tip goriva')
plt.ylabel('Izvangradska potrošnja (L/100km)')


# d) Stupčasti dijagram - broj vozila po tipu goriva
plt.figure(figsize=(8, 5))
broj_po_gorivu = data.groupby('Fuel Type').size()
broj_po_gorivu.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Broj vozila po tipu goriva')
plt.xlabel('Tip goriva')
plt.ylabel('Broj vozila')
plt.xticks(rotation=0)


# e) Stupčasti dijagram - prosječna CO2 emisija s obzirom na broj cilindara
plt.figure(figsize=(8, 5))
prosjek_co2_cilindri = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
prosjek_co2_cilindri.plot(kind='bar', color='darkcyan', edgecolor='black')
plt.title('Prosječna CO2 emisija s obzirom na broj cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Prosječna CO2 emisija (g/km)')
plt.xticks(rotation=0)

plt.show()