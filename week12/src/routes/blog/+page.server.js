import { METHODS } from 'http'

export async function load() {
    const res = await fetch('http://localhost:3000/posts')
    const posts = await res.json()
    
    console.log(`Fectching posts from server ${posts.length}post(s)`)
    return {
        summaries: posts.map((post) => ({
            id: post.id,
            slug: post.slug,
            title: post.title,
        }))
    }
}

export const actions = {
    delete: async ({ cookies, request}) => {
        const data = await request.formData()
        const postId = data.get('id')

        console.log(`Deleting post id=${postId}`)
        const res = await fetch(`http://localhost:3000/posts/${postId}`, {
            method: 'DELETE'
        })
    },

    create: async ({ cookies, request}) => {
        const data = await request.formData()
        console.log(`Adding a post with slug=${data.get('slug')}`)
        const post = {
            slug: data.get('slug'),
            title: data.get('title'),
            content: data.get('content')
        }

        const res = await fetch('http://localhost:3000/posts', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(post)

        })

        console.log(`Adding post get status ${res.status}`)
    }
}