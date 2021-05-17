$(document).ready(utc2local);

function utc2local() {
    $(".UTCTime").text((i, v) => new Date(v).toLocaleString());
}
if (document.getElementById("signupPass2"))
    document
        .getElementById("signupPass2")
        .addEventListener("input", (event) => {
            const passw = document.getElementById("signupPass1").value;
            if (passw != event.target.value) {
                event.target.classList.add("is-invalid");
                document.getElementById("signUpButton").disabled = true;
            } else {
                event.target.classList.remove("is-invalid");
                document.getElementById("signUpButton").disabled = false;
            }
        });

///Data
var authToken = null; //or store in a cookie?
var userid = null; //or store in a cookie?
var user = null;
var url = location.hostname; //use navigator to compute current url for requests

///DOM elements
var loginButton, loginPanel, username, password;

function setUp() {
    loginButton = document.getElementById("log");
    loginPanel = document.getElementById("login-panel");
    username = document.getElementById("username");
    password = document.getElementById("password");
    loginButton.onclick = function () {
        if (authToken == null) loginPanel.hidden = !loginPanel.hidden;
        else {
            logout();
            loginButton.innerHTML = "Login";
            loginPanel.hidden = true;
            renderTable([]);
        }
    };
}

//Expected data format
//{token:"HASHef+HASH', expiry:'2019-5-30T12:00'}
function login() {
    if (authToken != null) logout();
    else {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                responseData = JSON.parse(this.responseText);
                authToken = responseData["token"];
                loginButton.innerHTML = "Logout";
                loginPanel.hidden = true;
            } else if (this.readyState == 4) alert(this.statusText);
        };
        xhttp.open(
            "POST",
            "/api/tokens",
            true,
            (user = snum.value),
            (psw = pin.value)
        );
        xhttp.send();
    }
}

function logout() {
    if (authToken == null) return;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 204) {
            authToken = null;
            student = null;
            document.getElementById("log").value = "Login";
            loginPanel.hidden = true;
        } else {
            alert(this.statusText);
        }
    };
    xhttp.open("DELETE", "/api/tokens", true);
    xhttp.setRequestHeader("Authorization", "Bearer " + authToken);
    xhttp.send();
}
