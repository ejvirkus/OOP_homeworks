public class Ebook extends Book{
    public Ebook(String name, String author, double price) {
        super(name, author, price);
    }
    @Override
    public double calcDiscount(){
        return this.price * 0.95;
    }

    @Override
    public String toString(){
        return "Ebook \n" + "Title: " + name + "\n" +
                "Author: " + author + "\n" +
                "Price: " + price + "€\n" +
                "Price after discount: " + calcDiscount() + "€\n";
    }
}
