const container = document.querySelector('#container');
const display = container.firstElementChild;
// const controls = container.secondElementChild;

const content = document.createElement('div');
content.classList.add('content');
content.textContent = 'Hamcodes is avaliable for production';

container.appendChild(content);



const div = document.createElement('div');

div.style.color = 'blue';
div.style.cssText = 'color: blue; background: white;';
div.setAttribute('style', 'color: blue; background: white;');
// div.backgroundColor = 'grey';
div.textContent = 'Hello world';
div.innerHTML = '<span>Hello world</span>';