using System;

namespace MyFirstProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            // tömb = egy változó ami több értéket tud tárolni. megadott méret

            //String[] cars = {"BMW", "Mustang", "Corvette"};

            String[] kocsik = new string[3];

            kocsik[0] = "Tesla";
            kocsik[1] = "Mustang";
            kocsik[2] = "Corvette";

            for (int i = 0; i < kocsik.Length; i++)
            {
                Console.WriteLine(kocsik[i]);
            }

            Console.ReadKey();
        }
    }
}

