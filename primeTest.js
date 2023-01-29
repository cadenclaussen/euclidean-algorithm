'use strict';
var generatePrimes = require('./prime');


let max = parseInt(process.argv[2]);
let primeNumbers = generatePrimes(max);
console.log(primeNumbers.length);
