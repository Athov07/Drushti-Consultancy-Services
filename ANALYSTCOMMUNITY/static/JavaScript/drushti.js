function showSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'flex'
}

function hideSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'none'
}


function toggleNav() {
    const navLink = document.getElementById("nav-links");
    if (navLink.style.display === "block") {
      navLink.style.display = "none";
    } else {
      navLink.style.display = "block";
    }
  }

// script for FAQs

let li = document.querySelectorAll(".faq-text li");
     for(var i=0 ; i<li.length ; i++){
        li[i].addEventListener("click", (e)=>{
            let clickedLi;
            if(e.target.classList.contains("question-arrow")){
                clickedLi = e.target.parentElement;
            }else{
                clickedLi = e.target.parentElement.parentElement;
            }
            clickedLi.classList.toggle("showAnswer");
        });
    }
// li.forEach(question =>{
//     question.addEventListener("click", (e)=>{
//                 let clickedLi;
//                 if(e.target.classList.contains("question-arrow")){
//                     clickedLi = e.target.parentElement;
//                 }else{
//                     clickedLi = e.target.parentElement.parentElement;
//                 }
//                 clickedLi.classList.toggle("showAnswer");
//     });
// })

// script for plan 
function togglePopupP() { 
    const overlay = document.getElementById('popupOverlay11'); 
    overlay.classList.toggle('show'); 
}
