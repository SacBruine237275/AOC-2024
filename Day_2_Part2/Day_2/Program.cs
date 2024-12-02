using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day_2
{
    public class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(ReadFile());
        }

        public static int ReadFile()
        {
            try
            {
                int safeCount = 0;
                using (StreamReader reader=File.OpenText("input.txt"))
                {
                    string line;
                    while ((line=reader.ReadLine())!=null)
                    {
                        int[] valueArray =Array.ConvertAll(line.Split(' '),int.Parse);
                        if(isSafe(valueArray))
                            safeCount++;
                        else
                        {
                            bool canBeSafe = false;
                            for(int i = 0; i < valueArray.Length; i++)
                            {
                                var modifiedArray = valueArray.Where((val, index) => index != i).ToArray();
                                if (isSafe((modifiedArray))) { 
                                    canBeSafe = true;
                                    break;
                                }
                            }
                            if (canBeSafe)
                                safeCount++;
                        }

                    }
                }
                return safeCount;
            }
            catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
                return 0;
            }
        }


        public static bool isSafe(int[] valueArray)
        {
            int validDifferenceCount = 0;
            bool increase = true;
            bool decrease = true;
            for (int i = 0; i < valueArray.Length - 1; i++)
            {
                int differenceBetwennValue = Math.Abs(valueArray[i] - valueArray[i + 1]);
                if (differenceBetwennValue == 0 || differenceBetwennValue > 3)
                    break;

                if (valueArray[i] < valueArray[i + 1])
                    decrease = false;
                if (valueArray[i] > valueArray[i + 1])
                    increase = false;
                validDifferenceCount++;
            }
            if (validDifferenceCount == valueArray.Length - 1 && (increase || decrease))
                return true;
            return false;
        }
    }
}
