import org.apache.spark.mllib.classification.SVMWithSGD
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LinearRegressionWithSGD
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.mllib.util.MLUtils

object machion_learning {
    def main(args:Array[String]): Unit ={
      val conf=new SparkConf().setMaster("local").setAppName("machine_learning")
      val sc=new SparkContext(conf)
      val lines=sc.textFile("F:\\projectfile\\sparkfile\\scala2\\data\\kmeans.txt")
      val labeledpoints=lines.map{line=>
        val Array(rawlabel,rawFeatures)=line.split(",")
        val features=rawFeatures.split(" ").map{_.toDouble}
        LabeledPoint(rawlabel.toDouble,Vectors.dense(features))
      }.cache()

      val numIterations=100
      val lr_model=LinearRegressionWithSGD.train(labeledpoints,numIterations)
      // 查看模型参数
      val intercept=lr_model.intercept
      val weights=lr_model.weights

      // 求准确率
      val observationAndprediction=labeledpoints.map{observation=>
        val prediction=lr_model.predict(observation.features)
        (observation.label,prediction)
      }

      // 计算准确率   均方误差（meansquareError）
      val squareError=observationAndprediction.map{case(actual,predicted)=>
          math.pow((actual-predicted),2)
      }
      val meansquareError=squareError.mean()
      println("meansquareError:",meansquareError)

      // 利用LIBSVM格式载入数据，切分训练集和验证集
      val labeledPoints=MLUtils.loadLibSVMFile(sc,"F:\\projectfile\\sparkfile\\scala2\\data\\kmeans.txt")
      val Array(trainingData,validationData,testData)=labeledPoints.randomSplit(Array(0.6,0.2,0.2))
      val numIterations2=100
      val SVMmodel=SVMWithSGD.train(trainingData,numIterations2)
      // 对测试数据进行预测
      val predictionANDtruelabels=testData.map{testdata=>
        val prediction=SVMmodel.predict(testdata.features)
        (prediction,testdata.label)
      }
      val fivepredANDtruelabel=predictionANDtruelabels.take(5)
      // 另一种单独预测的方法
      val predictionlabels=SVMmodel.predict(testData.map{_.features})
      val fivepredictionlabels=predictionANDtruelabels.take(5)

    }
}
