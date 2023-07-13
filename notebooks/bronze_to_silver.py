# Databricks notebook source
dbutils.fs.ls("mnt/dados/datalake-prod-bronze")

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

path_source = "dbfs:/mnt/dados/datalake-prod-bronze/dataset_imoveis/"
path_silver = "dbfs:/mnt/dados/datalake-prod-silver/"

# COMMAND ----------

DfBronze = spark.read.load(path_source)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Flatten columns

# COMMAND ----------

DfSilver = DfBronze.select("anuncio.*")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Details Columns

# COMMAND ----------

DfDetails = DfSilver.select(
    col('id'),
    col('andar'),
    col('area_total').getItem(0).alias("area_total"),
    col('area_util').getItem(0).alias("area_util"),
    col('banheiros').getItem(0).alias("banheiros"),
    col('caracteristicas'),
    col('endereco.*'),
    col('quartos').getItem(0).alias("quartos"),
    col('suites').getItem(0).alias("suites"),
    col('tipo_anuncio'),
    col('tipo_unidade'),
    col('tipo_uso'),
    col('vaga').getItem(0).alias("vaga"),
    explode_outer(col('valores')).alias("values"))

DfDetails = DfDetails.select("*", "values.*")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Drop Columns

# COMMAND ----------

DfFinal = DfDetails.drop("caracteristicas", "values")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Save bronze layer

# COMMAND ----------

DfFinal.write.format("delta").mode("overwrite").save(f"{path_silver}/dataset_imoveis")
