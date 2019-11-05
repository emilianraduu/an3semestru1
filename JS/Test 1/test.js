let startNumber = 0;
let values = []
let ActionManager = (function ActionManagerIIFE(number) {
  return {
    do: operation => {
      if (operation instanceof Plus2) {
        return (number = new operation().add2(number));
      }
      if(operation instanceof Minus5){
        return (number = new operation().minus5(number));

      }
    },
    undo: () => {
      try {
        // startNumber = startNumber[startNumber.length - 1];
      } catch (e) {
        console.log(e);
      }
    }
  };
})(startNumber);

class Plus2 {
  constructor() {
    this.value = 2;
  }

}

class Minus5 {
  constructor() {
    this.value = -5;
  }

}

console.log(ActionManager.do(Plus2)); // returns 2
console.log(ActionManager.do(Minus5)); // returns -3

console.log(ActionManager.undo()); // returns 2
console.log(ActionManager.undo()); // returns 0
console.log(ActionManager.undo()); // throw an error: 'Cannot redo anymore'
