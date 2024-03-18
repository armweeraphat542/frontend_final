<script>
  import Quantifier from "$lib/Quantifier.svelte";

  const tours = [
    {
      image: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png",
      title: 'Phuket',
      quantity: 6,
      price: 25000
    },
    {
      image: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png",
      title: 'Thammasat Fair',
      quantity: 1,
      price: 450000
    },
    {
      image: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png",
      title: 'Bangkok',
      quantity: 7,
      price: 500
    },   
    {
      image: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png",
      title: 'Chaingmai',
      quantity: 5,
      price: 5000
    }

  ]

</script>


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png" alt="Google" width="300px" height="300px">


{#each tours as tour }
  {#if tour.price < 10000}
    <p style="color: red" >Super Cheap</p>
  {/if}

    <div><Quantifier {...tour} /></div>

{/each}

