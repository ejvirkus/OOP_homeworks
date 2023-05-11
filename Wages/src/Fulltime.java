public class Fulltime extends Employee {
    private double monthlyHours;

    public Fulltime(String name, double wage, boolean wageMonthly, double taxRate, double monthlyHours){
        super(name, wage, wageMonthly, taxRate);
        this.name = name;
        this.wage = wage;
        this.wageMonthly = wageMonthly;
        this.taxRate = taxRate;
        this.monthlyHours = monthlyHours;
    }

    public double getNetPay(){
        monthlyHours = 170;
        double pay;
        if (this.wageMonthly) {
            pay = this.wage * (1 - this.taxRate);
            return pay;
        }
        else {
            pay = this.wage * this.monthlyHours * (1 - this.taxRate);
            return pay;
        }
    }

    public double getPay(){
        monthlyHours = 170;
        double pay;
        if (this.wageMonthly) {
            return this.wage;
        }
        else {
            pay = this.wage * this.monthlyHours;
            return pay;
        }
    }

    @Override
    public String toString() {
        return ("Fulltime worker: " + this.name + ", pay: " + this.getPay() + ", net pay: " + this.getNetPay());
    }
}
