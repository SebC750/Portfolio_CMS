console.log("Hello world")

var num1: number = 20;

//Types vs Interfaces

type TPerson = {
    name: string;
    age: number;
    gender?: string;
    major?: string;
}
interface IPerson{
    name: string;
    age: number;
}

const person1: TPerson = {name: "Harry", age: 20}

const iperson1: IPerson = {name: "James", age: 27}


console.log(iperson1)
console.log(person1)
console.log(person1.name)
console.log(person1.age)