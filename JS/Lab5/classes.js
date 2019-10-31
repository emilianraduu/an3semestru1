class Plus {
  value;
  constructor(item1, item2) {
    if (item1 instanceof Minus) {
      this.value = item1.value;
    } else {
      this.value = item1;
    }
    if (item2 instanceof Minus) {
      this.value += item2.value;
    } else {
      this.value += item2;
    }
  }
}

class Minus {
  value;
  constructor(item1, item2) {
    this.value = item1 - item2;
  }
}

class Log {
  static print(a) {
    console.log(a.value);
  }
}

Log.print(new Plus(new Minus(5, 10), 15));
Log.print(new Plus(15, new Minus(5, 10))); 
