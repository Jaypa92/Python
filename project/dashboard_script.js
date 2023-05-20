const user_pic = document.querySelector('#user_pic');
var uploaded_pic = '';

user_pic.addEventListener('change',function(){
    var reader = new FileReader();
    reader.addEventListener('load',() => {
        uploaded_pic = reader.result;
        document.querySelector('#display').getElementsByClassName.backgroundImage = 'url(${uploaded_pic})'
    })
    reader.readAsDataURL(this.files[0]);
})