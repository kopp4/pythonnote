package oddsnends;

/**
 * @Author: taltalasuka
 * @Date: 2021/10/17 21:56
 */
public class AngleBracket {
    public static void main(String[] args) {

        Test<Integer> test = new Test<Integer>(18);
        System.out.println(test.getTest());
    }
}

class Test<T>{
    T test;

    public T getTest() {
        return test;
    }

    public void setTest(T test) {
        this.test = test;
    }

    public Test(T test) {
        this.test = test;
    }
}
