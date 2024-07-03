
public class CineFacade {
    private SistemaReservas reservas;
    private SistemaPagos pagos;
    private SistemaNotificaciones notificaciones;
    
    public CineFacade(){
        this.reservas = new SistemaReservas();
        this.pagos = new SistemaPagos();
        this.notificaciones = new SistemaNotificaciones();
    }
    
    public void comprarEntrada(String pelicula, int asiento, String tarjeta, double monto){
        reservas.reservarAsiento(pelicula, asiento);
        pagos.procesarPago(tarjeta, monto);
        notificaciones.enviarNotificacion("Entrada comprada para " + pelicula + ", asiento " + asiento);
    }
}
