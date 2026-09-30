


let btn=document.getElementById("button")
console.log(btn)
btn.onclick=e=>{
    let b1=document.getElementById("loki").value
    let b2=document.getElementById("date").value
    console.log(b1,b2)
    fetch('/recv',
        {
            method:"post",
            body:JSON.stringify({'task_name':b1,'due_date':b2})
        }
    ).then(res =>res.json())
    .then(r =>{
        if(r.status==='ok'){
            window.location.reload()
        }
    })   
    .catch(e => console.log("error",e))
}




function is_delete(a){
    console.log(a)
    fetch("task_delete?task_id="+a ,{
        method:"delete"
    }).then (res=> res.json())
    .then(r =>{
      console.log(r)
        window.location.reload()
    })
}




function mark_complete(a){
    console.log(a)
    fetch("is_put?task_id="+a,{
        method:"PUT"
    }).then (res => res.json())
    .then(r =>{
        if(r.status==="ok"){
            window.location.reload()
        }
        else{
            alert('something is wrong')
        }

    })
}