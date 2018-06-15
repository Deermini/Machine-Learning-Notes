
//Spark Streaming - 为程序员服务  http://ju.outofmemory.cn/entry/96018
//package com.debugo.example

import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.SparkConf

object wordcountstreaming {
  def main(args: Array[String]): Unit ={
    val sparkConf = new SparkConf().setAppName("HDFSWordCount").setMaster("local")
    sparkConf.set("spark.testing.memory", "2147480000")
    //create the streaming context
    val  ssc = new StreamingContext(sparkConf, Seconds(30))

    //process file when new file be found.
    val lines = ssc.textFileStream("F:\\projectfile\\sparkfile\\data")
    val words = lines.flatMap(_.split(" "))
    val wordCounts = words.map(x => (x, 1)).reduceByKey(_ + _)
    wordCounts.print()
    ssc.start()
    ssc.awaitTermination()
  }
}
