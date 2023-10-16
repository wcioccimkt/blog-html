#Coleta-de-dados

pip install pandas
pip install openpyxl

#BeautifulSoup

#Exemplo de dados de imóveis
imoveis = [
    {"Endereço": "Rua A, 123", "Área (m²)": 150, "Preço (R$)": 250000},
    {"Endereço": "Avenida B, 456", "Área (m²)": 200, "Preço (R$)": 350000},
    # Adicione mais imóveis conforme necessário
]

import pandas as pd

df = pd.DataFrame(imoveis)

df.to_excel("dados_imobiliarios.xlsx", index=False)


