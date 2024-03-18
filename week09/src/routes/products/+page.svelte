<script>
    let title = "";
    let price = 0;

</script>



<div class="field">
    <label class="label">Title</label>
    <div class="control">
      <input class="input" type="text" bind:value={title} placeholder="Enter title">
    </div>
    <label class="label">Price</label>
    <div class="control">
      <input class="input" type="number" bind:value={price} placeholder="Enter price">
    </div>
</div>

<div>{title} + {price}</div>
