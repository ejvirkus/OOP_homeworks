public class Employee {

    public String name;
    public double wage;
    public boolean wageMonthly;
    public double taxRate;
    public Employee(String name, double wage, boolean wageMonthly, double taxRate) {
        this.name = name;
        this.wage = wage;
        this.wageMonthly = wageMonthly;
        this.taxRate = taxRate;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setWage(double wage) {
        this.wage = wage;
    }

    public void setWageMonthly(boolean wageMonthly) {
        this.wageMonthly = wageMonthly;
    }

    public void setTaxRate(float taxRate) {
        this.taxRate = taxRate;
    }

    public String getName() {
        return name;
    }

    public double getWage() {
        return this.wage;
    }

    public boolean isWageMonthly() {
        return wageMonthly;
    }

    public double getTaxRate() {
        return taxRate;
    }
}
