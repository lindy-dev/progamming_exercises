// URLify 
var urlify = function(str, length){
    // have a pointer to check from start to end
    var strArr = str.split(''); 
    var pointer = 0; 
    while(pointer < str.length){
        if(strArr[pointer] === ' '){
            for(var i = str.length -1; i>pointer + 3; i--){
                strArr[i] = str[i-2]; 
            }
            str[pointer] = '%'; 
            str[pointer+1] = '2';
            str[pointer+2] = '0';

        }
        pointer++; 
    }
    return strArr.join(''); 
}; 

const urlify2 = (str) => {
    const convertToArray = str.trim().split(''); 
    for(let i in convertToArray){
        if(convertToArray[i] === ' '){
            convertToArray[i] = "%20"
        }

    }
    return convertToArray.join(''); 
}
