public class Halftime extends Employee{

    private double monthlyHours;
    public Halftime(String name, double wage, boolean wageMonthly, double taxRate, double monthlyHours){
        super(name, wage, wageMonthly, taxRate);
        this.monthlyHours = monthlyHours;
    }

    public void setMonthlyHours(double monthlyHours) {
        this.monthlyHours = monthlyHours;
    }

    public double getMonthlyHours() {
        return monthlyHours;
    }

    public double getNetPay() {
        double pay;
        if (wageMonthly) {
            pay = this.wage * (1-this.taxRate);
            return pay;
        }
        else {
            pay = this.wage * this.monthlyHours * (1-this.taxRate);
            return pay;
        }
    }

    public double getPay() {
        double pay;
        monthlyHours = 70;
        if (wageMonthly) {
            return this.wage;
        }
        else {
            pay = this.wage * this.monthlyHours;
            return pay;
        }
    }

    @Override
    public String toString() {
        return ("Halftime worker: " + this.name + ", pay: " + this.getPay() + ", net pay: " + this.getNetPay() + ".");
    }
}
