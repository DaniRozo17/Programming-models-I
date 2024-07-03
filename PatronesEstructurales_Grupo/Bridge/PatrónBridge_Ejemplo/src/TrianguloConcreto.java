public class TrianguloConcreto extends AbstraccionFiguras{
    private ImplementorTamaños implementor;

    public TrianguloConcreto(ImplementorTamaños implementor){
        this.implementor = implementor;
    }

    public void setImplementor(ImplementorTamaños implementor) {
        this.implementor = implementor;
    }

    @Override
    public void dibujarFigura() {
        implementor.dibujarPorTamaño("Triangulo");
    }
}
