from pdb import post_mortem
from pipes import Template
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.views.generic.base import TemplateView
from .forms import CommentForm, CreatePostForm, UpdatePostForm
from .models import Post, Profile, CustomUser
from django.contrib import messages
from django.urls import reverse


class IndexView(TemplateView):
    template_name = 'blogs/index.html'

    def get(self, request):
        profile_list = Profile.objects.all()
        posts = Post.objects.all()
        context = {
            'profile_list' : profile_list,
            'posts' : posts
        }
        return render(request, self.template_name, context)

class createPostView(TemplateView):
    template_name = 'blogs/create_post.html'

    def get(self, request):
        
        form = CreatePostForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        
        createPostForm = CreatePostForm(request.POST, request.FILES)
            
        if createPostForm.is_valid():
            createPostForm = createPostForm.save(commit = False)
            createPostForm.authorEmail = request.user
            createPostForm.save()

            messages.success(request, 'Profile has been created successfully!')
            return redirect('blogs:index')

        else:
            createPostForm = CreatePostForm(request.user.profile)

        return render(request, 'blogs/create_post.html', {'createPostForm' : createPostForm})

class UpdatePostView(TemplateView):
    template_name = 'blogs/modify_post.html'

    def get(self, request, id):
       #load previous post data on form
        post = Post.objects.get(id=id)
        data = {
            'title' : post.title,
            'slug' : post.slug,
            'intro' : post.intro,
            'body' : post.body,
            'picture' : post.picture
        }
        form = UpdatePostForm(initial=data)
        context = {
            'post': post,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        #import pdb; pdb.set_trace()
        post = Post.objects.get(id=id)
        form = UpdatePostForm(request.POST, request.FILES, instance = post)

        if form.is_valid():
            form = form.save(commit=False)
            
            form.save()

            return redirect('blogs:postDetail', post.id)
        
        else:
            form = UpdatePostForm()
            return redirect('blogs:postModify', post.id)

    

def delete_Post(request, id):

    post = Post.objects.get(id=id)

    if post.authorEmail == request.user:
        post.delete()
        return HttpResponseRedirect(reverse("blogs:index"))
    
    return render(request, "blogs/delete_post.html")

def LikeView(request, id):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    isLiked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        isLiked = False
    else:
        post.likes.add(request.user)
        isLiked = True
    return HttpResponseRedirect(reverse('blogs:postDetail', args=[id]))

# def search_posts(request):
#     template_name = 'blogs/search_posts.html'

#     searchTypeVal = request.GET['searchType']
    
#     if request.method == "POST":

#         if searchTypeVal == 'posts':
#             searchedPosts = request.POST['searchedPosts']
#             posts = Post.objects.filter(title__contains=searchedPosts)
#             context = {
#                 'searchTypeVal' : searchTypeVal,
#                 'searchedPosts' : searchedPosts,
#                 'posts' : posts
#             }
#             return render(request, template_name, context)

#         elif searchTypeVal == 'profiles':
#             searchedPosts = request.POST['searchedPosts']
#             pFirstName = Profile.objects.filter(first_name__contains=searchedPosts)
#             pLastName = Profile.objects.filter(last_name__contains=searchedPosts)
#             context = {
#                 'searchTypeVal' : searchTypeVal,
#                 'searchedPosts' : searchedPosts,
#                 'pFirstName' : pFirstName,
#                 'pLastName' : pLastName
#             }
#             return render(request, template_name, context)

def search_posts(request):
    template_name = 'blogs/search_posts.html'
    
    if request.method == "POST":
        searchedPosts = request.POST['searchedPosts']
        posts = Post.objects.filter(title__contains=searchedPosts)
        context = {
            'searchedPosts' : searchedPosts,
            'posts' : posts
        }
        return render(request, template_name, context)


class PostDetailView(TemplateView):
    template_name = 'blogs/post_detail.html'

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        totalLikes = post.total_likes()
        profile_list = Profile.objects.all()
        isLiked =False
        form = CommentForm()

        if post.likes.filter(id=request.user.id).exists():
            isLiked= True
        context = {
            'totalLikes': totalLikes,
            'isLiked' : isLiked,
            'profile_list' : profile_list,
            'post': post,
            'form' : form,

        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        post = Post.objects.get(id=id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Profile has been created successfully!')
            return redirect('blogs:postDetail', post.id)

        else:
            form = CommentForm()
            return redirect('blogs:index')
            
# Create your views here.
