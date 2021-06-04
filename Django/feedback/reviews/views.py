from django.db.models import base
from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {"form": form})

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         else:
#             return render(request, "reviews/review.html", {"form": form})


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:  # GET request
        form = ReviewForm()  # Empty form

    return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     return base_query.filter(rating__gt=3)


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "review"
