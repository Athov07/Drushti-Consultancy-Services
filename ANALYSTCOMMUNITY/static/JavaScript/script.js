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

