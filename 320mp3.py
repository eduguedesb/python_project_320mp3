import os
import shutil
from mutagen.mp3 import MP3

def verificar_bitrate(arquivo):
    audio = MP3(arquivo)
    bitrate = audio.info.bitrate
    return bitrate

def mover_arquivos(pasta_principal):
    # Caminho da pasta TEMP
    pasta_temp = os.path.join(pasta_principal, 'TEMP')

    # Criar a pasta TEMP apenas uma vez, dentro da pasta principal
    if not os.path.exists(pasta_temp):
        os.makedirs(pasta_temp)

    # Percorre todos os arquivos na pasta principal, ignorando a pasta TEMP
    for file in os.listdir(pasta_principal):
        caminho_arquivo = os.path.join(pasta_principal, file)
        
        # Verifica se é um arquivo e se é MP3
        if os.path.isfile(caminho_arquivo) and file.endswith('.mp3'):
            try:
                # Verifica o bitrate
                bitrate = verificar_bitrate(caminho_arquivo)

                # Move arquivos que não são 320 kbps
                if bitrate != 320000:
                    print(f"Movendo {file} - Bitrate: {bitrate // 1000} kbps")
                    shutil.move(caminho_arquivo, os.path.join(pasta_temp, file))
            
            except Exception as e:
                print(f"Erro ao processar {file}: {e}")

if __name__ == "__main__":
    # Insira o caminho da pasta principal aqui
    pasta_principal = r"D:\BACKUP\PASTA (MP3)"  # Atualize com o caminho correto
    mover_arquivos(pasta_principal)
