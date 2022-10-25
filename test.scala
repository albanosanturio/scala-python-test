object test {
    def main (args: Array [String]) =
        println("\n TEST DEF VAR VAL")
        
        println("\n TEST ARRAY")
        println("\n TEST LIST")
        println("\n TEST SEQ")
        println("\n Differences array/list/sequence")


        println("\n TEST DEF FUNC")

        val array1 = Array("A","B","C") 
        //println(array1)

        println("\n TEST WHILE")
        var i=0
        while (i<=10){
            println(i)
            i+=1
        }

        println("\n TEST FOR")
        val nums = Seq(20,30,40)
        for (n<-nums) println(n)

        val fruits = List("apple","banana","cherry")
        for (n<-nums) println(n)

        println("\n TEST MAP - .toLowerCase")
        val name = Seq("NAME1", "NAME2")
        val result1 = name.map(_.toLowerCase)
        val result2 = name.flatMap(_.toLowerCase)
        println("nomap: "+name)
        println("map: "+result1)
        println("flatmap: "+result2)

        
}

