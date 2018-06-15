import org.apache.spark.mllib.clustering.KMeans
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.{SparkConf,SparkContext}
import org.apache.spark.mllib.util.MLUtils

object Kmeans {
  def main(args:Array[String] ){
    val conf=new SparkConf().setMaster("local").setAppName("Kmeans")
    conf.set("spark.testing.memory", "21474800000")
    val sc=new SparkContext(conf)
    val data=sc.textFile("F:\\projectfile\\sparkfile\\scala2\\data\\kmeans.txt")
//    val data=MLUtils.loadLibSVMFile(sc,"F:\\projectfile\\sparkfile\\scala2\\data\\kmeans.txt")
    val parased=data.map(s=>Vectors.dense(s.split(" ").map(_.toDouble))).cache()
    val numcluster=2
    val numiter=20
    val model =KMeans.train(parased,numcluster,numiter)
    model.clusterCenters.foreach(println)
    println(model.computeCost(parased))
    model.predict(parased).foreach(print)
//    val lengths=data.map{l=>l.length}
//    lengths.foreach(println)
  }
}
