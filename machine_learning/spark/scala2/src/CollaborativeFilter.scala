import org.apache.spark._
import org.apache.spark.mllib.recommendation.{ALS,Rating}

object CollaborativeFilter {
  def main(args:Array[String]): Unit ={
    val conf=new SparkConf().setMaster("local").setAppName("CollaborativeFilter")
    conf.set("spark.testing.memory", "21474800000")
    val sc=new SparkContext(conf)
    val data=sc.textFile("F:\\projectfile\\sparkfile\\scala2\\data\\user_item.txt")
    val ratings=data.map(_.split(" ") match{
      case Array(user,item,rate)=>Rating(user.toInt,item.toInt,rate.toDouble)
    })
    val rank=2
    val numiterations=6
    val model=ALS.train(ratings,rank,numiterations,0.001)
    var rs=model.recommendProducts(2,1)
    rs.foreach(println)
  }
}
