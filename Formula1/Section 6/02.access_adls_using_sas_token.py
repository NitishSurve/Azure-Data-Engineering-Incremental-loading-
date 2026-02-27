# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using SAS Token
# MAGIC 1. Set the spark config for SAS Token
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

dbutils.secrets.list(scope = 'formula1_scope')

# COMMAND ----------

formula1dl2397_SAS_token =  dbutils.secrets.get(scope = 'formula1_scope', key = 'formula1dl2397-SAS-token')

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.formula1dl2397.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula1dl2397.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formula1dl.dfs.core.windows.net", formula1dl2397_SAS_token)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dl2397.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dl2397.dfs.core.windows.net/circuits.csv"))