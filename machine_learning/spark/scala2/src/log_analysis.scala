import org.apache.spark.{SparkConf,SparkContext}


object log_analysis {
  def main(args:Array[String]):Unit={
    val conf=new SparkConf().setMaster("local").setAppName("log_analysis")
    conf.set("spark.testing.memory", "2147480000")
    val sc=new SparkContext(conf)
    val raw_logs=sc.textFile("F:\\projectfile\\sparkfile\\scala2\\data\\app.log")
//    raw_logs.foreach(println)
    val logs=raw_logs.map{line=>line.trim.toLowerCase()}
    val logs_count=logs.count()
    println(logs_count)

    val logs_filter=logs.filter(_.split(" ")(1)=="12")
//    logs_filter.foreach(println)
//    println(logs_filter.count())
    val fires_raw=logs.take(3)
    fires_raw.foreach(println)

    val length=logs.map{line=>line.size}
    val max_length=length.reduce{(a,b)=>if (a>b) a else b}
    println("max_length:",max_length)

    val xs=(1 to 100).toList
    println("xs.size:",xs.size)

//    def
    val log_pair=logs.map{line=>(line.split(" ")(1),1)}
//    val countbykey=log_pair.reduceByKey((x,y)=>x+y)
    val countbykey=log_pair.countByKey()
//    println(countbykey)
    countbykey.foreach(println)
  }
}
