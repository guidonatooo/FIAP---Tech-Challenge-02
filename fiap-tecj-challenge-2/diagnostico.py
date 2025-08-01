import os
import glob
import pandas as pd

PASTA_DOWNLOAD = os.path.join(os.getcwd(), "downloads_b3")

print("--- INICIANDO SCRIPT DE DIAGNÓSTICO ---")

try:
    lista_de_arquivos = glob.glob(os.path.join(PASTA_DOWNLOAD, '*.csv'))
    if not lista_de_arquivos:
        raise FileNotFoundError("Nenhum arquivo .csv encontrado na pasta de downloads.")
    
    caminho_csv = max(lista_de_arquivos, key=os.path.getctime)
    print(f"Analisando o arquivo: {caminho_csv}\n")

    # Tentativa de leitura com os parâmetros que acreditamos serem os corretos
    df = pd.read_csv(
        caminho_csv, 
        sep=';', 
        encoding='latin1', 
        header=1, 
        skipfooter=1, 
        engine='python'
    )

    # --- INÍCIO DA ANÁLISE ---
    print("--- 1. Amostra do DataFrame (df.head()) ---")
    print(df.head())
    print("-" * 50)

    print("\n--- 2. Informações do DataFrame (df.info()) ---")
    # Esta parte é a mais importante. Ela nos dirá quantos valores não-nulos cada coluna tem.
    df.info()
    print("-" * 50)
    # --- FIM DA ANÁLISE ---

except Exception as e:
    print(f"\nOcorreu um erro durante o diagnóstico: {e}")

print("\n--- FIM DO DIAGNÓSTICO ---")