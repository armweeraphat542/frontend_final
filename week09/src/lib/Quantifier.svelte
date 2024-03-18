<script>
    export let image ="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png"
	export let quantity = 0
    export let price = 200
    export let title = "Product"
    let totalPrice = 0
    

    $: {
        totalPrice = quantity * price
        console.log("Total Price" + totalPrice)
		
    }
	function increment() {
		quantity += 1
		
	}

	function decrement() {
		if (quantity === 0){
			return
			
		}
		quantity -= 1
		
	}
</script>

<div class="box">
    <div class="field">
        <span><img src="{image}" alt="{title}" width="100"></span>
        <span>Product: {title}</span>
    </div>    
    <div class="field">
        <span>Current quantity {quantity}</span>
        <span>Price: {price}</span>
        <span>Total: {totalPrice}</span>
    </div>       
    <div class="field">   
        <button class="button is-danger" on:click={decrement}> - </button>
        <button class="button is-danger" on:click={increment}> + </button>
    </div> 
</div>

