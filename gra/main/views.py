from django.shortcuts import render,redirect
from .models import MainCategory,ArticleSeries,MainArticle





# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories": MainCategory.objects.all})






def single_slug(request, single_slug):
    # first check to see if the url is in categories.

    categories = [c.cat_slug for c in MainCategory.objects.all()]
    if single_slug in categories:
        matching_series = ArticleSeries.objects.filter(main_category__cat_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = MainArticle.objects.filter(article_series__article_series=m.article_series).earliest("date_published")
            series_urls[m] = part_one.article_slug

        return render(request=request,
                      template_name='main/category.html',
                      context={"tutorial_series": matching_series, "part_ones": series_urls})

    article = [t.article_slug for t in MainArticle.objects.all()]

    if single_slug in article:
        this_article = MainArticle.objects.get(article_slug=single_slug)
        article_from_series = MainArticle.objects.filter(article_series__article_series=this_article.article_series).order_by('date_published')
        this_article_idx = list(article_from_series).index(this_article)

        return render(request=request,
                      template_name='main/articles.html',
                      context={"article": this_article,
                               "sidebar": article_from_series,
                               "this_art_idx": this_article_idx})


        