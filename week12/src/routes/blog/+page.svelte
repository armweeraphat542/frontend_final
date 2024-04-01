<script>
    import { thumb } from '$lib/store.js';

    export let data

    function getthumbUp(slug) {
        const index = $thumb.posts.findIndex((post) => post.slug === slug)

        if (index !== -1) {
            return $thumb.posts[index].thumbUp
        }

        return 0
    }

    function getthumbDown(slug) {
        const index = $thumb.posts.findIndex((post) => post.slug === slug)

        if (index !== -1) {
            return $thumb.posts[index].thumbDown
        }

        return 0
    }
</script>


<div class="content">
<h1>Blog</h1>
    <ul>
        {#each data.summaries as {slug, title}}
            <li>
                <div class="grid">
                    <div class="cell">
                        <a href="./blog/{slug}">{title}</a>
                        <span class="icon">
                            <i class="fas fa-thumbs-up" aria-hidden="true"></i>{getthumbUp(slug)}
                        </span>
                        <span class="icon" >
                            <i class="fas fa-thumbs-down" aria-hidden="true"></i>{getthumbDown(slug)}
                        </span>
                </div>
            </li> 
        
        {/each}
    </ul>
</div>