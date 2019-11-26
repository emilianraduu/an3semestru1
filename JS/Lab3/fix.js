const add = (a, b) => a + b;
const addG = a => b => () => add(a, b);
console.log(addG(10)(15)(20)()); // 15
