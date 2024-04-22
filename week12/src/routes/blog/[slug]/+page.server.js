import { error } from "@sveltejs/kit";
import { create } from "domain";

export async function load({params}) {
    const res = await fetch(`http://localhost:3000/posts?slug=${params.slug}`)
    const posts = await res.json()
    const post = posts[0]
    console.log(post)

    if (!post) throw error(404)

    return {
        post
    }
}

