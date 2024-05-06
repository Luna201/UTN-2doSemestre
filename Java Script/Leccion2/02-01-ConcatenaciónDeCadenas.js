var nombre= "Jose";
var apellido= "Montes";
var nombreCompleto= nombre +" "+apellido; //Primera concatenación
console.log(nombreCompleto);

var nombreCompleto2= "Ariel"+" "+"Betancud";    //Segunda concatenación
console.log(nombreCompleto2);

var juntos = nombre+ 219;   //Lee de izq a der siguiendo la cadena, lee el nro como str
console.log(juntos);
juntos = nombre + 78 +17;
console.log(juntos);

juntos = 78 + 17 + nombre;  //contexto str: si los nros estan primero los suma
console.log(juntos);

nombre+= apellido;  //Tercera concatenación 
console.log(nombre);

// Ya no se usar var, usaremos let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2= "Lopez";
//apellido2= "Perez"; una constante no puede ser modificada
console.log(apellido2);

let x, y;	//Se puede crear varia variables dentro de una linea
x= 17, y=21; //Se puede hacer asiganciones a varias variables dentro de una linea

let z = x + y; // se asigna el valor de la operación
console.log(z);

let _1num = 21; // No se puede iniciar una variable con un nro
let rompiendo = "rompe"; //No utilizar palabras reservadas para variables

console.log(_1num)
console.log(rompiendo)