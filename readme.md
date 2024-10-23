Este script realiza a verificação e organização de arquivos MP3 com base na taxa de bits (bitrate). O programa percorre todos os arquivos MP3 em uma pasta principal especificada, identifica aqueles que não possuem uma taxa de bits de 320 kbps e os move para uma subpasta chamada TEMP.

Verifica o bitrate de cada arquivo MP3 utilizando a biblioteca mutagen.
Cria uma pasta TEMP dentro da pasta principal, se ela ainda não existir.
Move para a pasta TEMP todos os arquivos MP3 que não possuírem uma taxa de bits de 320 kbps.
Exibe uma mensagem informando o bitrate e o nome do arquivo movido.
Em caso de erro durante o processamento de um arquivo, o erro é exibido no console.

Dependências:
mutagen: Biblioteca necessária para extrair informações dos arquivos MP3, como o bitrate.

Como usar:
Atualize o caminho da pasta principal no script com o local onde estão seus arquivos MP3.
Execute o script e ele moverá os arquivos MP3 com bitrates diferentes de 320 kbps para a subpasta TEMP.
