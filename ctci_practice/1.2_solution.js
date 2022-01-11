// Check permutation 
// Given two strings, write a method to decide if one is a permutation of the other 

var checkPermute = function(string1, string2){
    //if different lengths, return false 
    if (string1.length !== string2.length){
        return false; 
    } else {
        var sortedString1 = string1.split('').sort().join(''); 
        var sortedString2 = string2.split('').sort().join(''); 
        return sortedString1 === sortedString2;
    }


};

// Tests 

console.log(checkPermute('aba','aab'), true); 

console.log(checkPermute('aba','aaba'), false); 

console.log(checkPermute('aba', 'aa'), false);  