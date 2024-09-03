from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages

from account.models import Account


class ProfileView(View):
    def get(self, request, username):
        account = Account.objects.get(username=username)
        context = {
            "account": account
        }
        return render(request, "account/profile.html", context=context)


class FollowView(LoginRequiredMixin, View):
    def get(self, request, username):
        account = request.user
        user = Account.objects.get(username=username)
        type = request.GET.get('type')
        if type == "follow":
            account.following.add(user)
            messages.success(request, "You are successfully followed")
        elif type == "unfollow":
            account.following.remove(user)
            messages.success(request, "You are successfully unfollowed")
        else:
            messages.error(request, "Bad credentials")

        return redirect("account:profile", username=username)
