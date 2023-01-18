using System;

namespace MyFirstProgram
{
    class Program
    {
        static void Main(string[] args)
        {

            // while loop = addig ismétli a kódot amíg a feltétel megfelel a paramétereknek
          
            String neve = "";

            while (neve == "")
            {
                Console.Write("Enter your name: ");
                neve = Console.ReadLine();
            }

            Console.WriteLine("Hello " + neve);

            Console.ReadKey();



            // for loop = annyiszor futassa le a kódót amig a megadott érték/értékek igazak

            // Felszámolás 10-ig
            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine(i);
            }

            // Leszámolás 10-ig
            for (int i = 10; i > 0; i--)
            {
                Console.WriteLine(i);
            }

            Console.ReadKey();
        }
    }
}
