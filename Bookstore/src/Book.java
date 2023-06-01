abstract class Book implements Discount{
    String name;
    String author;
    double price;

    public Book(String name, String author, double price){
        this.name = name;
        this.author = author;
        this.price = price;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}
