
function entrar() {
    document.getElementById('divRight').style.color = 'blue'
    document.getElementById('divRight').style.background = 'rgb(165, 164, 164)'
}
      
function sair() {
    document.getElementById('divRight').style.background = 'white'
}

function leftEnter(){
    var sei = document.getElementById('imd_brinde')
    sei.innerHTML = 'Click AQUI  -- E SE  -- CADASTRE'
    sei.style.color = 'red'
    sei.style.fontSize = '60px'

}
function leftSair(){
    
    var sei = document.getElementById('imd_brinde')
    sei.innerHTML = 'Quer ganhar   um Brinde'
    sei.style.color = 'white'
    sei.style.fontSize = '90px'
    sei.style.textAlign = 'center';
    

