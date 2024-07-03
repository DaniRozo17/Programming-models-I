public class CuadradoConcreto extends AbstraccionFiguras{
    private ImplementorTamaños implementor;

    public CuadradoConcreto(ImplementorTamaños implementor){
        this.implementor = implementor;
    }

    public void setImplementor(ImplementorTamaños implementor) {
        this.implementor = implementor;
    }

    @Override
    public void dibujarFigura() {
        implementor.dibujarPorTamaño("cuadrado");
    }
}
