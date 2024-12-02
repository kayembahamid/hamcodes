// Function to add 7 to a given number

function add7(n){
    return n =+ 7; 
}

// Function to multiply two numbers

function multiply(n1, n2) {
    product = n1 * n2 
    return product;
}

// Function to capitalize only the first letter of a string

function capitalize(str) {
   return str.charAt(0).toUpperCase() + str.slice(1).lowerCase();

}

// Function to return the last letter of a string
function lastLetter(str){
    return str.charAt(str.length - 1);
}

// Example of usage:
console.log(add7(7));
console.log(multiply(3, 4));
console.log(capitalize("hELLo"));
console.log(lastLetter("abcd"))