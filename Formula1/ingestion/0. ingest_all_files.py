# Databricks notebook source
dbutils.notebook.help()

# COMMAND ----------

v_result = dbutils.notebook.run("/Workspace/Users/nitishsurve887@gmail.com/Formula1/INGESTION_CSV_JSON/01. Ingest_circuit_files", 0, {"p_data_source" : "Ergast API"})

# COMMAND ----------

v_result

# COMMAND ----------

# DBTITLE 1,Cell 4
v_result = dbutils.notebook.run("/Workspace/Users/nitishsurve887@gmail.com/Formula1/INGESTION_CSV_JSON/02. ingest_race_files", 0, {"p_data_source" : "Ergast API"})

# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("/Workspace/Users/nitishsurve887@gmail.com/Formula1/INGESTION_CSV_JSON/03. ingest_constructors_file", 0, {"p_data_source" : "Ergast API"})


# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("/Workspace/Users/nitishsurve887@gmail.com/Formula1/INGESTION_CSV_JSON/04. ingest_drivers_file", 0, {"p_data_source" : "Ergast API"})


# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("/Workspace/Users/nitishsurve887@gmail.com/Formula1/INGESTION_CSV_JSON/05. ingest_results_file", 0, {"p_data_source" : "Ergast API"})


# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("/Workspace/Users/nitishsurve887@gmail.com/Formula1/INGESTION_CSV_JSON/06. ingest_pit_stops_file", 0, {"p_data_source" : "Ergast API"})


# COMMAND ----------

v_result

# COMMAND ----------

v_result = dbutils.notebook.run("/Workspace/Users/nitishsurve887@gmail.com/Formula1/INGESTION_CSV_JSON/07. ingest_lap_times_file", 0, {"p_data_source" : "Ergast API"})


# COMMAND ----------

v_result





# COMMAND ----------

v_result = dbutils.notebook.run("/Workspace/Users/nitishsurve887@gmail.com/Formula1/INGESTION_CSV_JSON/08. ingest_qualifying_file", 0, {"p_data_source" : "Ergast API"})

# COMMAND ----------

v_result