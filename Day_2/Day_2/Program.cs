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
            ReadFile();
        }

        public static void ReadFile()
        {
            try
            {
                Console.WriteLine(Directory.GetCurrentDirectory());
                using (StreamReader reader=File.OpenText("input.txt"))
                {
                    string line;
                    while((line=reader.ReadLine())!=null)
                    {
                        int[] valueArray =Array.ConvertAll(line.Split(' '),int.Parse);
                    }
                }
            }
            catch(Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
