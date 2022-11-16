import java.util.Scanner;

public class r {
    public Main() {
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Какой тип данных?");
        String step = in.nextLine();
        if (step.equals("целочисленные")) {
            System.out.println("Введите первое число");
            int x = in.nextInt();
            System.out.println("Введите второе число");
            int y = in.nextInt();
            System.out.println("сложение " + (x + y));
            System.out.println("Вычитание " + (x - y));
            System.out.println("умножени " + x * y);
            System.out.println("деление " + x / y);
            System.out.println("деление по модулю " + x % y);
        } else if (step.equals("вещественные")) {
            System.out.println("Введите первое число");
            float x = in.nextFloat();
            System.out.println("Введите второе число");
            float y = in.nextFloat();
            System.out.println("сложение " + (x + y));
            System.out.println("Вычитание " + (x - y));
            System.out.println("умножени " + x * y);
            System.out.println("деление " + x / y);
            System.out.println("деление по модулю " + x % y);
        } else if (step.equals("байтовые")) {
            System.out.println("Введите первое число");
            byte x = in.nextByte();
            System.out.println("Введите второе число");
            byte y = in.nextByte();
            System.out.println("сложение " + (byte)(x + y));
            System.out.println("Вычитание " + (byte)(x - y));
            System.out.println("умножени " + (byte)(x * y));
            System.out.println("деление " + (byte)(x / y));
            System.out.println("деление по модулю " + (byte)(x % y));
        }

    }
}
