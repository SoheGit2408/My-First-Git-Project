
import java.util.Scanner;
class diff {
public static void main(String[] args){
Scanner num=new Scanner(System.in);
System.out.println("Enter first number: ");
int a=num.nextInt();

System.out.println("Enter second number: ");
int b=num.nextInt();
System.out.println("Difference of two numbers is : "+(a-b));
num.close();
}
}
