import numpy as np
import pandas as pd
import matplotlib . pyplot as plt

data = pd.read_csv("data_C02_emission.csv")
#Broj redaka bez prvog i tip vrijednosti po stupcima
print("Broj redaka: ",len(data.iloc[1:]))
print(data.dtypes)
# Postoje li izostale vrijednosti?
print("\nBroj izostalih vrijednosti po stupcima:")
print(data.isnull().sum())

# Postoje li duplicirane vrijednosti i brisanje istih
broj_duplikata = data.duplicated().sum()
print("\nBroj dupliciranih redaka: ", broj_duplikata)
if broj_duplikata > 0:
    data.drop_duplicates(inplace=True)
    data.reset_index(drop=True, inplace=True)
    print("Duplicirani redci su obrisani.")


# Na temelju CSV-a, to su: Make, Model, Vehicle Class, Transmission, Fuel Type
kategoricki_stupci = ['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']
for col in kategoricki_stupci:
    if col in data.columns:
        data[col] = data[col].astype('category')
print("\nNovi tipovi podataka nakon konverzije u 'category':")
print(data.dtypes)

stupci_za_ispis = ['Make', 'Model', 'Fuel Consumption City (L/100km)']

najmanja_potrosnja = data.sort_values(by="Fuel Consumption City (L/100km)", ascending=True).head(3)
najveca_potrosnja = data.sort_values(by="Fuel Consumption City (L/100km)", ascending=True).tail(3)

print("Top 3 NAJVECE potrosnje: ",najveca_potrosnja[stupci_za_ispis])
print("Top 3 NAJMANJE potrosnje: ",najmanja_potrosnja[stupci_za_ispis])

# Koristimo stupac 'Engine Size (L)'
filtrirana_vozila = data[(data['Engine Size (L)']>=2.5)&(data['Engine Size (L)']<=3.5)]
print("Broj vozila s filtriranim enigneom: ", len(filtrirana_vozila))
print("Prosjecna emisija C02 filtriranih vozila: ",filtrirana_vozila['CO2 Emissions (g/km)'].mean(), "[g/km]")

audi = data[data["Make"]=="Audi"]
print("Broj 'Audi' mjerenja: ", len(audi))
audi_4_cilindra = audi[audi["Cylinders"]==4]
print("Prosjecna emisija C02 Audi vozila s 4 cilindra: ", audi_4_cilindra["CO2 Emissions (g/km)"].mean(), "[g/km]")

# 1. Grupiramo podatke po stupcu 'Cylinders'
# Prvo napravimo grupiranje i izračunamo statistiku za SVE cilindre
analiza_svi = data.groupby('Cylinders')['CO2 Emissions (g/km)'].agg(['count', 'mean'])

# 2. Zatim filtriramo taj rezultat koristeći .index
# Tražimo one gdje je broj cilindara (indeks) >= 4 i paran
analiza_cilindara = analiza_svi[(analiza_svi.index >= 4) & (analiza_svi.index % 2 == 0)]

print("\nAnaliza vozila s obzirom na broj cilindara:")
print(f"Broj vozila s takvom korelacijom: {analiza_cilindara['count'].sum()}")
print(analiza_cilindara)

# f) Analiza potrošnje: Dizel vs. Regularni benzin ---

# 1. Izdvajamo dizel i benzin
dizel_vozila = data[data['Fuel Type'] == 'D']
benzin_vozila = data[(data['Fuel Type'] == 'X')]

# 2. Izračun prosjeka (mean) za gradsku potrošnju
prosjek_dizel = dizel_vozila['Fuel Consumption City (L/100km)'].mean()
prosjek_benzin = benzin_vozila['Fuel Consumption City (L/100km)'].mean()

# 3. Izračun medijana (median) za gradsku potrošnju
medijan_dizel = dizel_vozila['Fuel Consumption City (L/100km)'].median()
medijan_benzin = benzin_vozila['Fuel Consumption City (L/100km)'].median()

print(f"\nDizel vozila:")
print(f"  - Broj dizela: {len(dizel_vozila)} ")
print(f"  - Prosjecna gradska potrosnja: {prosjek_dizel:.2f} L/100km")
print(f"  - Medijalna gradska potrosnja: {medijan_dizel:.2f} L/100km")

print(f"\nRegularni benzin (X) vozila:")
print(f"  - Broj benzina: {len(benzin_vozila)} ")
print(f"  - Prosjecna gradska potrosnja: {prosjek_benzin:.2f} L/100km")
print(f"  - Medijalna gradska potrosnja: {medijan_benzin:.2f} L/100km")

# --- g) Najveći potrošač među dizelašima s 4 cilindra (preko sortiranja) ---
# 1. Filtriramo dizelaše s 4 cilindra
dizel_4 = data[(data['Fuel Type'] == 'D') & (data['Cylinders'] == 4)]

# 2. Sortiramo po gradskoj potrošnji silazno (ascending=False)
# head(1) uzima samo prvi, tj. najveći rezultat
najveci_potrosac_sort = dizel_4.sort_values(by='Fuel Consumption City (L/100km)', ascending=False).head(1)

print("\nVozilo s 4 cilindra na dizelski pogon s najvecom gradskom potrosnjom (dobiveno sortiranjem):")
print(najveci_potrosac_sort[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

# Filtriramo sve redove gdje mjenjač počinje slovom 'M'
rucni_mjenjaci = data[data['Transmission'].str.startswith('M')]

# Brojimo takva vozila
broj_rucnih = len(rucni_mjenjaci)

print(f"\nBroj vozila s rucnim tipom mjenjaca: {broj_rucnih}")

# --- j) Vizualizacija korelacije (Scatter plot) ---

# 1. Grupiranje podataka (uzimamo prosjek emisije po cilindrima)
podaci_za_graf = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
data = data.corr( numeric_only=True)
print(data)
# 2. Kreiranje grafikona
# kind='bar' stvara uspravne stupce
podaci_za_graf.plot(kind='bar', color='skyblue', edgecolor='black', figsize=(10, 6))

# 3. Estetsko uređivanje
plt.title('Prosjecna CO2 emisija prema broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Prosjecna emisija (g/km)')
plt.xticks(rotation=0) # Da brojevi na X osi stoje ravno, ne ukoso
plt.grid(axis='y', linestyle='--', alpha=0.7) # Mreža samo po vodoravnim linijama

# 4. Prikaz
plt.show()
#sns.heatmap(data)


