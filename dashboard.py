# Salvar o script Python como um arquivo .py para a usuária baixar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações gerais
plt.style.use("seaborn-whitegrid")
sns.set_palette("pastel")
figsize = (10, 6)

# === 1. LER PLANILHA ===
arquivo = "Questionário Socioeconômico 2025 (OFICIAL)(1-52).xlsx"
df = pd.read_excel(arquivo, engine='openpyxl')

# === 2. LIMPEZA DE DADOS ===
df = df.dropna(axis=1, how='all')  # Remove colunas totalmente vazias

# Renomeia colunas importantes para facilitar
df.rename(columns={
    "Em qual cidade você reside?": "Cidade",
    "Qual é o seu gênero?": "Gênero",
    "Qual é a faixa de renda mensal da sua família?": "Renda Familiar",
    "Você trabalha?": "Trabalha",
    "Qual sua expectativa após se formar?": "Expectativa Pós-Formado"
}, inplace=True)

# === 3. GRÁFICOS ===

# Participantes por Cidade
plt.figure(figsize=figsize)
df['Cidade'].value_counts().plot(kind='bar')
plt.title("Distribuição de Participantes por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_cidade.png")
plt.close()

# Distribuição por Gênero
plt.figure(figsize=figsize)
df['Gênero'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Distribuição por Gênero")
plt.ylabel("")
plt.tight_layout()
plt.savefig("grafico_genero.png")
plt.close()

# Faixa de Renda Familiar
plt.figure(figsize=figsize)
df['Renda Familiar'].value_counts().sort_index().plot(kind='barh')
plt.title("Faixa de Renda Familiar")
plt.xlabel("Quantidade")
plt.ylabel("Faixa de Renda")
plt.tight_layout()
plt.savefig("grafico_renda.png")
plt.close()

# Situação de Trabalho
plt.figure(figsize=figsize)
df['Trabalha'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Você Trabalha?")
plt.ylabel("")
plt.tight_layout()
plt.savefig("grafico_trabalho.png")
plt.close()

# Expectativas após se formar
plt.figure(figsize=figsize)
df['Expectativa Pós-Formado'].value_counts().plot(kind='barh')
plt.title("Expectativas após se Formar")
plt.xlabel("Quantidade")
plt.ylabel("Expectativa")
plt.tight_layout()
plt.savefig("grafico_expectativa.png")
plt.close()

print("Gráficos salvos com sucesso! 🎉")
"""

with open("/mnt/data/dashboard_socioeconomico.py", "w") as f:
    f.write(codigo)

"/mnt/data/dashboard_socioeconomico.py"
