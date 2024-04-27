package Operaciones;
public class Aritmetica {
    // atributos de la clase
    int a;
    int b;
    
    //Método
    public void sumarNumeros(){ //void no retorna
        int resultado = a+ b;
        System.out.println("resultado= "+ resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return a + b;
        
    }    
    public int sumarConArgumentos(int arg1, int arg2){
        a = arg1;
        b = arg2;
        //return a + b;
        return sumarConRetorno();   //se puede llamar a oro método solo si comparte la misma clase
    }
    //El constructor es un Metodo especial. Sobrecarga de constructor = 1 o mas constructores, agregando  u omitiendo valores
    //public Aritmetica(){    //constructor 1, vacio, por defecto
    //    System.out.println("Se esta ejecutando este constructor número uno");
    //}
}