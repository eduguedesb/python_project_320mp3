# Visão Geral:
Este script realiza a verificação e organização de arquivos MP3 com base na taxa de bits (bitrate). O programa percorre todos os arquivos MP3 em uma pasta principal especificada, identifica aqueles que não possuem uma taxa de bits de 320 kbps e os move para uma subpasta chamada TEMP.

# Funcionamento:
Verifica o bitrate de cada arquivo MP3 utilizando a biblioteca mutagen, cria uma pasta TEMP dentro da pasta principal, se ela ainda não existir, move para a pasta TEMP todos os arquivos MP3 que não possuírem uma taxa de bits de 320 kbps, exibe uma mensagem informando o bitrate e o nome do arquivo movido e, em caso de erro durante o processamento de um arquivo, o erro é exibido no console.

# Dependências:
mutagen: Biblioteca necessária para extrair informações dos arquivos MP3, como o bitrate.

# Como Usar:
Atualize o caminho da pasta principal no script com o local onde estão seus arquivos MP3.
Execute o script com o seguinte comando: py 320mp3.py ou python 320mp3.py.
