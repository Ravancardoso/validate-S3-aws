alidação Automática de Buckets AWS

Este projeto tem como objetivo automatizar a validação de buckets na AWS S3, verificando se estão vazios ou se contêm arquivos. Ele utiliza Python com as bibliotecas boto3, pandas e openpyxl para realizar a validação de forma eficiente e prática.

Pré-requisitos Antes de rodar o projeto, você precisa garantir que o ambiente está configurado corretamente. Para isso, siga os passos abaixo:

Python (versão 3.6 ou superior)

Bibliotecas: Instale as dependências necessárias com o pip:

pip install boto3 pandas openpyxl

Credenciais AWS: O projeto utiliza o SDK boto3 para acessar os buckets na AWS. Certifique-se de ter as credenciais configuradas corretamente no seu ambiente:

Defina as variáveis de ambiente AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY, ou configure o arquivo de credenciais usando o AWS CLI:

bash aws configure
