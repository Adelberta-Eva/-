import findspark
findspark.init()
# 在spark前，添加此代码
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCount").getOrCreate()
spark.sparkContext.textFile("C:/Users/HONOR/Desktop/word.txt") \
    .flatMap(lambda x: x.split(' ')) \
    .map(lambda x: (x, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .foreach(print)
