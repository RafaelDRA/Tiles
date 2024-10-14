import os
import json

def create_images_json(folder_path):
    # Lista para armazenar os nomes dos arquivos de imagem
    images_list = []

    # Extensões de arquivos de imagem que queremos incluir
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

    # Itera sobre os arquivos na pasta especificada
    for file_name in os.listdir(folder_path):
        # Verifica se o arquivo tem uma extensão de imagem
        if os.path.splitext(file_name)[1].lower() in image_extensions:
            images_list.append(file_name)

    # Cria o conteúdo JSON
    images_json = {
        "images": images_list
    }

    # Caminho do arquivo JSON de saída
    json_output_path = os.path.join(folder_path, 'images.json')

    # Salva o JSON no arquivo
    with open(json_output_path, 'w') as json_file:
        json.dump(images_json, json_file, indent=4)

    print(f"'images.json' criado com sucesso na pasta: {folder_path}")

def process_folders(base_folder):
    # Percorre todas as subpastas do diretório base
    for root, dirs, files in os.walk(base_folder):
        # Verifica se a pasta contém "ZT" no nome
        if "ZT" in os.path.basename(root):
            print(f"Processando a pasta: {root}")
            # Cria o arquivo images.json para a pasta
            create_images_json(root)

# Caminho da pasta atual (ou pode ser alterado para outro caminho se necessário)
current_folder = os.getcwd()

# Chama a função para processar todas as subpastas que contenham 'ZT' no nome
process_folders(current_folder)
