
package adapters;
import round.RoundPeg;
import square.SquarePeg;

public class SquarePegAdapter extends RoundPeg{
    private final SquarePeg peg;
   
    public SquarePegAdapter(SquarePeg peg){
        this.peg = peg;
    }
    @Override
    public double getRadius(){
        double result;
        result = (Math.sqrt(Math.pow((peg.getwidth() / 2), 2) * 2));
        return result;
    } 
}
