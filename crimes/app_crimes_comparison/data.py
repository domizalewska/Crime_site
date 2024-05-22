# Plik z danymi do wykresów
import pandas as pd
import matplotlib.pyplot as plt


df1 = pd.read_csv('data/Crimes-2021.csv', delimiter=';')
df2 = pd.read_csv('data/Crimes-2022.csv', delimiter=';')
df3 = pd.read_csv('data/Crimes-2023.csv', delimiter=';')
df4 = pd.read_csv('data/Crimes-2024.csv', delimiter=';')
df_combined = pd.concat([df1, df2, df3, df4], ignore_index=True)


def W1():
    data_1 = len(df1)
    data_2 = len(df2)
    data_3 = len(df3)
    data_4 = len(df4)

    x = [data_1, data_2, data_3, data_4]
    y = ['2021', '2022', '2023', '2024']

    positions = range(len(x))

    width = 0.2
    plt.bar(positions, x, width=width, color='r')
    plt.xticks(positions, y, rotation=80)

    plt.title('Liczba przestępst w poszczególnych latach w Chicago', fontweight='bold', fontsize=15, x=0.5, y=1.1)
    plt.ylabel('Ilość przestępstw', fontweight='bold', fontsize=15, labelpad=20)
    plt.savefig('media/images/wykres.png')
    plt.close()