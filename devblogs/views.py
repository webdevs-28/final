from django.shortcuts import render,HttpResponse,redirect
from devblogs.models import Post,BlogCommnets
from django.contrib import messages

# Create your views here.
def bloghome(request):
    allposts  = Post.objects.all()
    context = {'allposts':allposts}
    return render(request,'blog/bloghome.html',context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogCommnets.objects.filter(post=post)
    context = {'post':post,'comments':comments,'user': request.user}
    return render(request,'blog/blogpost.html', context)

def postcomment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postsno  = request.POST.get('postsno')
        post = Post.objects.get(sno=postsno)
        parentsno = request.POST.get('parentsno')
        if parentsno == "":
            comment = BlogCommnets(comment=comment,user=user,post=post)
            comment.save()  
            messages.success(request,"comment posted")
        else:
            parent = BlogCommnets.objects.get(sno=parentsno)
            comment = BlogCommnets(comment=comment,user=user,post=post,parent=parent)
            comment.save()  
            messages.success(request,"reply posted")
        
    return redirect(f'/blog/{post.slug}')