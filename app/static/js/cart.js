function addToCart(bookId, bookName, image, price) {
    fetch('/api/cart', {
        method: 'POST',
        body: JSON.stringify({
            "id": bookId,
            "name": bookName,
            "image": image,
            "price": price
        }),
        headers: {
            "Content-Type": 'application/json'
        }
    }).then(res => res.json()).then(data => {
        console.info(data);
        alert(data.message);
        window.location.reload(true);
    })
}

function removeFromCart(bookId, bookName, image, price) {
    fetch('/api/remove-item-cart', {
        method: 'POST',
        body: JSON.stringify({
            "id": bookId,
            "name": bookName,
            "image": image,
            "price": price
        }),
        headers: {
            "Content-Type": 'application/json'
        }
    }).then(res => res.json()).then(data => {
        console.info(data);
        alert(data.message);
        window.location.reload(true);
    })
}

function updateCartByInput(bookId, bookName, image, price) {
    fetch('/api/add_remove_cart', {
        method: 'POST',
        body: JSON.stringify({
            "id": bookId,
            "name": bookName,
            "image": image,
            "price": price,
            "quantity": document.getElementById('quantity' + bookId).value
        }),
        headers: {
            "Content-Type": 'application/json'
        }
    }).then(res => res.json()).then(data => {
        console.info(data);
        alert(data.message);
        window.location.reload(true);
    })
}


function pay() {
    if(confirm("Xác nhận đặt hàng ?") == true)
        fetch('/checkout', {
            method: 'POST',
            headers: {
                "Content-Type": 'application/json'
            }
        }).then(res => res.json()).then(data => {
            alert(data.message);
            window.location.reload(true);
        })
}

function alertOutOfProduct() {
    alert("Sản phẩm tạm hết hàng")
}