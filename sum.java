import java.util.Scanner;
class sum {
/**
 * @param args
 */
public static void main(String[] args){
Scanner num=new Scanner(System.in);
System.out.println("Enter first number: ");
int x=num.nextInt();

System.out.println("Enter second number: ");
int y=num.nextInt();
System.out.println("sum of two numbers is : "+(x+y));
num.close();
}
}
