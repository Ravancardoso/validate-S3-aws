import boto3
import pandas as pd

# Configurar sessão AWS
session = boto3.Session(
    aws_access_key_id="SEU_ACCESS_KEY_ID",
    aws_secret_access_key="",
    region_name="us-east-1"  # Ajuste para a região desejada
)
s3 = session.client('s3')

# Listar todos os buckets
buckets = s3.list_buckets()['Buckets']
print("iniciando", len(buckets))

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
        else:  # Bucket vazio
            buckets_vazios.append(bucket_name)
    except Exception as e:
        print(f"Erro ao verificar o bucket {bucket_name}: {e}")

# Criar DataFrames
df_com_objetos = pd.DataFrame(buckets_com_objetos, columns=["Buckets com Objetos"])
df_vazios = pd.DataFrame(buckets_vazios, columns=["Buckets Vazios"])

# Salvar em planilha Excel
output_file = "buckets_mapeados.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_com_objetos.to_excel(writer, sheet_name="Buckets com Objetos", index=False)
    df_vazios.to_excel(writer, sheet_name="Buckets Vazios", index=False)

print(f"Planilha gerada com sucesso: {output_file}")