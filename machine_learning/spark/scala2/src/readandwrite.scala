import java.io.PrintWriter
import scala.io.Source
import scala.collection.immutable
import scala.collection.mutable.{Set,Map}

object readandwrite {
  def main(args:Array[String]): Unit ={
    val university=Map("XMU"->"Xiamen university","THU"->"Tsinghua","PKU"->"Peking university")
    println(university("XMU"))
    university+=("FZ"->"FZ nuiversity")
    println(university)
    for(k<-university.values) println(k)
  }
}

