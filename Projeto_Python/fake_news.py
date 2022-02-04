import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("Fake News.xlsx")

regiões = planilha['Regiões:']
porcentagem = planilha['Porcentagem:']

plt.title("Comparação das Fake News:")

plt.pie(porcentagem, labels=regiões, autopct='%1.2f%%')

plt.grid()
plt.show()