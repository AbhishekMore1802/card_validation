using System;
 
class GFG {
     

static bool ccvalidation(String cardnumber)
{
    int totaldigits = cardnumber.Length;
 
    int sumofdigit = 0;
    bool isSecond = false;
    for (int i = totaldigits - 1; i >= 0; i--) 
    {
 
         int d = cardnumber[i] - '0';
 
        if (isSecond == true)
            d = d * 2;
 
     
        sumofdigit += d / 10;
        sumofdigit += d % 10;
 
        isSecond = !isSecond;
    }
    return (sumofdigit % 10 == 0);
}
 
    static public void Main()
    {
        String cardnumber = "79927398713";
        if (ccvalidation(cardnumber))
            Console.WriteLine("This is a valid card");
        else
            Console.WriteLine("This is not a valid card");
     
    }
}