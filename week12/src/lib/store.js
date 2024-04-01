import { writable } from "svelte/store";

const initialThumb = {
    posts: [],
}

function createThumb() {
    const { subscribe, set, update } = writable(initialThumb)

    return {
        subscribe,
        thumbUp: (post) =>
            update((state) => {
                const index = state.posts.findIndex((item) => item.slug === post.slug)

                if(index !== -1 ) {
                    state.posts[index].thumbUp += 1
                } else {
                    state.posts.push({...post})
                }

                return state
            }),
            thumbDown: (post) =>
            update((state) => {
                const index = state.posts.findIndex((item) => item.slug === post.slug)

                if(index !== -1 ) {
                    state.posts[index].thumbDown += 1
                } else {
                    state.posts.push({...post})
                }

                return state
            })
    }
}

export const thumb = createThumb();

const exampleThumb = {
    posts: [
        {
            slug: '/welcome',
            thumbUp : 1,
            thumbDown :0
        },
        {
            slug: '/safe',
            thumbUp : 1,
            thumbDown :0
        },
    ]
}