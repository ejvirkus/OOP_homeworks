abstract class Book implements Discount{
    String name;
    String author;
    double price;

    public Book(String name, String author, double price){
        this.name = name;
        this.author = author;
        this.price = price;
    }
    @Override
    public double calcDiscount(){
        return this.price;
    }

}
