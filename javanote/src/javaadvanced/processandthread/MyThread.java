package javaadvanced.processandthread;

/**
 * @Author: taltalasuka
 * @Date: 2021/11/10 17:01
 */
public class MyThread extends Thread{
//    public void setName(){}
//
//    public void setName(String Name){
//        super.setName();
//    }



    public MyThread(String name){
        super(name);
    }

    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.println(getName() + ":" + i);
        }
    }
}
