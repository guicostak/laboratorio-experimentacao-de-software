import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import os

plt.style.use("seaborn-v0_8-darkgrid")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../"))

file_path = os.path.join(ROOT_DIR, "outputs", "repos.csv")
output_dir = os.path.join(ROOT_DIR, "outputs", "graphs")

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(file_path)

# Converter coluna de criação para datetime
df["Criado em"] = pd.to_datetime(df["Criado em"], errors='coerce').dt.tz_localize(None)

# Calcular idade dos repositórios
df["Idade (anos)"] = (datetime.datetime.now() - df["Criado em"]).dt.days / 365

def save_graph(fig, filename):
    file_path = os.path.join(output_dir, filename)
    fig.savefig(file_path)
    plt.close(fig)

# RQ01 - Idade dos Repositórios
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df["Idade (anos)"].dropna(), bins=20, ax=ax, kde=True, color="royalblue")
ax.set_title("Idade dos Repositórios Populares")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Número de Repositórios")

save_graph(fig, "RQ01_idade_repositorios.png")