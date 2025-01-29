using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        string filePath = "input.txt";
        var lines = File.ReadAllLines(filePath);
        long result=0;
        foreach (var line in lines)
        {
            var parts = line.Split(':');
            if (parts.Length != 2) continue;

            long targetResult = long.Parse(parts[0].Trim());
            var numbers = Array.ConvertAll(parts[1].Trim().Split(' '), long.Parse);

            if (FindResult(numbers, targetResult))
            {
                result += targetResult;
            }
            else
            {
                
            }
        }
        Console.WriteLine(result);
    }

    static bool FindResult(long[] numbers, long target)
    {
        return TryCalculate(numbers, 1, numbers[0], target);
    }

    static bool TryCalculate(long[] numbers, int index, long currentResult, long target)
    {
        if (index == numbers.Length)
        {
            if (currentResult == target)
            {
                return true;
            }
            return false;
        }

        long nextNumber = numbers[index];

        if (TryCalculate(numbers, index + 1, currentResult + nextNumber, target))
        {
            return true;
        }

        if (TryCalculate(numbers, index + 1, currentResult * nextNumber, target))
        {
            return true;
        }

        return false;
    }
}
