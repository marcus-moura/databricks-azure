# Projeto de Orquestração de ELT no Azure Databricks com o Azure Data Factory

Este é um projeto de demonstração sobre como utilizar o Azure Data Factory (ADF) como um orquestrador para executar e monitorar fluxos ELT (Extração, Carregamento e Transformação) no Azure Databricks. Neste projeto, estaremos criando pipelines que acionam os notebooks do Azure Databricks, permitindo a execução de tarefas de processamento de dados complexas e escaláveis, além de carregar os dados resultantes em destinos desejados.

### Descrição do Projeto
O objetivo deste projeto é mostrar como o Azure Data Factory pode ser utilizado para criar fluxos de trabalho ELT que envolvem a extração de dados de fontes externas, o processamento e transformação desses dados usando notebooks do Azure Databricks e, finalmente, o carregamento dos dados transformados em destinos desejados, como o Azure SQL Database ou o Azure Data Lake Gen2.

### Pré-requisitos
Antes de começar a trabalhar com este projeto, certifique-se de ter o seguinte:

1. Conta do Azure: Você precisa ter uma conta ativa do Microsoft Azure para criar e configurar os recursos necessários.

2. Azure Data Factory: Crie uma instância do Azure Data Factory no portal do Azure para orquestrar os pipelines.

3. Azure Databricks: Provisione um workspace do Azure Databricks no Azure e garanta que você tenha as permissões necessárias para executar notebooks.

### Avisos

Este projeto é apenas para fins de demonstração e aprendizado.

### Recursos Adicionais
- [Documentação do Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/)
- [Documentação do Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/)
- [Integração do Azure Data Factory com Azure Databricks](https://learn.microsoft.com/en-us/azure/data-factory/transform-data-using-databricks-notebook)
