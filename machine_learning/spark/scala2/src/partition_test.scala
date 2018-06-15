import org.apache.spark.{Partitioner,SparkConf,SparkContext}

class UsridPartitions(numParts:Int) extends Partitioner{
  override def numPartitions: Int = numParts
  override def getPartition(key: Any): Int = {
    key.toString.toInt%10
  }
}

object partition_test {
  def main(arg:Array[String]): Unit ={
    val conf = new SparkConf().setMaster("local").setAppName("helloscala")
    conf.set("spark.testing.memory", "2147480000")
    val sc = new SparkContext(conf)
    val data=sc.parallelize(1 to 10,5)
    data.map((_,1)).partitionBy(new UsridPartitions(10)).map(_._1).saveAsTextFile("F:\\projectfile\\sparkfile\\scala2\\data\\output")
  }
}
