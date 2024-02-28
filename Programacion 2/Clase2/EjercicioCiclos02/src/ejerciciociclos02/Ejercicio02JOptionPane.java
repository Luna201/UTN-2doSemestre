/*
Ejercicio2: leer un número e indicar si es positivo o negativo. El proceso se
repetira hasta introducir un cero 0. Con JOptionPane
*/
package ejerciciociclos02;
import javax.swing.JOptionPane;
public class Ejercicio02JOptionPane {
    public static void main(String[]args){
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero != 0){
            if (numero > 0){
                JOptionPane.showConfirmDialog(null, "El número "+numero+" es POSITIVO");
            }
            else{
               JOptionPane.showConfirmDialog(null, "El número "+numero+" es NEGATIVO");
            }
            System.out.println("Digite otro número");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        }
        JOptionPane.showConfirmDialog(null, "El número "+numero+" finaliza el programa");
    }
}

