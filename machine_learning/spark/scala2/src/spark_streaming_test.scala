package org.apache.spark.examples.streaming

import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.storage.StorageLevel
import org.apache.spark.streaming._
import org.apache.spark._

object spark_streaming_test {
  def main(args:Array[String]):Unit={
//    StreamingExamples.setStreamingLogLevels()
    val conf=new SparkConf().setMaster("local").setAppName("spark_streaming_test")
    conf.set("spark.testing.memory", "2147480000")
    val sc=new SparkContext(conf)
    val batchInterval=10
    val ssc=new StreamingContext(sc,Seconds(batchInterval))
    val lines=ssc.textFileStream("F:\\projectfile\\sparkfile\\new_document")
    val word=lines.flatMap(_.split(" "))
    val wordcount=word.map(x=>(x,1)).reduceByKey(_+_)
    wordcount.print()
    ssc.start()
    ssc.awaitTermination()
//    val rdd=sc.parallelize(List(1,2,3,4,1,2,3,1,2,1))
//    val counts=rdd.countByValue()
//    counts.foreach(println)
  }
}



