package Clases;
public class PruebaPersona {    //pascar case, empieza con mayscula cada palabra
    public static void main(String[] args) {    //ejecuta el programa
        Persona persona1;   //
        persona1 = new Persona ();  //llamamos al constructor
        //Persona persona1 = new Persona (); // reemplaza a la linea 4 y 5 por solo una
        persona1.nombre ="Andrés";  //el valor hexadecimal normalmente comina con 0x
        persona1.apellido = "Luna";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = "+ persona2);
        System.out.println("persona1 = "+ persona1);
        persona2.obtenerInformacion ();
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion ();
    }
}
