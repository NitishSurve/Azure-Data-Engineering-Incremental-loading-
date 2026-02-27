# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC #### MANAGED TABLES demo

# COMMAND ----------

# MAGIC %run "../includes/configuration"

# COMMAND ----------

race_results_df = spark.read.parquet(f"{presentation_folder_path}/race_results")

# COMMAND ----------

    race_results_df.write.format("parquet").saveAsTable("demo.race_results_python")

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_database()

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES;

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended race_results_python;

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE OR REPLACE TABLE
# MAGIC race_results_sql
# MAGIC AS
# MAGIC select * from demo.race_results_python
# MAGIC where race_year = 2020;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES

# COMMAND ----------

# MAGIC %sql 
# MAGIC DROP TABLE demo.race_results_sql;

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables;

# COMMAND ----------

race_results_df.write.format("parquet").option("path",f"{presentation_folder_path}/race_results_ext_py").saveAsTable("demo.race_results_ext_py")

# COMMAND ----------

# MAGIC %sql
# MAGIC desc extended demo.race_results_ext_py;

# COMMAND ----------

# MAGIC %sql show tables

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC drop table race_results_ext_py;

# COMMAND ----------

