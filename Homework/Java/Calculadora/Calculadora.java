import java.util.Scanner;
// Importar la clase Scanner para leer la entrada del usuario

// La clase Calculator contiene el método main
public class Calculator {
    // El método main es el punto de entrada del programa
    public static void main(String[] args) {
        // Crear un objeto Scanner para leer la entrada del usuario
        Scanner scanner = new Scanner(System.in);
       // Leer la entrada del usuario
        System.out.println("Ingresa una operación matemática (ej. 2 + 2):");
        // Guardar la entrada del usuario en una variable
        String input = scanner.nextLine();

        // Utilizar una expresión regular para dividir la entrada en números y operadores
        String[] tokens = input.split("(?<=[^\\d])|(?=[^\\d])");

        // Inicializar variables para almacenar el resultado y el operando anterior
        double result = 0;
        String previousOperator = "";

        // Iterar a través de los tokens y realizar las operaciones correspondientes
        for (String token : tokens) {
            if (token.equals("+")) {
                previousOperator = "+";
            } else if (token.equals("-")) {
                previousOperator = "-";
            } else if (token.equals("*")) {
                previousOperator = "*";
            } else if (token.equals("/")) {
                previousOperator = "/";
            } else {
                // Convertir el token a un número y realizar la operación correspondiente
                double number = Double.parseDouble(token);
                if (previousOperator.equals("+")) {
                    result += number;
                } else if (previousOperator.equals("-")) {
                    result -= number;
                } else if (previousOperator.equals("*")) {
                    result *= number;
                } else if (previousOperator.equals("/")) {
                    result /= number;
                } else {
                    result = number;
                }
            }
        }
         // Imprimir el resultado
        System.out.println("Resultado: " + result);
    }
}
