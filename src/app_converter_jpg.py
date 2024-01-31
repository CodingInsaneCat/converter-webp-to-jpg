from PIL import Image
import subprocess

#Edit the path below putting your username and the folder name where the images are located
caminho_saida = f'/Users/your-username/Desktop/folder-name/converted/'  
caminhos_arquivos = []   
comando = ["find", "/Users/your-username/Desktop/", "-type", "f", "-iname", "*.webp"]

from PIL import Image

def converter_webp_para_jpg(caminho_entrada, caminho_saida):
    """
    Converts a WebP image to JPEG format.

    Args:
        caminho_entrada (str): The path to the WebP image file.
        caminho_saida (str): The path to save the converted JPEG image file.

    Returns:
        None
    """
    imagem = Image.open(caminho_entrada)
    imagem.convert('RGB').save(caminho_saida, 'jpeg')


def execute_converter():
    """
    Executes the webp to jpg converter.

    This function runs a subprocess command to convert webp files to jpg format.
    It captures the output of the command and processes it to obtain a list of file paths.
    Then, it iterates over the file paths and converts each webp file to jpg format.
    Finally, it prints the number of files found and a success message.

    Args:
        None

    Returns:
        None
    """
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


if __name__ == '__main__':
    execute_converter()