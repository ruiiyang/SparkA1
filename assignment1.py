import pyspark
from pyspark.sql import SparkSession

#Create SparkSession
spark = SparkSession.builder \
.master("local") \
.appName("MySparkApp") \
.getOrCreate()
df= spark.read.format("csv").option("header", True).load("lab_dataset.csv")


