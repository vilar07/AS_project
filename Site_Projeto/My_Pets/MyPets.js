const wrapper = document.querySelector('.popup')
      form = wrapper.querySelectorAll(".form")

if (document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready(){
    submitInput.addEventListener('click', getDataForm, false)
    
    var Animal_List = JSON.parse(localStorage.getItem("InfAnimal"))

    for (i = 0; i<Animal_List.length;i++){
        addAnimaltoList(Animal_List[i].foto,Animal_List[i].age,Animal_List[i].name,Animal_List[i].sex,Animal_List[i].size)
    }
    
}

function getDataForm(event){
    var formData = new FormData(form[0]);
    var fotografia =  formData.get('fotografia')
    var nome =  formData.get('nomeAnimal')
    var sexo = formData.get('sexo')
    var age = formData.get('age')
    var size = formData.get('size')

    
    const InfAnimal = {
        foto: fotografia,
        name: nome,
        sex: sexo,
        age: age,
        size: size
    }
    Animal_List = JSON.parse(localStorage.getItem("InfAnimal"))

    if (Animal_List !== null)
        addAnimaltoList(fotografia,age,nome,sexo,size)

    Animal_List.push(InfAnimal)
    localStorage.setItem("InfAnimal", JSON.stringify(Animal_List))
    
}

function addAnimaltoList(fotografia,age,nome,sexo,size){
    var cartRow =  document.createElement('div')
    var cartItems= document.getElementsByClassName('anim')[0]
    cartRow.classList.add('anim')
    var cartRowContens = `
                        <div class="anim">
                            <div class="animal-info">
                                <img class= "animal-info-image" src="${fotografia}">
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