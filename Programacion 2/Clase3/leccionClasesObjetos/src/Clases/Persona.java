package Clases;
public class Persona {
    //declarar atributos: caracteristicas de la clase
    String nombre; 
    String apellido;
    
    // metodo de las clase(acciones)    //se puede reutilizar
    public void obtenerInformacion(){
        System.out.println("Nombre; "+nombre);  //es un atributo, no variable
        System.out.println("Apellido: "+apellido);
    }
}
