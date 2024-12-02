function random(number){
    return Math.floor(Math.random() * number)
}

function draw(){
    ctx.clearReact(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < 100; i++){
        ctx.beginPath();
        ctx.fillStyle = "rgb(255 0 0 / 50%)";
        ctx.arc(
            random(canvas.width),
            random(canvas.heigh),
            random(50),
            0,
            2 * Math.PI,
        );
        ctx.fill();
    }
}

const cats = ["leopard", "Serval", "Jaguar", "Tiger", "Caracal", "Lion"];
for (const cat of cats){
    console.log(cat);

for (let i = 0; i < cats.length; i++){
    console.log(cats[i]);
}

}
function toUpper(string){
    return string.toUpperCase();
} 
const upperCats = cats.map(toUpper);
console.log(upperCats);

function lCat(cat){
    return cat.startsWith("L");
}

const filtered = cats.filter(lCat);
console.log(filtered);

// for (initializer; condition; final-expression) { // code to run}

for (let i = 1; i < 10; 1++){
    const cats = `${i} X ${i} = ${i * i}\n`
    
}

for () {
    if (){}
    break;
    continue;
    
}

let i = 0;

while (i < cats.length){
    if (i === cats.length -1){
        cats += `and ${cats[i]}.`;
    }   else{
        cats += `${cats[i]},`;
    }

    i++;

}

do {
    // code to run

    final-expression
}while (condition)




    let i = 3

    while(i < 3){
        alert(i--);
    }
    
    let x = 0;
    while (++x < 5) alert(x);
    
    while (x++ < 5) alert(x); 