import static java.lang.System.exit;
import java.util.Stack;
import java.util.*;

// Java program to convert an infix expression to a 
// postfix expression using two precedence function 
class Main {

    // to check if the input character
// is an operator or a '(' 
    static int isOperator(char input) {
        switch (input) {
            case '+':
                return 1;
            case '-':
                return 1;
            case '*':
                return 1;
            case '^':
                return 1;
            case '%':
                return 1;
            case '/':
                return 1;
            case '(':
                return 1;
        }
        return 0;
    }

    // to check if the input character is an operand
    static int isOperand(char input) {
        if (input >= 65 && input <= 90
                || input >= 97 && input <= 122) {
            return 1;
        }
        return 0;
    }

    // function to return precedence value
// if operator is present in stack 
    static int inPrec(char input) {
        switch (input) {
            case '+':
            case '-':
                return 2;
            case '*':
            case '%':
            case '/':
                return 4;
            case '^':
                return 5;
            case '(':
                return 0;
        }
        return 0;
    }

    // function to return precedence value
// if operator is present outside stack. 
    static int outPrec(char input) {
        switch (input) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '%':
            case '/':
                return 3;
            case '^':
                return 6;
            case '(':
                return 100;
        }
        return 0;
    }

    // function to convert infix to postfix
    static void inToPost(char[] input) {
        Stack<Character> s = new Stack<Character>();

        // while input is not NULL iterate 
        int i = 0;
        while (input.length!=i) {

            // if character an operand 
            if (isOperand(input[i]) == 1) {
                System.out.printf("%c", input[i]);
            } // if input is an operator, push 
            else if (isOperator(input[i]) == 1) {
                if (s.empty()
                        || outPrec(input[i]) > inPrec(s.peek())) {
                    s.push(input[i]);
                } else {
                    while (!s.empty()
                            && outPrec(input[i]) < inPrec(s.peek())) {
                        System.out.printf("%c", s.peek());
                        s.pop();
                    }
                    s.push(input[i]);
                }
            } // condition for opening bracket 
            else if (input[i] == ')') {
                while (s.peek() != '(') {
                    System.out.printf("%c", s.peek());
                    s.pop();

                    // if opening bracket not present 
                    if (s.empty()) {
                        System.out.printf("Wrong input\n");
                        exit(1);
                    }
                }

                // pop the opening bracket. 
                s.pop();
            }
            i++;
        }

        // pop the remaining operators 
        while (!s.empty()) {
            if (s.peek() == '(') {
                System.out.printf("\n Wrong input\n");
                exit(1);
            }
            System.out.printf("%c", s.peek());
            s.pop();
        }
        System.out.println();
    }

    // Driver code
    static public void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        for(int i = 0;i<a;i++){
            String c = in.next();
            char [] s = c.toCharArray();
            inToPost(s);
        }
//        String c = in.next();
////        System.out.println(c);
//        char [] s = c.toCharArray();
//        char input[] = "a+b*c-(d/e+f^g^h)".toCharArray();
//        inToPost(input);
//        System.out.println("ABC+*D/");
    }
} 