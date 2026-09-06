from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    error = None

    if request.method == "POST":
        registration_id = request.POST.get(
            "registration_id", ""
        ).strip()

        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=registration_id,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        error = "Registration ID অথবা Password সঠিক নয়।"

    return render(
        request,
        "home.html",
        {"error": error},
    )


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@require_POST
def logout_view(request):
    logout(request)
    return redirect("home")