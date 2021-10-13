let addButton = document.getElementById("add-form")
let removeButton = document.getElementById("remove-form")
let cont = document.getElementById('id_extra_category_count')
let cont_value = cont.value
let ingredients= document.getElementsByName('ingredients')
let form = document.getElementById('form')

addButton.addEventListener('click',(e)=>{
    e.preventDefault()
    cont_value++
    let newingredients = ingredients[0].cloneNode(true)
    newingredients.setAttribute('name','extra_category_'+cont.value)
    newingredients.setAttribute('class','extra_category')
    let p = document.createElement("p")
    p.appendChild(newingredients)
    form.insertBefore(p, addButton) 
    cont.setAttribute('value',cont_value)
})

removeButton.addEventListener('click',(e)=>{
    e.preventDefault()
    if(cont_value>0){
        let fields = document.getElementsByClassName('extra_category')
        let parent = fields[cont_value-1].parentNode
        form.removeChild(parent)
        cont_value--
        cont.setAttribute('value',cont_value)
    }
})
