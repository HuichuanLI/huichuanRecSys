import findspark

findspark.init("/Users/hui/Desktop/bigdata/spark-2.4.4-bin-hadoop2.7")

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import pyspark.sql as sql
from pyspark.sql.functions import *
from pyspark.sql.types import *
from collections import defaultdict
from pyspark.sql import functions as F
import time

if __name__ == "__main__":
    conf = SparkConf().setAppName('helloworld').setMaster('local')
    # spark = SparkSession.builder.config(conf=conf).getOrCreate()
    sc = SparkContext(conf=conf)
    """
        创建RDD:
        方式一：
        
    """
    datas = ["hadoop spark", "spark hive spark sql", "spark hadoop sql spark"]
    rdd = sc.paralleize(datas)

    time.sleep(10000)
    sc.stop()
