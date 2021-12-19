from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from shopping.models import Post, Comment


def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/landing.html',
                  {'recent_posts' : recent_posts})

def about_me(request):
    return render(request, 'single_pages/about_me.html')

@login_required
def my_page(request):
    comments = Comment.objects.all()
    comments_list = comments.filter(comment_user=request.user.username) # 내가 쓴 댓글만
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    paginator = Paginator(comments_list, 6)
    posts = paginator.get_page(page)
    return render(request, 'single_pages/mypage.html', {'comments_list' : comments_list, 'posts' : posts})
