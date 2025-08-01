import os
import glob
import boto3

BUCKET_NAME = "fiap-tc2-raw-guilherme-jardim"
PASTA_OUTPUT = os.path.join(os.getcwd(), "output")

def upload_para_s3():
    print("Iniciando upload do arquivo PARQUET para o S3...")
    try:
        lista_de_arquivos = glob.glob(os.path.join(PASTA_OUTPUT, '**', '*.parquet'), recursive=True)
        if not lista_de_arquivos:
            raise FileNotFoundError(f"Nenhum arquivo .parquet encontrado na pasta '{PASTA_OUTPUT}'.")
        
        caminho_local_completo = max(lista_de_arquivos, key=os.path.getctime)
        print(f"Arquivo a ser enviado: {caminho_local_completo}")

        caminho_relativo = os.path.relpath(caminho_local_completo, PASTA_OUTPUT)
        s3_key = os.path.join('raw', caminho_relativo).replace("\\", "/") 

        s3_client = boto3.client('s3')
        print(f"Enviando arquivo para s3://{BUCKET_NAME}/{s3_key}")
        s3_client.upload_file(caminho_local_completo, BUCKET_NAME, s3_key)

        print("-" * 50)
        print("SUCESSO! Upload do Parquet para o S3 concluído.")
        print("-" * 50)

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    upload_para_s3()