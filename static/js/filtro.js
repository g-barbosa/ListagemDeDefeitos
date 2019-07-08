var campoFiltroPlaca = document.querySelector("#placa");
var campoFiltroComponente = document.querySelector("#componente");
var campoFiltroDefeito = document.querySelector("#defeito");

campoFiltroPlaca.addEventListener("input", function(){
    var placas = document.querySelectorAll(".infoDefeito");

    if (this.value.length > 0){
        for (var i = 0; i < placas.length; i++){
            var placa = placas[i];
            var tdNomePlaca = placa.querySelector(".nomePlaca");
            var nomePlaca = tdNomePlaca.textContent;
            var expressao = new RegExp(this.value, "i");

            if (!expressao.test(nomePlaca)){
                placa.classList.add("apaga");
            } else {
                placa.classList.remove("apaga");
            }
        }
    }else {
        for (var i=0;i < placas.length; i++){
            var placa = placas[i];
            placa.classList.remove("apaga");
        }
    }
});

campoFiltroComponente.addEventListener("input", function(){
    var placas = document.querySelectorAll(".infoDefeito");

    if (this.value.length > 0){
        for (var i = 0; i < placas.length; i++){
            var placa = placas[i];
            var tdNomeComp = placa.querySelector(".nomeComp");
            var nomeComp = tdNomeComp.textContent;
            var expressao = new RegExp(this.value, "i");

            if (!expressao.test(nomeComp)){
                placa.classList.add("apaga");
            } else {
                placa.classList.remove("apaga");
            }
        }
    }else {
        for (var i=0;i < placas.length; i++){
            var placa = placas[i];
            placa.classList.remove("apaga");
        }
    }
});

campoFiltroDefeito.addEventListener("input", function(){
    var placas = document.querySelectorAll(".infoDefeito");

    if (this.value.length > 0){
        for (var i = 0; i < placas.length; i++){
            var placa = placas[i];
            var tdNomeDef = placa.querySelector(".nomeDef");
            var nomeDef = tdNomeDef.textContent;
            var expressao = new RegExp(this.value, "i");

            if (!expressao.test(nomeDef)){
                placa.classList.add("apaga");
            } else {
                placa.classList.remove("apaga");
            }
        }
    }else {
        for (var i=0;i < placas.length; i++){
            var placa = placas[i];
            placa.classList.remove("apaga");
        }
    }
});