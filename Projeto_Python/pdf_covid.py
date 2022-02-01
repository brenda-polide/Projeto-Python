import os
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Times', '', 16)

texto = "Análise dos dados do site: No Brasil, a pandemia do COVID-19 tem sido grave nos estados das regiões mais pobres, como o Nordeste. Na ausência de uma política nacional de controle do surto, as autoridades estaduais e municipais implementaram medidas de saúde pública, e muitos estados têm uma alta proporção da população trabalhadora informal. O estado da Bahia, apesar de ser o quarto estado em população, tem o segundo maior número absoluto de pobres do país, com a metade da população em condições precárias, sem conhecimento, dessa forma desencadeando mais a desinformação e a disseminação do vírus. São Paulo é um estado com a economia que forma o maior Produto Interno Bruto (PIB), contudo mesmo possuindo uma economia elevada e melhor que na Bahia, as taxas de contaminação do vírus foram altíssimas, muitas vezes pela questão das fake news, conhecimentos errados. Atualmente em 2022, as pessoas estão tomando as devidas providências em relação ao COVID-19, se vacinando e os índices tem diminuído, uso essa analise para ressaltar as desigualdades e de como isso afeta ainda mais a pandemia, retratando dessa forma a realidade que só se choca quando se sente na pele."

pdf.multi_cell(w=0, h=8, txt=texto, align='J')

pdf.output("Covid-19.pdf")

print("O PDF foi criado com sucesso!")
os.system("pause")