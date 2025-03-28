function Car(brand, model, HP){
    this.brand = brand;
    this.model = model;
    this.Hp = HP
    this.incrementHP = function(){
        this.HP = this.HP + 50
    }
}

const Car1 = new Car1("BMW", "e39", "200");
const Car2 = new Car2("audi", "rs6", "200");
const Car3 = new Car3("toyota", "camry", "150");

car3.incrementHP();
console.log(Car3.HP);