from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),  # (url에 표시될 단어, admin panel에 표시될 단어)
            ("great", "Great"),
        ]

    def queryset(self, request, reviews):
        # word = request.GET.get("word")
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class RatingFilter(admin.SimpleListFilter):
    title = "good or bad reviews"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, queryset):
        rating = self.value()
        if rating:
            if rating == "good":
                return queryset.filter(rating__gte=3)
            else:
                return queryset.filter(rating__lt=3)
        else:
            return queryset


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "payload")

    list_filter = (
        RatingFilter,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
    )
