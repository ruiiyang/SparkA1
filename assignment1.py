
import pyspark
from pyspark.sql import SparkSession

#Create SparkSession
spark = SparkSession.builder \
.master("local") \
.appName("MySparkApp") \
.getOrCreate()
df= spark.read.format("csv").option("header", True).load("./assignment1/lab_dataset.csv")
df.show()
spark.stop()