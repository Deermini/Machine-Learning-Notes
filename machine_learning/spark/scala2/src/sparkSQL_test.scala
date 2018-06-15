import org.apache.spark.sql._
import org.apache.spark._

object sparkSQL_test {
  case class Email(Sender:String,recepient:String,age:Int,subject:String,body:String)
  case class Employee(name:String,age:Int,gender:String)

  def main(args:Array[String]): Unit ={
    val conf = new SparkConf().setMaster("local[*]").setAppName("helloscala")
    conf.set("spark.testing.memory", "2147480000")
    val sc = new SparkContext(conf)
    val sqlContext=new SQLContext(sc)
    import sqlContext.implicits._

//    行的使用
//    val row1=Row("Barack Obama","President","United States")
//    val row2=Row("David Cameron","Prime Minster","United Kingdom")
//    val presidentName=row1.getString(0)
//    val country=row1.getString(2)
//    println(presidentName)
//    println(country)

    //    toDF方法
//    import sqlContext.implicits._
//    val rowsRDD=sc.textFile("F:\\projectfile\\sparkfile\\scala2\\data\\employee.csv")
//    val employeeRDD=rowsRDD.map{row=>row.split(",")}.map{cols=>Employee(cols(0),cols(1).trim.toInt,cols(2))}
//    val employeeDF=employeeRDD.toDF()
//    println(employeeDF.show())

//      createDataFrame
//    import org.apache.spark.sql.types._
//    val linesRDD=sc.textFile("F:\\projectfile\\sparkfile\\scala2\\data\\employee.csv")
//    val rowsRDD=linesRDD.map{row=>row.split(",")}.map{cols=>Row(cols(0),cols(1).trim.toInt,cols(2))}
//    val schema=StructType(List(
//      StructField("name",StringType,true),
//      StructField("age",IntegerType,true),
//      StructField("gender",StringType,true)
//    ))
//    val employeesDF=sqlContext.createDataFrame(rowsRDD,schema)
//    println(employeesDF.show())
//    println(employeesDF.printSchema)
//    employeesDF.columns.foreach(println)

//    读取json文件
//    val jsonDF=sqlContext.read.json("F:\\projectfile\\sparkfile\\scala2\\data\\people.json")
//    println(jsonDF.show())
//    加速创建过程
//    import org.apache.spark.sql.types._
//    val userSchema=StructType(List(
//      StructField("name",StringType,false),
//      StructField("age",IntegerType,false)
//    ))
//    val jsonDF=sqlContext.read.schema(userSchema).json("F:\\projectfile\\sparkfile\\scala2\\data\\people.json")
//    println(jsonDF.show())
//    println(jsonDF.columns)

//    存储文件
//    val textfile=sc.textFile("F:\\projectfile\\sparkfile\\scala2\\data\\testCorrectX.txt")
//    textfile.saveAsTextFile("F:\\projectfile\\sparkfile\\scala2\\data\\testCorrectXback.txt")

//    dataframe格式的操作 ：distinct、explode、filter、groupby
    val emails=List(Email("James","Mary",26,"back","just got back from vacation"),
                    Email("Zim","xiaolu",28,"report","i am a GAN producer"),
                    Email("Tim","xiaolu",28,"report","i am a GAN producer"),
      Email("James","Mary",26,"back","just got back from vacation"),
      Email("Zim","xiaolu",9,"report","i am a GAN producer"),
      Email("Tim","xiaolu",2,"report","i am a GAN producer"),
      Email("James","Mary",6,"back","just got back from vacation"),
      Email("Zim","xiaolu",29,"report","i am a GAN producer"),
      Email("Tim","xiaolu",78,"report","i am a GAN producer"),
      Email("Tim","xiaolu",38,"report","i am a GAN producer")
    )
    val emailsDF=sc.parallelize(emails).toDF()
//    val wordDF=emailsDF.distinct.explode("body","word"){body:String=>body.split(" ")}
//    wordDF.show()

//    val ageDF=emailsDF.filter("age>25")
//    val ageDF=emailsDF.filter($"age">25)
//    ageDF.show()

      //groupBy、orderBy
//    val groupByDF=emailsDF.groupBy("recepient").count()
//    groupByDF.show()
//    val orderbyDF=emailsDF.orderBy("Sender")
//    orderbyDF.show()

//    val dfArray=emailsDF.randomSplit(Array(0.6,0.2,0.2))
//    println(dfArray(0).count)
//    println(dfArray(1).count)
//    println(dfArray(2).count)

//    val sampleDF=emailsDF.sample(true,0.30)
//    println(sampleDF.count)

//    val ageDF=emailsDF.select(emailsDF("age")+1)
//    val ageDF=emailsDF.select($"age"+1)
    val ageDF=emailsDF.selectExpr("age+10")
    ageDF.show()

  }
}
