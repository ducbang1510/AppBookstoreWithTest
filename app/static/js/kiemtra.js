function checkPhone() {
    var regExp = /^(0[234][0-9]{8}|1[89]00[0-9]{4})$/;
    var phone = document.getElementById("phone").value;
    if (regExp.test(phone))
        alert('SĐT hợp lệ!');
    else
        alert('SĐT không hợp lệ!');
}

function checkName() {
    var regExp = /^[A-Za-z\s]+$/;
    var name_dk = document.getElementById("name_dk").value;
    if (regExp.test(name_dk)) {
        document.getElementById("message-name").innerHTML = " ";
        return true;
    } else {
        document.getElementById("message-name").innerHTML = "Họ tên không hợp lệ!";
        return false;
    }
}


function checkEmail() {
    var regExp = /^[A-Za-z][\w$.]+@[\w]+\.\w+$/;
    var email_dk = document.getElementById("email_dk").value;
    if (regExp.test(email_dk)) {
        document.getElementById("message-mail").innerHTML = " ";
        return true;
    }
    else{
        document.getElementById("message-mail").innerHTML = "Email không hợp lệ!";
        return false;
    }
}

function checkUsername() {
    var regExp = /^[A-Za-z0-9]+$/;
    var username_dk = document.getElementById("username_dk").value;
    if (regExp.test(username_dk)) {
        document.getElementById("message-username").innerHTML = " ";
        return true;
    } else {
        document.getElementById("message-username").innerHTML = "Username không hợp lệ!";
        return false;
    }
}

function checkPassword() {
    var num = {};
    num.Lower = 0;
    num.Upper = 0;
    num.Numbers = 0;
    num.Symbols = 0;
    var password_dk = document.getElementById("password_dk").value;
    for (i = 0; i < password_dk.length; i++) {
        if (password_dk[i].match(/[a-z]/g)) {
            num.Lower++;
        }
        if (password_dk[i].match(/[A-Z]/g)) {
            num.Upper++;
        }
        if (password_dk[i].match(/[0-9]/g)) {
            num.Numbers++;
        }
        if (password_dk[i].match(/\W/g)) {
            num.Symbols++;
        }
    }
    if (num.Upper && num.Numbers && num.Symbols && num.Lower && password_dk.length > 5 && password_dk.length < 31) {
        document.getElementById("message-password").innerHTML = " ";
        return true;
    } else if (password_dk.length < 6 || password_dk.length > 30) {
        document.getElementById("message-password").innerHTML = "Password phải từ 6 tới 30 kí tự";
        return false;
    } else {
        document.getElementById("message-password").innerHTML = "Password phải có đầy đủ kí tự thường, kí tự hoa, số và kí tự đặc biệt";
        return false;
    }
}

function submitFormRegister() {
    if (checkPassword()==true && checkUsername()==true && checkEmail()==true) {
        document.getElementById("register").submit()
    }
}
