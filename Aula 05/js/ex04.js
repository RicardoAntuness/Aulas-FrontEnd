function fraseProduto(produto, valor, quantidade) {
    let total = valor * quantidade;
    let frase = `${produto}, valor unitário: ${valor}, total da compra: ${total}`;

    return frase;
}

console.log(fraseProduto("iPhone", 6000, 3)) ;
console.log(fraseProduto("xBox", 4800.99, 2)) ;
console.log(fraseProduto("Notebook", 8000, 3)) ;