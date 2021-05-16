$(document).ready(utc2local);

function utc2local() {
    $('.UTCTime').text( (i, v) => new Date(v).toLocaleString());
}

document.getElementById('signupPass2').addEventListener('input', (event) => {
    const passw = document.getElementById('signupPass1').value;
    if(passw != event.target.value){
      event.target.classList.add('is-invalid');
      document.getElementById('signUpButton').disabled = true;
    } 
    else{
      event.target.classList.remove('is-invalid');
      document.getElementById('signUpButton').disabled = false;
    }
});
