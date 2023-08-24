const cabecalho = document.querySelector("#cabecalho")
const menu = document.querySelector("#menu")
const btn_home = document.querySelector("#btn_home")
const btn_novo = document.querySelector("#btn_novo")
const btn_pesquisar = document.querySelector("#btn_pesquisar")
const btn_gestao = document.querySelector("#btn_gestao")
const btn_sobre = document.querySelector("#btn_sobre")
const principal = document.querySelector("#principal")
const if_principal = document.querySelector('if_principal')

btn_home.addEventListener('click',(evt)=>{
    selecionarAba(evt.target,'static/html/home.html')
})

btn_novo.addEventListener('click',(evt)=>{
    selecionarAba(evt.target,'static/html/novo.html')
})

btn_pesquisar.addEventListener('click',(evt)=>{
    selecionarAba(evt.target,'static/html/pesquisar.html')

})

btn_gestao.addEventListener('click',(evt)=>{
    selecionarAba(evt.target,'static/html/gestao.html')
})

btn_sobre.addEventListener('click',(evt)=>{
    selecionarAba(evt.target,'static/html/sobre.html')
})


const selecionarAba=(el,url)=>{
    const abas = [...document.querySelectorAll('.aba')]
    abas.map(e=>{
        e.classList.remove('abaSelecionada')
    })
    el.classList.add('abaSelecionada')
    window.open(url,'if_principal')

}