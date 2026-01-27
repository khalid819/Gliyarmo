burger= document.querySelector('.burger')
navbar= document.querySelector('.navbar')
navlist= document.querySelector('.nav-list')
ro= document.querySelector('.line')
rt= document.querySelector('.p')
r= document.querySelector('.q')
burger.addEventListener('click',()=>{
    navbar.classList.toggle('hclass');
    navlist.classList.toggle('vclass');
    ro.classList.toggle('rt');
    rt.classList.toggle('r');
    r.classList.toggle('ro');
})