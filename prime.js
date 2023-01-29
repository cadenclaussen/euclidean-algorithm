'use strict';



function generatePrimes(max) {
    let primes = [ 2 ];
    for (let n = 3; n <= max; n++) {
        if (isPrime(n, primes)) {
            primes.push(n);
        }
    }
    return primes;
}


function isPrime(n, primes) {
    for (let prime of primes) {
        if (n % prime === 0) {
            return false;
        }
    }

    return true;
}


module.exports = generatePrimes;
