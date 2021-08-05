# Databricks notebook source


# COMMAND ----------

python git clone
python setup bdist wheel
push to s3

# COMMAND ----------

# DBTITLE 1,Notebooks in repo get updated in Prod, Job config in prod get updated
url + token
fetch-pull repos api code
push job config to be latest

# COMMAND ----------

from custom_functions.main import main

main()

# COMMAND ----------

with open("./custom_functions/funcs.py", "r") as f:
  data = f.read()

# COMMAND ----------

with open("./clusterspec.json", "r") as f:
  print(f.read())

# COMMAND ----------


