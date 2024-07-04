import java.util.*;
// Interfaz para todas las expresiones interpretativas 
interface Expression {
    void interpret (Robot robot);
}

// Expresión terminal que mueve al robot hacia adelante 
class ExpresionTerminal_Adelante implements Expression { 
    private int pasos;

    public ExpresionTerminal_Adelante(int pasos) {
        this.pasos = pasos;
    }

    public void interpret (Robot robot) {
        robot.moverAdelante (pasos);
    }
}

// Expresión terminal que gira al robot hacia la izquierda 
class ExpresionTerminal_Izquierda implements Expression { 
    public void interpret (Robot robot) {
        robot.girarIzquierda ();
    }
}

// Expresión terminal que gira al robot hacia la derecha 
class ExpresionTerminal_Derecha implements Expression { 
    public void interpret (Robot robot) {
        robot.girarDerecha();
    }
}

// Clase Parser que construye el árbol de expresiones a partir de una cadena 
class Parser {
    private List<Expression> parseTree = new ArrayList<>();

    public Parser(String s) {
    for (String token : s.split(" ")) {
        
        if (token.equals("adelante")) {
            parseTree.add(new ExpresionTerminal_Adelante (1)); // Por defecto, mueve 1 paso
        } else if (token.equals("izquierda")) {
            parseTree.add(new ExpresionTerminal_Izquierda());
        } else if (token.equals("derecha")) {
            parseTree.add(new ExpresionTerminal_Derecha());
        } else if (token.startsWith("adelante")) {
            int pasos = Integer.parseInt(token.substring(8)); // 'adelantex' donde X son los pasos
            parseTree.add(new ExpresionTerminal_Adelante (pasos));
        } 
    }
}
public void ejecutar (Robot robot) { 
    for (Expression e: parseTree) {
        e. interpret (robot);
        }
    }
}

// Clase Robot que simula las acciones del robot virtual 
class Robot {
        private int x, y;
        private String direccion;

        public Robot(int x, int y, String direccion) {
            this.x = x;
            this.y = y;
            this.direccion = direccion;
        }

        public void moverAdelante (int pasos) { 
            if (direccion.equals("norte")) {
                y += pasos;
            } else if (direccion.equals("sur")) { 
                y -= pasos;
            } else if (direccion.equals("este")) { 
                x += pasos;
            }else if (direccion.equals("oeste")) {
                x -= pasos;
            }
        }

        public void girarIzquierda() {
            if (direccion.equals("norte")) {
                direccion = "oeste";
            } else if (direccion.equals("sun")) { 
                direccion = "este";
            } else if (direccion.equals("este")) { 
                direccion = "norte";
            } else if (direccion.equals("oeste")) { 
                direccion = "sur";
            }
        }
        public void girarDerecha() {
            if (direccion.equals("norte")) {
                direccion = "este";
            } else if (direccion.equals("sur")) { 
                direccion = "oeste";
            } else if (direccion.equals("este")) { 
                direccion = "sur";
            } else if (direccion.equals("oeste")) { 
                direccion = "norte";
            }
        }

        public String obtenerPosicion() {
            return "(" + x + ", " + y + ") direccion " + direccion;
        }
    }

// Clase de ejemplo para probar el intérprete de comandos para el robot 
public class EjemploInterprete {
    public static void main(String[] args) {
        Robot robot = new Robot (0, 0, "norte");
        Parser parser = new Parser("adelante 3 derecha adelante 2 izquierda adelante 1");
        parser.ejecutar (robot);
        System.out.println("Posición final del robot: " + robot.obtenerPosicion());
    }
}