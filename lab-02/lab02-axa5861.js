/**
 * Name: Amlan Alok
 * Student ID: 1001855861
 * Due Date: 11th July, 2022
 * 
 * Used below command to run the file
 * node lab02-axa5861.js 
 */

console.log('------------------------------- Q1')
const n1 = 10
// creating array of size 10 using spread operator and Array().keys()
// map is used to increment each element by 1
const inputtable = [...Array(n1).keys()].map(x => x+1)
console.log(inputtable)



console.log('------------------------------- Q2')
// map is used to multiply each element in inputable by 5
const fiveTable = inputtable.map(x => x*5)
console.log(fiveTable)

// map is used to multiply each element in inputable by 13
const thirteenTable = inputtable.map(x => x*13)
console.log(thirteenTable)

// map is used to multiply each element in inputable by the elemtn itself
const squaresTable = inputtable.map(x => x*x)
console.log(squaresTable)



console.log('------------------------------- Q3')
const n100 = 100
// creating array of size 100 using spread operator and Array().keys()
// map is used to increment each element by 1
// filter is used to keep only the mulltiples of 5
const multiplesOfFive = [...Array(n100).keys()].map(x => x+1).filter(x => x%5 === 0)
// console.log(multiplesOfFive)

// checking if remainder is 1 for odd 
const oddFiveMultiples = multiplesOfFive.filter(x => x%2 === 1)
console.log(oddFiveMultiples)



console.log('------------------------------- Q4')
// creating array of size 100 using spread operator and Array().keys()
// map is used to increment each element by 1
// filter is used to keep only the mulltiples of 7
const multiplesOfSeven = [...Array(n100).keys()].map(x => x+1).filter(x => x%7 === 0)
// console.log(multiplesOfSeven)

// checking if remainder is 0 for even
const evenSevenMultiples = multiplesOfSeven.filter(x => x%2 === 0)
console.log(evenSevenMultiples)

// using reduce to add all elements in evenSevenMultiples array
const evenSevenMultiplesSum = evenSevenMultiples.reduce((acc, x) => acc+x)
console.log(`\nSum of even multiples of 7 between 1 and 100 = ${evenSevenMultiplesSum}`)



console.log('------------------------------- Q5')

// defined a currying function
const cylinder_volume = r => h => 3.14*r*r*h

// only passing r = 5 in the currying function as first argument
const cylinderRadius5 = cylinder_volume(5)

// passing value of h as the second argument in the currying function
const volumeWithHeight10 = cylinderRadius5(10)
console.log(`volumeWithHeight10 = ${volumeWithHeight10}`)

// passing value of h as the second argument in the currying function
const volumeWithHeight17 = cylinderRadius5(17)
console.log(`volumeWithHeight17 = ${volumeWithHeight17}`)

// passing value of h as the second argument in the currying function
const volumeWithHeight11 = cylinderRadius5(11)
console.log(`volumeWithHeight11 = ${volumeWithHeight11}`)



console.log('------------------------------- Q6')

// took from lab pdf
const makeTag = (beginTag, endTag) => {
    return (textContent) => '\n' + beginTag + textContent + endTag
}

// creating all the required tags
const tableTag = makeTag('<table>', '</table>')
const trTag = makeTag('<tr>','</tr>')
const thTag = makeTag('<th>','</th>')
const rowHeading = trTag(thTag('First Name') + thTag('Last Name') + thTag('Age') + '\n')
const rowData1 = trTag(thTag('Jon') + thTag('Snow') + thTag('22') + '\n')
const rowData2 = trTag(thTag('Arya') + thTag('Stark') + thTag('14') + '\n')
const rowData3 = trTag(thTag('Bran') + thTag('Stark') + thTag('12') + '\n')

// combining all the created tags in the correct order
const output = tableTag(rowHeading+'\n'+rowData1+'\n'+rowData2+'\n'+rowData3+'\n')
console.log(output)



console.log('------------------------------- Q8')
console.log('For even or odd, use arguments as \"even\" or \"odd\"')

// using closures and currying to generalize Q3 and Q4
const general = multipleOf => {
    const n100 = 100
    // creating array of size 100 using spread operator and Array().keys()
    // map is used to increment each element by 1
    const arr100 = [...Array(n100).keys()].map(x => x+1)

    // filter is used to keep only the mulltiples
    const multiples = arr100.filter(x => x%multipleOf === 0)
    
    // expects string "even" or "odd"
    return (type) => {
        // used to filter even numbers
        if (type === 'even'){
            // filter is used to keep only even numbers
            return multiples.filter(x => x%2 === 0)
        }
        // used to filter odd numbers
        else if (type === 'odd'){
            // filter is used to keep only odd numbers
            return multiples.filter(x => x%2 === 1)
        }
        // handles unexpected string inputs
        else {
            throw Error('The expected types are even and odd. Unexpected input.')
        }
    }
}

// Below is an alternative code I wrote

// const general = multipleOf => {
//     const n100 = 100
//     const arr100 = [...Array(n100).keys()].map(x => x+1)
//     const multiples = arr100.filter(x => x%multipleOf === 0)

//     return (type) => type === 'even' ? multiples.filter(x => x%2 === 0) : multiples.filter(x => x%2 === 1)
// }

// passing first argument to currying function
const multiplesOf5 = general(5)
// passing second argument to currying function
const oddMultiplesOf5 = multiplesOf5('odd')
console.log('Q3 general version\n')
console.log(oddMultiplesOf5)

// passing first argument to currying function
const multiplesOf7 = general(7)
// passing second argument to currying function
const evenMultiplesOf7 = multiplesOf7('even')
console.log('Q4 general version\n')
console.log(evenMultiplesOf7)
