import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.recommendation._

object data_input_format {
  def main(args:Array[String]): Unit ={
      //建立密集型矩阵
//    val vd=Vectors.dense(2,0,6)

      // 建立稀疏型矩阵
//    val vd=Vectors.sparse(10,Array(3,6),Array(9,7))
//    val vd=Vectors.sparse(10,Seq((3,100),(6,200)))
//    println(vd)

      //  建立LabeledPoint类型的数据
//    val positive=LabeledPoint(1.0,Vectors.dense(2,3,6))
//    val negative=LabeledPoint(0.0,Vectors.sparse(3,Array(0,2),Array(200,300)))
//    println(positive)
//    println(positive.label)

      //    Rating的创建方法，用于推荐系统中
    val rating=Rating(100,10,3.0)
    println(rating)

  }
}
