from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from agents.models import Agent
from django.http import JsonResponse, HttpResponse
from listings.choices import (
    city_choices,
    state_choices,
    category_choices,
    type_choices,
    bedroom_choices,
    bathroom_choices,
    garage_choices,
    current_status,
    buy_status,
)
from django.template.loader import render_to_string


def index(request):
    if not request.method == "POST":
        listings = Listing.objects.order_by("-list_date")

        paginator = Paginator(listings, 5)
        page = request.GET.get("page")
        paged_listings = paginator.get_page(page)

        context = {
            "listings": paged_listings,
            "city_choices": city_choices,
            "state_choices": state_choices,
            "category_choices": category_choices,
            "type_choices": type_choices,
            "bedroom_choices": bedroom_choices,
            "bathroom_choices": bathroom_choices,
            "garage_choices": garage_choices,
        }

        return render(request, "listings/listings.html", context)
    else:
        query_listings = Listing.objects.order_by("-list_date")
        # state
        if "state" in request.POST:
            state = request.POST["state"]
            if state:
                query_listings = query_listings.filter(state=state)

        # city
        if "city" in request.POST:
            city = request.POST["city"]
            if city:
                query_listings = query_listings.filter(city=city)

        if "category" in request.POST:
            category = request.POST["category"]
            if category:
                query_listings = query_listings.filter(listing_category=category)

        if "l_type" in request.POST:
            l_type = request.POST["l_type"]
            if l_type:
                query_listings = query_listings.filter(listing_type=l_type)

        if "bedrooms" in request.POST:
            bedrooms = request.POST["bedrooms"]
            if bedrooms:
                query_listings = query_listings.filter(bedrooms=bedrooms)

        if "bathrooms" in request.POST:
            bathrooms = request.POST["bathrooms"]
            if bathrooms:
                query_listings = query_listings.filter(bathrooms=bathrooms)

        if "garage" in request.POST:
            garage = request.POST["garage"]
            if garage:
                query_listings = query_listings.filter(garage=garage)

        # if "current_status" in request.POST:
        #     current_status = request.POST["current_status"]
        #     if current_status:
        #         query_listings = query_listings.filter(listing_current_status=current_status)

        # if "buy_status" in request.POST:
        #     buy_status = request.POST["buy_status"]
        #     if buy_status:
        #         query_listings = query_listings.filter(listing_buy_status=buy_status)

        paginator = Paginator(query_listings, 5)
        page = request.GET.get("page")
        paged_listings = paginator.get_page(page)

        context = {
            "listings": paged_listings,
            "city_choices": city_choices,
            "state_choices": state_choices,
            "category_choices": category_choices,
            "type_choices": type_choices,
            "bedroom_choices": bedroom_choices,
            "bathroom_choices": bathroom_choices,
            "garage_choices": garage_choices,
        }

        return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    agent = get_object_or_404(Agent, name=listing.agent)

    context = {"listing": listing, "agent": agent}

    return render(request, "listings/listing.html", context)


def search(request):
    return render(request, "listings/search.html")
