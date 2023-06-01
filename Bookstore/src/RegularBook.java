public class RegularBook extends Book{

    public RegularBook(String name, String author, double price) {
        super(name, author, price);
    }

    @Override
    public double calcDiscount(){
        return this.price * 0.9;
    }

    @Override
    public String toString(){
        return "Regular book \n" + "Title: " + name + "\n" +
                "Author: " + author + "\n" +
                "Price: " + price + "€\n" +
                "Price after discount: " + calcDiscount() + "€\n";
    }


}
