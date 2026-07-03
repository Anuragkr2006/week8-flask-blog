// ======================================
// Password Show / Hide
// ======================================

const togglePassword = document.getElementById("togglePassword");

if (togglePassword) {

    togglePassword.addEventListener("click", function () {

        const password = document.getElementById("password");

        const eyeIcon = document.getElementById("eyeIcon");

        if (password.type === "password") {

            password.type = "text";

            eyeIcon.classList.remove("bi-eye");

            eyeIcon.classList.add("bi-eye-slash");

        } else {

            password.type = "password";

            eyeIcon.classList.remove("bi-eye-slash");

            eyeIcon.classList.add("bi-eye");

        }

    });

}


// ======================================
// Auto Hide Alerts
// ======================================

setTimeout(function(){

    let alerts = document.querySelectorAll(".alert");

    alerts.forEach(function(alert){

        alert.classList.remove("show");

    });

},3000);


// ======================================
// Smooth Scroll
// ======================================

document.querySelectorAll('a[href^="#"]').forEach(anchor=>{

    anchor.addEventListener("click",function(e){

        e.preventDefault();

        document.querySelector(this.getAttribute("href"))

        ?.scrollIntoView({

            behavior:"smooth"

        });

    });

});