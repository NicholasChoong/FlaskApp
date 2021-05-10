user = 1;

if(user == 1){
    document.getElementById('noSignIn').hidden = true;
    document.getElementById('noCompleted').hidden = true;
    document.getElementById('testAccordion').hidden = false;
}
else if(user == 2){
    document.getElementById('noSignIn').hidden = true;
    document.getElementById('noCompleted').hidden = false;
    document.getElementById('testAccordion').hidden = true;
}
else{
    document.getElementById('noSignIn').hidden = false;
    document.getElementById('noCompleted').hidden = true;
    document.getElementById('testAccordion').hidden = true;
} 