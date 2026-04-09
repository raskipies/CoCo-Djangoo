from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Comment, Post, PostLike


def index(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            login_url = reverse('login_user')
            return redirect(f'{login_url}?next={request.path}')

        action = request.POST.get('action')
        if action == 'create_post':
            content = request.POST.get('content', '').strip()
            image = request.FILES.get('image')
            if content:
                Post.objects.create(author=request.user, content=content, image=image)

        elif action == 'toggle_like':
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            like, created = PostLike.objects.get_or_create(post=post, user=request.user)
            if not created:
                like.delete()

        elif action == 'add_comment':
            post_id = request.POST.get('post_id')
            content = request.POST.get('comment_content', '').strip()
            post = get_object_or_404(Post, id=post_id)
            if content:
                Comment.objects.create(post=post, author=request.user, content=content)

        return redirect('forum_index')

    posts = Post.objects.prefetch_related('comments__author', 'likes__user').all()
    liked_post_ids = []
    if request.user.is_authenticated:
        liked_post_ids = list(request.user.postlike_set.values_list('post_id', flat=True))
    return render(request, 'forum/index.html', {
        'posts': posts,
        'liked_post_ids': liked_post_ids,
    })


def delete_post(request, post_id):
    if not request.user.is_authenticated:
        login_url = reverse('login_user')
        return redirect(f'{login_url}?next={request.path}')

    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
    return redirect('forum_index')


def delete_comment(request, comment_id):
    if not request.user.is_authenticated:
        login_url = reverse('login_user')
        return redirect(f'{login_url}?next={request.path}')

    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        comment.delete()
    return redirect('forum_index')


def frequent_questions(request):
    return render(request,'forum/frequent_questions.html') 