import org.apache.spark.{SparkContext,SparkConf}

object wordcount {
  def main(args:Array[String]){
    val conf=new SparkConf().setMaster("local").setAppName("wordcount")
    conf.set("spark.testing.memory", "2147480000")
    val sc=new SparkContext(conf)
    val lines=sc.textFile("F:\\projectfile\\sparkfile\\scala2\\data\\inputFile.txt")
//    lines.flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).collect().foreach(println)
    val wordcounts=lines.flatMap{line=>line.split(" ")}.map(word=>(word,1)).reduceByKey(_+_)
//    wordcounts.foreach(println)
    wordcounts.saveAsTextFile("data/wordcounts2")
    val result=sc.textFile("data/wordcounts2")
    result.foreach(println)
  }
}

