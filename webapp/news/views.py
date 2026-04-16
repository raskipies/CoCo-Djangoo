from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from main.models import Game, Purchase 
from .models import Articles, Bug, BugComment
from .forms import ArticlesForm

# Create your views here.

def news_home(request):
    bugs = Bug.objects.all().order_by('-created_at').prefetch_related('comments__author')
    
    user_purchases = []
    if request.user.is_authenticated:
        user_purchases = Purchase.objects.filter(user=request.user).select_related('game')

    if request.method == 'POST' and request.user.is_authenticated:
        action = request.POST.get('action')
        
        if action == 'report_bug':
            content = request.POST.get('content')
            game_id = request.POST.get('game_id')
            image = request.FILES.get('image')
            
            # Validate that user owns the selected game
            if content and game_id:
                game_purchase = Purchase.objects.filter(
                    user=request.user, 
                    game_id=game_id
                ).exists()
                
                if game_purchase:
                    Bug.objects.create(author=request.user, game_id=game_id, content=content, image=image)
                    return redirect('news_home')

        elif action == 'add_comment':
            bug_id = request.POST.get('bug_id')
            comment_content = request.POST.get('comment_content')
            if comment_content and bug_id:
                bug_instance = Bug.objects.get(id=bug_id)
                BugComment.objects.create(
                    bug=bug_instance,
                    author=request.user,
                    content=comment_content
                )
                return redirect('news_home')

    return render(request, 'news/index.html', {
        'news': bugs, 
        'user_purchases': user_purchases
    })

def news_create(request):
    error = ''

    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Submitted form contain errors'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/show.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/update.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete.html'
    success_url = '/news/'


@login_required(login_url='login')
def delete_bug(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    if request.user == bug.author:
        bug.delete()
    return redirect('news_home')


@login_required(login_url='login')
def delete_bug_comment(request, comment_id):
    comment = BugComment.objects.get(id=comment_id)
    if request.user == comment.author:
        comment.delete()
    return redirect('news_home')