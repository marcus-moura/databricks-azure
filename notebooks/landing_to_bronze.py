# Databricks notebook source
dbutils.fs.ls("mnt/dados/datalake-prod-landing")

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

path_source = "dbfs:/mnt/dados/datalake-prod-landing/dados_brutos_imoveis.json"
path_bronze = "dbfs:/mnt/dados/datalake-prod-bronze/"

# COMMAND ----------

DfLanding = spark.read.json(path_source)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Drop Columns

# COMMAND ----------

DfLanding = DfLanding.drop("imagens","usuario")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create column id

# COMMAND ----------

DfBronze = DfLanding.withColumn("id", col("anuncio.id"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Save bronze layer

# COMMAND ----------

DfBronze.write.format("delta").mode("overwrite").save(f"{path_bronze}/dataset_imoveis")
