//var updateBtns = document.getElementById('update-cart');

$(document).ready(function(){
   $(".update-cart").on("click", function(e){
        e.preventDefault();
        var productId = $(this).attr("data-product");
		var action = $(this).attr("data-action");
		console.log('productId:', productId, 'Action:', action)

		if (user == 'AnonymousUser'){
			//addCookieItem(productId, action)
			alert("you are not logged in ")
		}else{
			updateUserOrder(productId, action)
		}
   });

});


$(document).ready(function(){

    $("#form").on("submit", function(e){
        e.preventDefault();
        $.ajax({
           type:'POST',
           url:'/grocery/process_order'
        })
		if (user == 'AnonymousUser'){
			//addCookieItem(productId, action)
			alert("you are not logged in ")


		}else{
			updateUserOrder(productId, action)
		}
   });



});


function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')
    console.log(csrftoken)
		var url = '/grocery/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},

			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {

		    alert("Your Cart was UPDATED!!!!! ")
		    location.reload()


		});
}


 function submitFormData(){
	    	console.log('Payment button clicked')
	    	console.log('User is authenticated, sending data...')
            console.log(csrftoken)

			var shippingInfo = {

				'landmark':null,
				'number':null,
				'Address':null,
				'city':null,
				'State':null,
				'pincode':null,
			}

			if (shipping != 'False'){
	    		shippingInfo.address = form.Address.value
	    		shippingInfo.landmark = form.landmark.value
	    		shippingInfo.number = form.number.value
		    	shippingInfo.city = form.city.value
		    	shippingInfo.state = form.State.value
		    	shippingInfo.pincode = form.pincode.value
	    	}

	    	console.log('Shipping Info:', shippingInfo)

	    	var url = "/grocery/process_order/"
	    	fetch(url, {
	    		method:'POST',
	    		headers:{
	    			'Content-Type':'applicaiton/json',
	    			'X-CSRFToken':csrftoken,
	    		},
	    		body:JSON.stringify({'form':userFormData, 'shipping':shippingInfo}),

	    	})
	    	.then((response) => response.json())
	    	.then((data) => {
				console.log('Success:', data);
				alert('Transaction completed');

				window.location.href = "/grocery/home"

			})
}