import org.apache.spark.{SparkConf,SparkContext}

object sparkapi {
  def main(args:Array[String]): Unit ={
    val conf=new SparkConf().setMaster("local").setAppName("Kmeans")
    conf.set("spark.testing.memory", "21474800000")
    val sc=new SparkContext(conf)
    val arr=sc.parallelize(Array(1,2,3,4))
    val result=arr.map(x=>x+1).collect()
    result.foreach(println)
  }
}
