public class TextBook extends Book{
    public TextBook(String name, String author, double price) {
        super(name, author, price);
    }

    @Override
    public double calcDiscount(){
        return this.price * 0.8;
    }

    @Override
    public String toString(){
        return "Textbook \n" + "Title: " + name + "\n" +
                "Author: " + author + "\n" +
                "Price: " + price + "€\n" +
                "Price after discount: " + calcDiscount() + "€\n";
    }
}
