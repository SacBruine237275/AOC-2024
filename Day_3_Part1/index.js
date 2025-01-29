var fs=require('fs-extra')

var data = fs.readFileSync('input.txt', 'utf8');
var result=0;
const regex = /mul\(\s*\d+\s*,\s*\d+\s*\)/g;
while ((array = regex.exec(data)) !== null) {
    const regexForHaveNumber = /mul\(\s*(\d+)\s*,\s*(\d+)\s*\)/g;
    while(((match=regexForHaveNumber.exec(array[0])))!=null){
        const number1=parseInt(match[1],10)
        const number2=parseInt(match[2],10)
        result+=number1*number2;
    }
  }

  console.log(result)
