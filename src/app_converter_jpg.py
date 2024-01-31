from PIL import Image
import subprocess



def converter_webp_para_jpg(caminho_entrada, caminho_saida):
    imagem = Image.open(caminho_entrada)
    imagem.convert('RGB').save(caminho_saida, 'jpeg')

caminhos_arquivos = []                                                                                                                                                                    
# Crie o comando
comando = ["find", "/Users/username/Desktop/", "-type", "f", "-iname", "*.webp"]

# Execute o comando

result = subprocess.run(comando, capture_output=True, text=True)
if result.returncode == 0:
    # Divida a saída em linhas e crie uma lista
    caminhos_arquivos = result.stdout.strip().split('\n')
    print("Arquivos encontrados:", len(caminhos_arquivos))
else:
    print("Erro ao executar o comando:", result.stderr)
  
for i, caminho in enumerate(caminhos_arquivos):
    saida = caminho_saida + str(i) + '.jpg'
    converter_webp_para_jpg(caminho, saida)
print("Conversão concluída com sucesso!")