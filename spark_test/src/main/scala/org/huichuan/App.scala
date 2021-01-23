package org.huichuan

import scala.collection.mutable.ArrayBuffer

/**
 * Hello world!
 *
 */
object App extends App {
  println("Hello World!")

  val s = Set(1, 2, 3)

  println(s)

  val s1 = scala.collection.mutable.Set(1, 2, 3, 4)
  val s2 = scala.collection.mutable.SortedSet(1, 2, 3, 4)

  val userEmbeddings = new ArrayBuffer[(String, Array[Float])]()

  userEmbeddings.append(("Hello,World!".toString(),Array[Float](1,2,3)))
  println(userEmbeddings)

  var pairSeq = Seq[(String, String)]()

  pairSeq = pairSeq :+ ("previousItem", "12")

  println(pairSeq)
  //  println(s2)


  s1 += 5

  println(s1)
}
