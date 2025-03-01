from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def profile_list_view(request):
    context = {}
    return render(request, "profiles/list.html", context)

@login_required
def profile_view(request, username=None, *rgs, **kwargs):
    user = request.user
    print(user.has_perm('auth.view_user'))
    print(user.get_all_permissions())
    # profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj.id == user.id
    if is_me:
        if user.has_perm("visits.view_pagevisit"):
            pass
            # qs = PageVisit.object.all()
    return HttpResponse(f"Hello there {username} - {profile_user_obj.id} - {user.id} - {is_me}")