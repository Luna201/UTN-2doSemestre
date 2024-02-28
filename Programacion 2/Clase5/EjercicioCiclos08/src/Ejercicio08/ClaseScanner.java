/*
Ejercicio 8: pedir un nro N, y mostrar todos los números de 1 a N
 */
package Ejercicio08;
import java.util.Scanner;
public class ClaseScanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        int numero= Integer.parseInt(entrada.nextLine());
        int i = 1;
        while(i <= numero){
            System.out.println(i);
            i++;
        }
    }
}
