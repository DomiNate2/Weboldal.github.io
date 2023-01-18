class Bank
{
    public void Feldolgozas(int o)
    {
        if (o < 0)
        {
            Console.WriteLine("Nincs ilyen összeg.");
        }
        else
        {
            if (o >= 0 && o <= 5000 && o % 5 == 0)
                Console.WriteLine("Jó a megadott összeg. Nincs visszajáró!");
            else if (o > 5000)
                Console.WriteLine("A visszajáró: " + (o - 5000));
            else
                Console.WriteLine("Az összeg nem osztható 5-tel.");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        var bank = new Bank();
        Console.WriteLine("Adjon meg egy összeget: ");
        int k = int.Parse(Console.ReadLine());
        bank.Feldolgozas(k);
    }
}
