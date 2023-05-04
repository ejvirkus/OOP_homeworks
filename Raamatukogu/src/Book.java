public class Book {
    private String name;
    private String author;
    private int publishDate;

    public Book(String name, String author, int publishDate) {
        this.name = name;
        this.author = author;
        this.publishDate = publishDate;
    }
    public String getName(){
        return this.name;
    }
    public String getAuthor(){
        return this.name;
    }
    public int getPublishDate(){
        return this.publishDate;
    }
}
