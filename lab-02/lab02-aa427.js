// const inputtable  = [1,2,3,4,5,6,7,8,9,10]
// console.log()

console.log('------------------------------- Q1')
const n1 = 10
const inputtable = [...Array(n1).keys()].map(x => x+1)
console.log(inputtable)

console.log('------------------------------- Q2')
const fiveTable = inputtable.map(x => x*5)
console.log(fiveTable)

const thirteenTable = inputtable.map(x => x*13)
console.log(thirteenTable)

const squaresTable = inputtable.map(x => x*x)
console.log(squaresTable)

console.log('------------------------------- Q3')
const n100 = 100
const multiplesOfFive = [...Array(n100).keys()].map(x => x+1).filter(x => x%5 === 0)
// console.log(multiplesOfFive)

// chekcing if remainder is 1 for odd
const oddFiveMultiples = multiplesOfFive.filter(x => x%2 === 1)
console.log(oddFiveMultiples)

console.log('------------------------------- Q4')
const multiplesOfSeven = [...Array(n100).keys()].map(x => x+1).filter(x => x%7 === 0)
// console.log(multiplesOfSeven)

const evenSevenMultiples = multiplesOfSeven.filter(x => x%2 === 0)
console.log(evenSevenMultiples)

const evenSevenMultiplesSum = evenSevenMultiples.reduce((acc, x) => acc+x)
console.log(`evenSevenMultiplesSum = ${evenSevenMultiplesSum}`)

console.log('------------------------------- Q5')

const cylinder_volume = r => h => 3.14*r*r*h

const cylinderRadius5 = cylinder_volume(5)

const volumeWithHeight10 = cylinderRadius5(10)
console.log(`volumeWithHeight10 = ${volumeWithHeight10}`)

const volumeWithHeight17 = cylinderRadius5(17)
console.log(`volumeWithHeight17 = ${volumeWithHeight17}`)

const volumeWithHeight11 = cylinderRadius5(11)
console.log(`volumeWithHeight11 = ${volumeWithHeight11}`)


const makeTag = (beginTag, endTag) =>{
    return (textContent) => '\n' + beginTag + textContent + endTag
}
    
console.log('------------------------------- Q6')

const tableTag = makeTag('<table>', '</table>')
const trTag = makeTag('<tr>','</tr>')
const thTag = makeTag('<th>','</th>')

const rowData1 = trTag(thTag('Jon') + thTag('Snow') + thTag('22') + '\n')
const rowData2 = trTag(thTag('Arya') + thTag('Stark') + thTag('14') + '\n')
const rowData3 = trTag(thTag('Bran') + thTag('Stark') + thTag('12') + '\n')

const output = tableTag(rowData1+'\n'+rowData2+'\n'+rowData3+'\n')
console.log(output)

console.log('------------------------------- Q8')

const general = multipleOf => {
    const n100 = 100
    const arr100 = [...Array(n100).keys()].map(x => x+1)
    const multiples = arr100.filter(x => x%multipleOf === 0)
    
    return (type) => {
        if (type === 'even'){
            return multiples.filter(x => x%2 === 0)
        }
        else if (type === 'odd'){
            return multiples.filter(x => x%2 === 1)
        }
        else {
            throw Error('The expected types are even and odd. Unexpected input.')
        }
    }
}

// const general = multipleOf => {
//     const n100 = 100
//     const arr100 = [...Array(n100).keys()].map(x => x+1)
//     const multiples = arr100.filter(x => x%multipleOf === 0)

//     return (type) => type === 'even' ? multiples.filter(x => x%2 === 0) : multiples.filter(x => x%2 === 1)
// }

const multiplesOf5 = general(5)
const oddMultiplesOf5 = multiplesOf5('odd')
console.log(oddMultiplesOf5)

const multiplesOf7 = general(7)
const evenMultiplesOf7 = multiplesOf7('even')
console.log(evenMultiplesOf7)
