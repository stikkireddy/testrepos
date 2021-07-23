# Databricks notebook source
from custom_functions.main import main

main()

# COMMAND ----------

with open("./clusterspec.json", "r") as f:
  print(f.read())

# COMMAND ----------


