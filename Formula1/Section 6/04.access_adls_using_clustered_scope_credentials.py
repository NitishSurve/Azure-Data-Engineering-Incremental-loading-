# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using cluster scoped credentials
# MAGIC 1. Set the spark config fs.azure.account.key in the cluster
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

spark.conf.set("fs.azure.account.key.formula1dl2397.dfs.core.windows.net",
               "qjcNBWywN1ynytOfnYUF9bHJQn0E807Qd3Pt6f2tbeNSSULMI0SqAPvS2ExJKZxjyutJlHqbum/p+AStA9eyIw==")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dl2397.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dl2397.dfs.core.windows.net"))