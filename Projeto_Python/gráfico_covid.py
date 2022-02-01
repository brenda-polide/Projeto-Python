import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("Covid-19.xlsx")

estados = planilha['Estados:']
casos = planilha['Casos:']

plt.title("Comparação dos estados de Bahia e São Paulo:")

plt.bar(estados, casos, color='dodgerblue', width=0.5)

plt.grid()
plt.show()