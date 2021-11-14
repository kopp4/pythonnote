package javaadvanced.processandthread;

/**
 * @Author: taltalasuka
 * @Date: 2021/11/10 16:57
 */
public class MyThreadDemo {
    public static void main(String[] args) {
        MyThread my1 = new MyThread("black");
        MyThread my2 = new MyThread("white");

//        my1.run();  // fake
//        my2.run();  // fake

        // void start()  contribute in starting to execute the thread
        my1.start();
        my2.start();
    }
}


