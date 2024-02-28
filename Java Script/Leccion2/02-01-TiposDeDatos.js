// Tipos de datos en JavaScript
/*
La sintaxis en los comentarios es similar a la de java
*/
var nombre = "Andres";  //tipo Str
console.log(nombre); 

var numero = 3000;  //tipon numerico
console.log(numero);

var objeto ={
    nombre : "Andres",
    apellido : "Luna",
    telefono : "2604123456"
}
console.log(objeto);

//Tipo de dato booleano
var bandera = true;
console.log(typeof bandera);

// Tipo de dato Funcion
function miFuncion(){}
console.log(typeof miFuncion); 

//Tipo de dato Symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre= nombre;
        this.apellido= apellido;
    }
}
console.log(Persona);

//Tipo de dato undefined: se le asigna un dato a una variable no definida
var x;
var xu = undefined;
console.log(typeof x);
console.log(typeof xu);

//null: significa ausencia de valor
var y = null;   //null no es un tipo de dato, pero su origen es objet
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ["Citroen","Audi","BMW","Ford"];
console.log(autos);
console.log(typeof autos);

var z = ""; //esto se refiere a que es una cadena vacia
console.log(z);
console.log(typeof z);