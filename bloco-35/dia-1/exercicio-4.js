const numbers = [0,1,2,3,4,5,6,7,8,9]
numbers.map(n => n*n)
       .filter(n => n%2 === 0)
       .reduce((acc, n) => acc + n)

// O(3n), a função itera pelo array inteiro 3 vezes seguidas, mas não de forma aninhada
// assim ela não tem complexidade O(n³) e sim O(n + n + n) ou simplemente O(n)