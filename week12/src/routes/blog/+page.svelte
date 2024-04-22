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
<form method="POST" action="?/create">
    <div class="field">
        <label class="label">
            <span>Slug</span>
            <div class="control">
                <input name="slug" class="input" type="text" placeholder="Slug">
              </div>
        </label>
      </div>
      <div class="field">
        <label class="label">
            <span>Title</span>
            <div class="control">
                <input name="title" class="input" type="text" placeholder="Title">
              </div>
        </label>
      </div>
      <div class="field">
        <label class="label">
            <span>Content</span>
            <div class="control">
                <input name="content" class="input" type="text" placeholder="Content">
              </div>
        </label>
      </div>
      <input class="button" type="submit" value="Add post" />
</form>
    <ul>
        {#each data.summaries as {id, slug, title}}
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
                        <form method="POST" action="?/delete">
                            <input type="hidden" name="id" value={id}>
                            <button class="button" type="submit">
                                <span class="icon is-small" >
                                    <i class="fas fa-exclamation-triangle"></i>
                                </span>
                            </button>
                        </form>
                </div>
            </li> 
        
        {/each}
    </ul>
</div>