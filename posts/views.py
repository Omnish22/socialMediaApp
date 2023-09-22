from django.shortcuts import render, redirect
from .forms import PostCreationForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def post_create(request):
    if request.method=="POST":
        form = PostCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # SINCE FORM HAS IMG, CAPT, TITLE FIELDS BUT WE NEED TO PROVIDE
            # OTHER FIELD USER ALSO NEED TO ADD TO FORM
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreationForm()
    return render(request, 'posts/create.html',{'post_form':form})


def feed(request):
    if request.method == 'POST':
        # GET DATA FROM COMMENT FORM
        comment_form = CommentForm(data=request.POST)
        # CREATE NEW COMMENT OBJECT BUT DON'T COMMIT IT 
        new_comment = comment_form.save(commit=False)
        # POST ID IS COMMING FROM COMMENT FORM
        post_id = request.POST.get('post_id')
        comment_by = request.POST.get('comment_by')
        # GET THE POST USING POST ID 
        post = get_object_or_404(Post, id=post_id)
        # ATTACH POST WITH COMMENT AS COMMENT FORM CONSIST ONLY BODY
        new_comment.post = post
        new_comment.comment_by = comment_by
        new_comment.save()
    else:
        comment_form = CommentForm()


    all_posts = Post.objects.all()
    return render(request, 'posts/feed.html', {'posts':all_posts, 'comment_form':comment_form})


def post_like(request):
    post_id = request.POST.get('post_id')
    print('post_id: ',post_id)
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id):
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed')