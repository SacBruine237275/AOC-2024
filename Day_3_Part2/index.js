var fs = require('fs-extra')

var data = fs.readFileSync('input.txt', 'utf8');
var result = 0;
var readBool = true;
const regex = /(mul\(\s*\d+\s*,\s*\d+\s*\))|(do\(\))|(don't\(\))/g;
while ((array = regex.exec(data)) !== null) {
    if(array[2]!=undefined){
     readBool = true;
    }
    if(array[3]!=undefined){
        readBool = false;
       }
    const regexForHaveNumber = /mul\(\s*(\d+)\s*,\s*(\d+)\s*\)/g;
    while (((match = regexForHaveNumber.exec(array[0]))) != null) {
        if (readBool) {
            const number1 = parseInt(match[1], 10)
            const number2 = parseInt(match[2], 10)
            result += number1 * number2;
        }
    }
}

console.log(result)
