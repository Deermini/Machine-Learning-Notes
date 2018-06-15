import org.apache.spark.mllib.linalg.{Vector,Vectors}
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark._
import org.apache.spark.mllib.util.MLUtils
import org.apache.spark.mllib.linalg.{Matrix,Matrices}
import org.apache.spark.mllib.linalg.distributed.{RowMatrix,IndexedRow,IndexedRowMatrix}
import org.apache.spark.mllib.stat.Statistics
import org.apache.spark.mllib.random.RandomRDDs._

object helloscala {
  def main(args: Array[String]) {
    val conf = new SparkConf().setMaster("local").setAppName("helloscala")
    conf.set("spark.testing.memory", "2147480000")
    val sc = new SparkContext(conf)
//    val randomNUM=normalRDD(sc,100)
//    randomNUM.foreach(println)

    //    join()函数的测试
//    val pairrdd1=sc.parallelize(List(("a",1),("b",2),("c",3)))
//    val pairrdd2=sc.parallelize(List(("b","second"),("c","third"),("d","fourth")))
//    val joinrdd=pairrdd1.join(pairrdd2)
//    val joinrdd=pairrdd1.leftOuterJoin(pairrdd2)
//    val joinrdd=pairrdd1.rightOuterJoin(pairrdd2)
//    val joinrdd=pairrdd1.fullOuterJoin(pairrdd2)
//    joinrdd.foreach(println)

    //广播变量的使用
//    val content=sc.parallelize(List(1,2,3,4))
//    val broadcastVar=sc.broadcast(3)
//    val content_b=content.map(x=>x*broadcastVar.value)
//    content_b.foreach(println)

//    求和
//    val content=sc.parallelize(List(1,2,3,4)).sum()
//    print(content)


  }
}