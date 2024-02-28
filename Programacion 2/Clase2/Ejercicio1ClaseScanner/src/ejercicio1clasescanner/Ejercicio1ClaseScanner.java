/*
Ejercicio 1: Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un número negativo
*/
package ejercicio1clasescanner;
import java.util.Scanner;
public class Ejercicio1ClaseScanner {

    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        int numero, cuadrado;
        numero = Integer.parseInt(entrada.nextLine());
        while(numero>= 0){
            cuadrado = (int)Math.pow(numero,2);
            System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("** El programa a finalizado por número negativo **");
    }
    
}
