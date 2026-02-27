# Databricks notebook source
dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()   

# COMMAND ----------

dbutils.secrets.list(scope = 'formula1_scope')

# COMMAND ----------

dbutils.secrets.get(scope = 'formula1_scope', key = 'formula1dl2397-account-key')