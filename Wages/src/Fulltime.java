public class Fulltime extends Employee {
    private double monthlyHours;
    private double pay;

    public Fulltime(String name, double wage, boolean wageMonthly, float taxRate, double monthlyHours, double pay){
        super(name, wage, wageMonthly, taxRate);
        this.name = name;
        this.wage = wage;
        this.wageMonthly = wageMonthly;
        this.taxRate = taxRate;
        this.monthlyHours = monthlyHours;
        this.pay = pay;
    }

    public void setMonthlyHours(double monthlyHours) {
        this.monthlyHours = monthlyHours;
    }

    public double getMonthlyHours() {
        return monthlyHours;
    }

    public double getPay(double monthlyHours, double wage, float taxRate){
        monthlyHours = 170;
        this.pay = this.wage*(1-this.taxRate);
        return this.pay;
    }
}
