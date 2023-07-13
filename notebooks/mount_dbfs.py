# Databricks notebook source
dbutils.fs.mkdirs("/mnt/dados")

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "303fd7aa-7a43-419d-a553-9c28061f1fee",
          "fs.azure.account.oauth2.client.secret": "1g_8Q~rXGwChiuTklx-UpgCKBClfU2qbfLOpRbW1",
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/609ea536-dbdf-4d28-a209-e6568275ab6d/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://imoveis@datalakemarcus.dfs.core.windows.net/",
  mount_point = "/mnt/dados",
  extra_configs = configs)
