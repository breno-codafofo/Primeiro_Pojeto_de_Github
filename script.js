class Pessoa {
    constructor (nome, idade, bairro) {
        this.nome = nome
        this.idade = idade
        this.bairro = bairro
    }
    falar() {
        console.log(`${this.nome} tem ${this.idade} anos!`)
    }
    comer() {
        console.log(`${this.nome} comeu almôndegas hoje!`)
    }
}
const pessoa1 = new Pessoa("Breno", 16, "Fromtalis")
pessoa1.falar()