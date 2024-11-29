Validação Automática de Buckets AWS e Download de Arquivos com Hospedagem no OneDrive

Este projeto tem como objetivo automatizar dois processos essenciais:

    A validação de buckets na AWS S3, verificando se estão vazios ou contêm arquivos.
    O download de arquivos e sua hospedagem automática no OneDrive, garantindo o armazenamento seguro e organizado dos dados.

As automações foram desenvolvidas utilizando Python com as bibliotecas boto3, pandas, openpyxl e onedrive-sdk para proporcionar uma integração eficiente e prática entre os serviços.
Pré-requisitos

Antes de rodar o projeto, você precisa garantir que o ambiente está configurado corretamente. Para isso, siga os passos abaixo:

    Python: Certifique-se de que possui a versão 3.6 ou superior instalada.

    Bibliotecas: Instale as dependências necessárias com o pip:

pip install boto3 pandas openpyxl onedrive-sdk

    Credenciais AWS: O projeto utiliza o SDK boto3 para acessar os buckets na AWS. Certifique-se de ter as credenciais configuradas corretamente no seu ambiente:

        Defina as variáveis de ambiente AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY, ou configure o arquivo de credenciais usando o AWS CLI:

        aws configure

    Credenciais OneDrive: Para integração com o OneDrive, configure as credenciais da API da Microsoft. Siga as instruções de registro de aplicativos no portal do Azure para obter o client_id, client_secret e redirect_uri. Certifique-se de incluir estas informações no código ou no ambiente de execução.

Automação de Validação de Buckets

A automação analisa os buckets na AWS S3 para verificar se estão vazios ou contêm arquivos, gerando relatórios detalhados em formato Excel para facilitar a consulta.
Automação de Download e Hospedagem no OneDrive

Esta funcionalidade realiza o download de arquivos diretamente da AWS S3 e faz o upload automático para o OneDrive, utilizando as credenciais configuradas. É possível organizar os arquivos em pastas específicas dentro do OneDrive, garantindo acesso fácil e seguro aos dados.
