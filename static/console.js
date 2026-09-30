let r=document.getElementById('numbers')
let b=document.getElementById('name')
let c=document.getElementById('sub')
function add() {
    f1 = parseFloat(r.value)
    f2 = parseFloat(b.value)
    console.log(f1+f2)
    c.value=f1+f2
}


let btn = document.getElementById('sub-btn')
btn.onclick = add





