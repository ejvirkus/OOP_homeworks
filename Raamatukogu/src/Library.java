import java.util.ArrayList;
import java.util.List;

public class Library {
    List<Book> ListOfBooks = new ArrayList<>();
    List<String> BooksAsString = new ArrayList<>();
    public String Convert(Book book){
        return("Name: " + book.getName() + "Author: " + book.getAuthor() +
                "Publish Date: " + book.getPublishDate() + "\n");
    }
    public void Add(Book book){
        ListOfBooks.add(book);
        BooksAsString.add(Convert(book));
        System.out.println(book + " added!");
    }
    public void Remove(Book book){
        ListOfBooks.remove(book);
        BooksAsString.remove(Convert(book));
        System.out.println(book + " removed!");
    }
    public String getBooksAsString(){
        return BooksAsString.toString();
    }
    public Boolean BookSearch(String name){
        for (Book book : ListOfBooks) {
            if (book.getName().equals(name)){
                System.out.println(book + " in stock!");
            }
        }
        return false;
    }
 }
