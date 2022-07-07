// const inputtable  = [1,2,3,4,5,6,7,8,9,10]
// console.log()

console.log('----------------- Q1')
const n1 = 10
const inputtable = [...Array(n1).keys()].map(x => x+1)
console.log(inputtable)

console.log('----------------- Q2')
const fiveTable = inputtable.map(x => x*5)
console.log(fiveTable)

const thirteenTable = inputtable.map(x => x*13)
console.log(thirteenTable)

const squaresTable = inputtable.map(x => x*x)
console.log(squaresTable)

console.log('----------------- Q3')
const n2 = 20
const multiplesOfFive = [...Array(n2).keys()].map(x => x+1).map(x => x*5)
// console.log(multiplesOfFive)

// chekcing if remainder is 1 for odd
const oddFiveMultiples = multiplesOfFive.filter(x => x%2 === 1)
console.log(oddFiveMultiples)

console.log('----------------- Q4')
const n3 = 14
const multiplesOfSeven = [...Array(n3).keys()].map(x => x+1).map(x => x*7)
console.log(multiplesOfSeven)

const evenSevenMultiples = multiplesOfSeven.filter(x => x%2 === 0)
console.log(evenSevenMultiples)

const evenSevenMultiplesSum = evenSevenMultiples.reduce((acc, x) => acc+x)
console.log(`evenSevenMultiplesSum = ${evenSevenMultiplesSum}`)

console.log('----------------- Q5')
