// function validate() {
//     var u = document.getElementById("username").value;
//     var p1 = document.getElementById("password").value;
//     var p2 = document.getElementById("password-repeat").value;
//
//     if (u == "") {
//         alert("Vui lòng nhập tên!");
//         return false;
//     }
//     if (p1 == "") {
//         alert("Vui lòng nhập mật khẩu!");
//         return false;
//     }
//     if (p2 == "") {
//         alert("Vui lòng xác minh mật khẩu!");
//         return false;
//     }
//
//     alert("Xin hãy điền đúng thông tin!")
//
//     return true;
// }

function checkPhone() {
    var vnf_regex = /((09|03|07|08|05)+([0-9]{8})\b)/g;
    var phone = $('#billing_phone').val();
    if (phone !== '') {
        if (vnf_regex.test(phone) == false) {
            alert('Số điện thoại của bạn không hợp lệ!');
            return false;
        } else {
            return true
        }
    }
}