from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from posts.models import Post

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # CLEAN THE FORM DATA
            data = form.cleaned_data

            # AUTHENTICATE AND GET RETURN AS USER OBJECT
            user = authenticate(request, username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                return redirect("feed")
            else:
                return HttpResponse("User Invalid")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

@login_required
def index(request):
    current_user = request.user
    current_user_posts = Post.objects.filter(user=current_user)
    profile = Profile.objects.filter(user=current_user).first

    return render(request, 'users/index.html', {'user_posts':current_user_posts, 'profile':profile})

def register(request):
    if request.method=='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # USER WILL NOT BE SAVED IN DB IF COMMIT=FALSE
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # AS SOON AS USER CREATED PROFILE SHOULD BE CREATED AS WELL
            Profile(new_user).save()
            return render(request, 'users/user_registeration_completed.html')

    user_form = UserRegistrationForm()
    return render(request, 'users/user_registration.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        # instance=request.user: This parameter tells the form to populate its fields with data from the request.user object. 
        # request.user typically represents the currently logged-in user in a Django web application.
        user_edit_form = UserEditForm(instance=request.user, data=request.POST)
        profile_edit_form = ProfileEditForm(instance=request.user.profile, data=request.POST)

        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
        
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit.html', {'user_edit':user_edit_form, 'profile_edit':profile_edit_form})