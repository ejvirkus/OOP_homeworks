public class Halftime extends Employee{

    private double monthlyHours;
    private double pay;

    public Halftime(String name, double wage, boolean wageMonthly, float taxRate, double monthlyHours, double pay){
        super(name, wage, wageMonthly, taxRate);
        this.name = name;
        this.wage = wage;
        this.wageMonthly = wageMonthly;
        this.taxRate = taxRate;
        this.monthlyHours = monthlyHours;
        this.pay = pay;
    }



}
