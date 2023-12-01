from django.shortcuts import render
from myapp.forms import CommentForm
from .models import UserComments
from django.http import JsonResponse


# Create your views here.
def form_view(request):
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user_comment = UserComments(
                first_name=clean_data["first_name"],
                last_name=clean_data["last_name"],
                comment=clean_data["comment"],
            )
            user_comment.save()
            return JsonResponse({'message': 'success'})

    return render(request, "blog.html", {"form": form})
