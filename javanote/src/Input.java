/**
 * @Author: taltalasuka
 * @Date: 2021/12/15 18:51
 */

import java.util.Scanner;


public class Input {

    private int SUM;
    private int MAX;
    private String NAME;
    private String SNo;

    public static void main(String[] args) {

    }


    public void getInformation(int M, int E,int J){

        this.SUM = M + E + J;
        this.MAX = Math.max(M, Math.max(E, J));     // get

    }

    public void announcement(){
        System.out.println("(Ordered by Math, English, Java): ");
        System.out.println("Plz input scores of 3 courses : ");

        inPut();    // calling input




    }

    public void outPut(){
        System.out.printf("");

    }


    /* Literally input */
    public void inPut(){



        Scanner sc = new Scanner(System.in);

        int math = sc.nextInt();
        int english = sc.nextInt();
        int java = sc.nextInt();

        sc.close();

        getInformation(math, english, java);

    }
}

//todo comment