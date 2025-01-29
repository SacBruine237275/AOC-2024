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

            if (FindResult(numbers, targetResult, out string expression))
            {
                result += targetResult;
            }
            else
            {
                
            }
        }
        Console.WriteLine(result);
    }

    static bool FindResult(long[] numbers, long target, out string expression)
    {
        expression = null;
        return TryCalculate(numbers, 1, numbers[0], $"{numbers[0]}", target, ref expression);
    }

    static bool TryCalculate(long[] numbers, int index, long currentResult, string currentExpression, long target, ref string validExpression)
    {
        if (index == numbers.Length)
        {
            if (currentResult == target)
            {
                validExpression = currentExpression;
                return true;
            }
            return false;
        }

        long nextNumber = numbers[index];

        // Test addition
        if (TryCalculate(numbers, index + 1, currentResult + nextNumber, $"{currentExpression} + {nextNumber}", target, ref validExpression))
        {
            return true;
        }

        // Test multiplication
        if (TryCalculate(numbers, index + 1, currentResult * nextNumber, $"{currentExpression} * {nextNumber}", target, ref validExpression))
        {
            return true;
        }
        
        if (TryCalculate(numbers, index + 1, long.Parse(currentResult.ToString() + nextNumber.ToString()), $"{currentExpression} || {nextNumber}", target, ref validExpression))
        {
            return true;
        }

        return false;
    }
}
