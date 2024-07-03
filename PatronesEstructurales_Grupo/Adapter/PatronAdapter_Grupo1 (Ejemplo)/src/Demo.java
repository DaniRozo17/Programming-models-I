/*
Modelos de programación I - Marcela Espinosa 
Patrón Adapter
*/

import adapters.SquarePegAdapter;
import round.RoundHole;
import round.RoundPeg;
import square.SquarePeg;

public class Demo {
    public static void main(String[] args){
        RoundHole hole = new RoundHole(5);
        RoundPeg rpeg = new RoundPeg(5);
        if(hole.fits(rpeg)){
            System.out.println("La clavija redonda r5 encaja en el agujero redondo r5.");
        }
        
        SquarePeg smallSqPeg = new SquarePeg(2);
        SquarePeg largeSqPeg = new SquarePeg(20);
        
        SquarePegAdapter smallSqPegAdapter = new SquarePegAdapter(smallSqPeg);
        SquarePegAdapter largeSqPegAdapter = new SquarePegAdapter(largeSqPeg);
        if(hole.fits(smallSqPegAdapter)){
            System.out.println("La clavija cuadrada w2 encaja en el orificio redondo r5.");
        }
        if(!hole.fits(largeSqPegAdapter)){
            System.out.println("La clavija cuadrada w20 no encaja en el orificio redondo r5.");
        }
    }
}
