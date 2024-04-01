<script>
    import { thumb } from '$lib/store.js';

    export let data

    function thumbUp() {
        thumb.thumbUp({
            slug: data.post.slug,
            thumbUp: 1,
            thumbDown: 0,
        })
        console.log($thumb)
    }

    function thumbDown() {
        thumb.thumbDown({
            slug: data.post.slug,
            thumbUp: 0,
            thumbDown: 1,
        })
        console.log($thumb)
    }
</script>


<div class="content">
    <h1>{data.post.title}</h1>
    <div>{@html data.post.content}</div>

</div>
<div class="grid">
    <div class="cell">
        <button class="button" on:click={thumbUp}>
            <span class="icon">
                <i class="fas fa-thumbs-up" aria-hidden="true"></i>
            </span>
        </button>

        <button class="button" on:click={thumbDown}>
            <span class="icon" >
                <i class="fas fa-thumbs-down" aria-hidden="true"></i>
            </span>
        </button>
    </div>

</div>