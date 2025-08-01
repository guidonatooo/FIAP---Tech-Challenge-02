import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL_B3 = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"

# Define a pasta onde os arquivos baixados serão salvos

PASTA_DOWNLOAD = os.path.join(os.getcwd(), "downloads_b3")

# --- Lógica Principal do Script ---

# 1. Configurar o navegador (Chrome) com opções personalizadas
print("Iniciando configuração do WebDriver...")
chrome_options = webdriver.ChromeOptions()

# Define a pasta de download personalizada.
prefs = {"download.default_directory": PASTA_DOWNLOAD}
chrome_options.add_experimental_option("prefs", prefs)

# Garante que a pasta de download exista. Se não existir, ela é criada.
os.makedirs(PASTA_DOWNLOAD, exist_ok=True)

# Instala e configura o ChromeDriver automaticamente usando webdriver-manager
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=chrome_options)
print("WebDriver configurado e pronto para uso.")

try:
    # 2. Abrir a página da B3
    print(f"Acessando a URL: {URL_B3}")
    driver.get(URL_B3)

    # 3. Localizar e clicar no botão de Download
    print("Aguardando o botão de download ficar disponível...")
    
    botao_download = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Download')]"))
    )
    
    print("Botão encontrado! Clicando para iniciar o download...")
    botao_download.click()

    # 4. Aguardar o download ser concluído
    nome_arquivo_esperado = f"IBOV_{datetime.today().strftime('%Y-%m-%d')}.csv"
    caminho_arquivo_completo = os.path.join(PASTA_DOWNLOAD, nome_arquivo_esperado)
    
    print(f"Aguardando o download do arquivo: {nome_arquivo_esperado}...")
    
    tempo_espera = 0
    while not os.path.exists(caminho_arquivo_completo):
        time.sleep(1)
        tempo_espera += 1
        if tempo_espera > 60:
            raise Exception("Tempo de espera para download excedido!")

    print("-" * 50)
    print("SUCESSO! Download concluído.")
    print(f"O arquivo foi salvo em: {caminho_arquivo_completo}")
    print("-" * 50)

except Exception as e:
    print(f"\nOcorreu um erro durante o processo: {e}")

finally:
    print("Fechando o navegador.")
    driver.quit()