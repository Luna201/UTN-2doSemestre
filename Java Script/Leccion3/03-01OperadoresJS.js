// Ejercicio 1: para encontrar números pares impares

let parImpar= 10;
if(parImpar % 2 ==0){
    console.log("Es un número PAR")
}
else{
    console.log("Es un número IMPAR")
}

//Ejercicio: es mayor de edad

let edad = 14, adulto = 18
if(edad >= adulto){
    console.log("Usted es una persona adulta");
}
else{console.log("Usted es una persona menor de edad");
}

// Ejercicio: Dentro de rango
let dentroRango = -1; // Aqui vamos a ir cambiando  el valor
let valMin = 0, valMax = 10;
if( dentroRango >=valMin &&dentroRango <=valMax){
    console.log("Esta dentro del rango establecido")
}
else{
    console.log("Esta fuera del rango establecido")
}

// Ejercicio 03: Si el padre puedde asistir al juego del hijo
let vacaciones = false, diaDescanso = false
if (vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego del hijo")
}
else{
    console.log("El padre No puede asistir al juego del hijo")
}

// OPERADOR TERNARIO
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)

let numero = 9;
resultado2 = numero % 2 == 0 ? "Es un número PAR" : "Es un número IMPAR";
console.log(resultado2)

//CONVERTIR STRING A NUMBER
/*
let miNumero = "21";    //Es una cadena
console.log(typeof miNumero)
let edad2 = Number(miNumero);   // Esta es una función
console.log(typeof edad2);
if(edad2 >= 16){
    console.log("Puede votar")
}
else{
    console.log("Muy joven para votar")
}
*/
//FUNCIÓN isNaN= no es un múmero (is Not a Number (devuelve un resultado booleano))
let miNumero = "19";    //Es una cadena
console.log(typeof miNumero)
let edad2 = Number(miNumero);   // Esta es una función
console.log(typeof edad2);
if(isNaN(edad2)){
    console.log("Esta variable no contiene sólo números")
}
else{
    if(edad2 >= 18){
        console.log("Puede votar")
    }
    else{
        console.log("Muy joven para votar")
    }
}


//Resumen del codigo de arriba en una linea
let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar"
console.log(resultado3)

