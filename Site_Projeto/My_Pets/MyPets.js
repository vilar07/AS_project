const wrapper = document.querySelector('.popup')
      form = wrapper.querySelectorAll(".form")

if (document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready(){
    submitInput.addEventListener('click', getDataForm, false)
}

function getDataForm(event){
    var formData = new FormData(form[0]);
    var fotografia =  formData.get('fotografia')
    var nome =  formData.get('nomeAnimal')
    var sexo = formData.get('sexo')
    var size = formData.get('size')
    var age = formData.get('age')
    addAnimaltoList(fotografia,age,nome,sexo,size)
}

function addAnimaltoList(fotografia,age,nome,sexo,size){
    var cartRow =  document.createElement('div')
    var cartItems= document.getElementsByClassName('anim')[0]
    cartRow.classList.add('anim')
    var cartRowContens = `
                        <div class="anim">
                            <div class="animal-info">
                                <img class= "animal-info-image" src="${fotografia}">
                                <h2>${nome}</h2>
                                <p><b>Name:</b> ${nome}</p>
                                <p><b>Sex:</b> ${sexo}</p>
                                <p><b>Age:</b> ${age} </p>
                                <p><b>Size:</b> ${size}</p>
                                <a href="http://127.0.0.1:5500/My_Pets/MyPets.html"><h3>More Informations</h3></a>
                            </div>
                        </div>` 
    cartRow.innerHTML =  cartRowContens
    cartItems.appendChild(cartRow)
  
}