function isPositiveOrNegative(value) {
    if (value > 0 ) {
        return "positivo";
    }
    if (value < 0) {
        return "negativo";
    }
    return "neutro";
}


console.log(isPositiveOrNegative(1));      
console.log(isPositiveOrNegative(100));    
console.log(isPositiveOrNegative(-1000));  
console.log(isPositiveOrNegative(0));

/*let nome = prompt("Informe seu nome");
console.log(nome);*/