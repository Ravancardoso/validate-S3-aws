import boto3
import pandas as pd
import os
import requests
from datetime import datetime

# Função para fazer o upload dos arquivos para o OneDrive
def upload_to_onedrive(local_file_path, onedrive_folder_path, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Criar a URL de upload no OneDrive
    upload_url = f"https://graph.microsoft.com/v1.0/me/drive/root:{onedrive_folder_path}/{os.path.basename(local_file_path)}:/content"
    
    with open(local_file_path, "rb") as file:
        response = requests.put(upload_url, headers=headers, data=file)
    
    if response.status_code == 201:
        print(f"Arquivo {local_file_path} enviado com sucesso para o OneDrive.")
    else:
        print(f"Erro ao enviar {local_file_path} para o OneDrive. Status code: {response.status_code}, {response.text}")

# Configurar sessão AWS
session = boto3.Session(
    aws_access_key_id="SEU_ACCESS_KEY_ID",
    aws_secret_access_key="SEU_SECRET_ACCESS_KEY",
    region_name="us-east-1"  # Ajuste para a região desejada
)
s3 = session.client('s3')

# Listar todos os buckets
buckets = s3.list_buckets()['Buckets']

# Inicializar listas
buckets_com_objetos = []
buckets_vazios = []

# Verificar se os buckets têm objetos
for bucket in buckets:
    bucket_name = bucket['Name']
    try:
        response = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=1)
        if 'Contents' in response:  # Bucket com objetos
            buckets_com_objetos.append(bucket_name)
            # Fazer backup dos arquivos para o OneDrive
            for obj in response['Contents']:
                file_key = obj['Key']
                local_file_path = f"temp/{file_key}"
                # Baixar o arquivo para o local temporário
                s3.download_file(bucket_name, file_key, local_file_path)
                # Realizar o upload para o OneDrive
                upload_to_onedrive(local_file_path, "/Backup_S3_Files", "SEU_ACCESS_TOKEN")
                # Deletar o arquivo local temporário após o backup
                os.remove(local_file_path)
        else:  # Bucket vazio
            buckets_vazios.append(bucket_name)
            # Deletar o bucket vazio
            try:
                s3.delete_bucket(Bucket=bucket_name)
                print(f"Bucket vazio {bucket_name} deletado com sucesso.")
            except Exception as e:
                print(f"Erro ao deletar o bucket vazio {bucket_name}: {e}")
    except Exception as e:
        print(f"Erro ao verificar o bucket {bucket_name}: {e}")

# Criar DataFrames
df_com_objetos = pd.DataFrame(buckets_com_objetos, columns=["Buckets com Objetos"])
df_vazios = pd.DataFrame(buckets_vazios, columns=["Buckets Vazios"])

# Salvar em planilha Excel
output_file = f"buckets_mapeados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_com_objetos.to_excel(writer, sheet_name="Buckets com Objetos", index=False)
    df_vazios.to_excel(writer, sheet_name="Buckets Vazios", index=False)

print(f"Planilha gerada com sucesso: {output_file}")
