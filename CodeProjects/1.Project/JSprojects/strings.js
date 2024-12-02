const string = "The revolution will not be televised.";
console.log(string)

const single = 'single quotes';
const double = "Double quotes";
const backtick = `Backticks`;
console.log(single);
console.log(double);
console.log(backtick);

const name1 = "ham";
const greeting = `Hello, ${name1}`;
console.log(greating); "Hello, Chris";

const one = "Hello";
const two = "how are you?";
const joined = `${one}, ${two}`;
console.log(joined);

const greetings = "Hello";
const name2 = "ham";
console.log(`${greetings}, ${name2}`);

console.log(greetings + "," + name2)


if (time < 10){
    greeting = "Good morning";
} else if (time < 20){
    greeting = "Good day";
}else {
    greeting = "Good evening";
}

let arg = prompt("Enter a value?");
switch (arg){
    case '0':
    case '1':
        alert('One or zero');
        break;
    case '3':
        alert('Two');
        break;
    case 4:
        alert('Never executes')
        break;
    default:
        alert('An unknown value');

}

// Ternary Operator

condition ? run this code : run this code instead
const greeting = isBirthday 
? "Happy birthday Mrs. smith - we hope you have a great day!"
: "Good morning Mrs. Smith";

let result = condition ? value1 : value2;

let accessAllowed = (age > 18) ? true : false;