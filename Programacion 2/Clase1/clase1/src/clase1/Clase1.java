package clase1;
public class Clase1 {

    public static void main(String[] args) {
        var conteo = 0; //inferencia de tipos
        while(conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo++;   //Vamos aumentando en 1 la variable
        }


System.out.println("-CICLO DO WHILE-");
        //
        //CICLO DO WHILE : MIENTRAS, HACER se ejecuta una vez el codigo dentro del ciclo, si la condicion 
        var contador = 0;
        do{
           System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
        

System.out.println("-CICLO FOR-");

            //CICLO FOR : PARA
        for(var contando = 0; contando < 6; contando ++)  
//ciclo for tiene 3 lugares (variable iterador;condicion;incremento o decremento de iterador )
        System.out.println("Contando= " + contando);

 
System.out.println("-BREAK Y CONTINUOS, junto a ETIQUETAS LEBELS-"); 
 // --- BREAK Y CONTINUOS ---
        //CICLO FOR : PARA
        for(var contando = 0; contando < 7; contando ++){  
//ciclo for tiene 3 lugares (variable iterador;condicion;incremento o decremento de iterador )
            if(contando %2 == 0){
                System.out.println("Contando= "+ contando);
                break;
            }
        }
 
        System.out.println("---");        
        inicio:     //Se usa para ciclos anidados
        for(var contando = 0; contando < 7; contando ++) { 
//ciclo for tiene 3 lugares (variable iterador;condicion;incremento o decremento de iterador )
            if(contando %2 != 0){
                continue;   //Vamos a la siguiente iteracion
            }
            System.out.println("Contando= "+contando);
        }       
    }   
}