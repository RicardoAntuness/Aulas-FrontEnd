const numeros = [10, 5, 8, 20, 3];
let maior = numeros[0];

for(let i = 1; i < numeros.length; i++) {
    if(numeros[i] > maior) {
        maior = numeros[i];
    }
}
console.log(maior);

/* maior é igual a 10 */
/* 5 é maior que 10 */
/* 8 é maior que 10 */
/* 20 é maior que 10 */
/*armazena 20 porque armazena o maior*/