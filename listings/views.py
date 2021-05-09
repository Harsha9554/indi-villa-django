from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from agents.models import Agent


def index(request):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 5)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {"listings": paged_listings}

    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    agent = get_object_or_404(Agent, name=listing.agent)

    context = {"listing": listing, "agent": agent}

    return render(request, "listings/listing.html", context)


def search(request):
    return render(request, "listings/search.html")
