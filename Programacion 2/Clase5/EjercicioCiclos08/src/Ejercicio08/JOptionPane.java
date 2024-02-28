/*
Ejercicio 8: pedir un nro N, y mostrar todos los números de 1 a N
 */
package Ejercicio08;

import javax.swing.JOptionPane;

public class JOptionPane {
    public static void main(String[] args) {
        int numero= Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        int i = 1;
        while(i <= numero){
            JOptionPane.showMessageDialog(null, i);
            i++;
        }
    }
}