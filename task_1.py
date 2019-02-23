from pyspark import SparkContext, SparkConf
import sys, getopt

conf = SparkConf().setAppName('Big Data project exercise1')
sc = SparkContext(conf = conf)

artists_RDD = sc.textFile("/Users/hansedvardhafskolt/Desktop/artists.csv")

artists_RDD.map(lambda line: line[3]).distinct().count()

