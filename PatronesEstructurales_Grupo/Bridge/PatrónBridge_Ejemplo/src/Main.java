public class Main {
    public static void main(String[] args) {
        ImplementorTamaños implementorGrande = new ImplementorGrande();
        AbstraccionFiguras cuadrado = new CuadradoConcreto(implementorGrande);
        AbstraccionFiguras triangulo = new TrianguloConcreto(implementorGrande);
        cuadrado.dibujarFigura();
        triangulo.dibujarFigura();

        ImplementorTamaños implementorPequeño = new ImplementorPequeño();
        cuadrado.setImplementor(implementorPequeño);
        cuadrado.dibujarFigura();
        triangulo.setImplementor(implementorPequeño);
        triangulo.dibujarFigura();;



    }
}
