let tovar_hajm = document.querySelector('#mahsulot_hajm')
let tovar_soni = document.querySelector('#mahsulot_soni')
let umumiy_miqdor = document.querySelector('#umumiy_miqdor')

//radio
let radio_dona = document.getElementById('radioinline1')
let radio_kilagram = document.getElementById('radioinline2')
let radio_litr = document.getElementById('radioinline3')

//input
let My_maxsulot = document.getElementById('My_maxsulot')
let My_Jami = document.getElementById('My_Jami')

//foiz qo'yish
let kelgan_narxi = document.getElementById('kelgan_narxi')
let Foiz = document.getElementById('foizi')
let sotlish_narxi = document.getElementById('sotlish_narxi')



//function count
tovar_soni.addEventListener('input', function() {
    if (this.value != ''){
        let umumiy_jami = tovar_hajm.value * tovar_soni.value
        umumiy_miqdor.value = Math.floor(umumiy_jami)
    }
});


//function radio

radio_dona.onclick = function radio_dona() {
    My_maxsulot.style.display = 'none'
    My_Jami.style.display = 'none'
}

radio_kilagram.onclick = function radio_kilagram() {
    My_maxsulot.style.display = 'block'
    My_Jami.style.display = 'block'
}

radio_litr.onclick = function radio_litr() {
    My_maxsulot.style.display = 'block'
    My_Jami.style.display = 'block'
}

//function foiz qoyish
Foiz.addEventListener('input',function() {
    if (this.value != '' ) {
        let cost = parseInt(((kelgan_narxi.value / 100) * Foiz.value)) + parseInt(kelgan_narxi.value)
        sotlish_narxi.value = Math.floor(cost)     
    }
})



