let ingredientform = document.querySelectorAll(".ingredient_form")
let container = document.querySelector("#form-container")
let addButton = document.getElementById("add-form")
let removeButton = document.getElementById("remove-form")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
let formnum = ingredientform.length-1


addButton.addEventListener('click',(e)=>{
    e.preventDefault()
    let newform = ingredientform[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')
    formnum ++
    newform.innerHTML = newform.innerHTML.replace(formRegex, `form-${formnum}-`)
    container.insertBefore(newform, addButton) 
    totalForms.setAttribute('value', `${formnum+1}`) 
})

removeButton.addEventListener('click',(e)=>{
    e.preventDefault()
    let divs = document.getElementsByClassName('ingredient_form')
    if(formnum>0){
        container.removeChild(divs[formnum]) 
        formnum--
        totalForms.setAttribute('value', `${formnum+1}`) 
    }
})