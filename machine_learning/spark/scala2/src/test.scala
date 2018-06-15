import org.apache.spark.mllib.clustering.KMeans
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.{SparkConf,SparkContext}
import org.apache.spark.mllib.util.MLUtils


object test {
  def main(args:Array[String]): Unit ={
    def add(firstinput:Int,secondinput:Int):Int={
      val sum=firstinput+secondinput
      sum
    }
//    println(add(1,2))
//    闭包
    def encodewithseed(num:Int,seed:Int):Long= {
      def encode(n: Int, f: (Int) => Long): Long = {
        val x = n * 10
        f(x)
      }
      val result=encode(10,(x:Int)=>(x+seed))
      result
    }
    val result2=encodewithseed(1,12)
//    println(result2)
//    类的写法
    case class Car(mk:String,ml:String,cr:String){
      val make=mk
      val model=ml
      var color=cr
      def repaint(newcolor:String)={
        color=newcolor
      }
    }
    val mustang=Car("Ford","Mustang","Red")
    val corvettr=Car("GM","Corvette","Black")
    corvettr.repaint("red")
//    println(corvettr.color)

    def f(x:Int,y:Int,operator:String):Double={
      operator match{
        case "+"=>x+y
        case "-"=>x-y
        case "*"=>x*y
        case "/"=>x/y.toDouble
      }
    }
    val sum=f(10,5,"+")
    val product=f(10,5,"*")
//    println(sum)
//    println(product)
//    println(10.+(3))

    trait Shape{
      def area():Int
    }
    class Square(length:Int) extends Shape{
      def area=length*length
    }
//    val square=new Square(10)
//    val area=square.area
//    println(area)

    def colorcode(color:String):Option[Int]={
      color match{
        case "red"=>Some(1)
        case "blue"=>Some(2)
        case "green"=>Some(3)
        case _=>None
      }
    }
//    val code=colorcode("orange")
//    code match{
//      case Some(c)=>println("code for orange is:"+c)
//      case None =>println("code not defined for orange")
//    }

//    val arr=Array(10,20,30,40)
//    arr(0)=50
//    val first=arr(0)
//    println(arr(2))

//    val arr=Array(10,20,30,40)
//    val xs=List(10,20,30,40)
//    val ys=(1 to 100).toList
//    val zs=arr.toList
//    println(zs)

//    val v1=Vector(0,10,20,30,40)
//    val v2=v1:+50
//    val v3=v2:+60
//    val v4=v3(4)
//    val v5=v3(5)
//    println(v5)

//    val capitals=Map("jiangxi"->"nanchan","fujian"->"xiamen")
//    val jxcapital=capitals("jiangxi")
//    println(jxcapital)

//    val xs=List(1,2,3,4)
//    val ys=xs.map(_*10.0)
//    println(ys)

//    val str="1 2 3 4"
//    val singlespace=" "
//    val content=str.split(singlespace)
//    val arrayofchars=content.flatMap(_.toList)
//    println(content)
//    println(arrayofchars)

//    val xs=(1 to 100).toList
//    val even=xs.filter(_%2==0)
//    println(even)

//    val str="scala is fun".split(" ")
//    str.foreach(println)

//    val xs=List(2,4,6,8,10)
//    val sum=xs reduce {(x,y)=>x+y}
//    println(sum)

//    val str="scala is fun".split(" ")
//    val longestword=str.reduce((w1,w2)=> if(w1.length>w2.length) w1 else w2)
//    println(longestword)


  }
}


