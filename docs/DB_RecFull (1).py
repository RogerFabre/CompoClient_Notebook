# Databricks notebook source
# %python
# # PRE
# dbutils.fs.mount(
#   source = "wasbs://recomanadorfulleto@stabdpredatalake.blob.core.windows.net",
#   mount_point = "/mnt/recfull",
#   extra_configs = {"fs.azure.account.key.stabdpredatalake.blob.core.windows.net":dbutils.secrets.get(
#     scope = "databricks-pre",
#     key = "aiduser")
#   }
# )

# COMMAND ----------

# MAGIC %python
# MAGIC # PRO
# MAGIC dbutils.fs.mount(
# MAGIC   source = "wasbs://recomanadorfulleto@stabdproddatalake.blob.core.windows.net",
# MAGIC   mount_point = "/mnt/recfull",
# MAGIC   extra_configs = {"fs.azure.account.key.stabdproddatalake.blob.core.windows.net":dbutils.secrets.get(
# MAGIC     scope = "databricks-pro",
# MAGIC     key = "aiduser")
# MAGIC   }
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE RECFULL LOCATION "/mnt/recfull"

# COMMAND ----------


