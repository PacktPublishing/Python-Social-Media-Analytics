"""

# Download
http://spark.apache.org/downloads.html

We will choose Spark 2.1.0 prebuilt hadoop 2.7
https://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz

## Extract files
tar xzf spark-2.1.1-bin-hadoop2.7.tgz
cd spark-2.1.1-bin-hadoop2.7

# Starting Standalone

## Start master
./sbin/start-master.sh

Get master url from http://localhost:8080
spark://master-hostname:7077

## Start slave
./sbin/start-slave.sh spark://master-hostname:7077

# Start Jupyter Notebook

## Install
pip install jupyter

## Start Notebook Server
jupyter notebook

## Create new notebook
"""

"""
## 
Using Spark
"""
# Make pyspark library accessible
import sys

spark_home = '/installation_path'
sys.path.insert(0, spark_home + "/python")

from pyspark import SparkConf, SparkContext

urlMaster = 'spark://master-hostname:7077'

conf = (
    SparkConf()
        .setAppName('spark.app')
        .setMaster(urlMaster)
)
sc = SparkContext(conf=conf)

"""
## 
Configuring Spark Context
"""
# Make pyspark library accessible
import sys

spark_home = '/installation_path'
sys.path.insert(0, spark_home + "/python")

from pyspark import SparkConf, SparkContext

driverConfs = [
    ('spark.cores.max', '24'),  # total number of cores
    ('spark.executor.memory', '10g')  # total memory per worker
]

conf = (
    SparkConf()
        .setAppName('spark.app')
        .setMaster(urlMaster)
        .setAll(driverConfs)
)
sc = SparkContext(conf=conf)

