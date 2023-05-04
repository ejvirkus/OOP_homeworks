public class Main {
    public static void main(String[] args){

        Library library1 = new Library();
        Library library2 = new Library();

        Book book1 = new Book("Kaks kantsi", "J.R.R. Tolkien", 1954);
        Book book2 = new Book("Sõrmuse vennaskond", "J.R.R. Tolkien", 1954);
        Book book3 = new Book("Kuninga tagasitulek", "J.R.R. Tolkien", 1955);
        Book book4 = new Book("Eragon", "Christopher Paolini", 2003);
        Book book5 = new Book("Eldest", "Christopher Paolini", 2005);

        library1.Add(book1);
        library1.Add(book2);
        library1.Add(book3);

        library2.Add(book4);
        library2.Add(book5);

        library2.BookSearch("Eragon");

    }

}