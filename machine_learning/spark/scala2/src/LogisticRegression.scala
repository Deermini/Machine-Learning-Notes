import org.apache.spark.{SparkConf,SparkContext}
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.classification.LogisticRegressionWithSGD

object LogisticRegression {
  def main(args:Array[String]){
    val conf=new SparkConf().setMaster("local[2]").setAppName("LogisticRession")
    conf.set("spark.testing.memory", "21474800000")
    val sc=new SparkContext(conf)
    val data=sc.textFile("F:\\projectfile\\sparkfile\\scala2\\data\\co7_logistic.txt")
    val parasedData=data.map{line=>val parts=line.split(" ")
      LabeledPoint(parts(0).toDouble,Vectors.dense(parts(1).split(" ").map(_.toDouble)))
    }.cache()
    val model=LogisticRegressionWithSGD.train(parasedData,50)
    val target=Vectors.dense(12)
    val result=model.predict(target)
    println(result)
  }
}
