import os
import glob
import pandas as pd

PASTA_DOWNLOAD = os.path.join(os.getcwd(), "downloads_b3")
PASTA_OUTPUT = os.path.join(os.getcwd(), "output")

print("Iniciando conversão para Parquet (Modo de Compatibilidade v1.0)...")

try:
    lista_de_arquivos = glob.glob(os.path.join(PASTA_DOWNLOAD, '*.csv'))
    if not lista_de_arquivos:
        raise FileNotFoundError("Nenhum arquivo .csv encontrado.")
    
    caminho_csv = max(lista_de_arquivos, key=os.path.getctime)
    
    df = pd.read_csv(
        caminho_csv, sep=';', encoding='latin1', skiprows=2, header=None,
        skipfooter=1, engine='python', decimal=',', thousands='.', usecols=range(5)
    )
    
    df.columns = ['codigo', 'acao', 'tipo', 'qtde_teorica', 'participacao']
    
    print("CSV lido e colunas renomeadas com sucesso.")
    
    nome_base_arquivo = os.path.basename(caminho_csv)
    data_pregao = nome_base_arquivo.split('_')[1].replace('.csv', '')
    pasta_particao = os.path.join(PASTA_OUTPUT, f'data={data_pregao}')
    os.makedirs(pasta_particao, exist_ok=True)
    caminho_parquet = os.path.join(pasta_particao, 'pregao.parquet')

    # --- CORREÇÃO APLICADA AQUI ---
    # Forçamos o uso da versão 1.0 do Parquet para máxima compatibilidade com o Glue
    df.to_parquet(caminho_parquet, index=False, engine='pyarrow', version='1.0')

    print("-" * 50)
    print("SUCESSO! Conversão para Parquet v1.0 concluída.")
    print(f"Arquivo salvo em: {caminho_parquet}")
    print("-" * 50)

except Exception as e:
    print(f"\nOcorreu um erro durante o processo: {e}")