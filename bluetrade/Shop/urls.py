from django.urls import path
from django.conf.urls import url
from . import views, search, post, update, delete, recommend, offer, user

app_name = 'api'

urlpatterns = [
    # Test-Use functions in the following
    path('', views.AllCommodity),
    path('commodity/', views.AllCommodity),
    path('users/', views.AllUser),


    # CRUD functions in the following
    #
    # Create functions
    url(r'^post-form/?$', post.post_form),
    url(r'^post/?$', post.postCommodity),
    # url(r'^post_image_form/?$', post.post_image),
    # url(r'^post_image/?$', post.post_image_handle),
    url(r'^post_list/?$', search.searchByOwner),
    url(r'^post_bidding/?$', offer.offerCommodity),
    # Read functions
    url(r'^search-form/?$', search.search_form),
    url(r'^search/?$', search.searchCommodity),
    url(r'^search-id-form/?$', search.search_id_form),
    url(r'^search-id/?$', search.searchById),
    url(r'^search-owner/?$', search.searchByOwner),
    url(r'^item/?$', search.searchById),
    # Update functions
    url(r'^update-form/?$', update.update_form),
    url(r'^update/?$', update.updateCommodity),
    url(r'^update_item/?$', update.updateCommodity),
    # Delete functions
    url(r'^delete/?$', delete.deleteCommodity),
    url(r'^delete-item/?$', delete.deleteCommodityPost),
    url(r'^delete_item/?$', delete.deleteCommodityPost),


    # Offer Related functions in the following
    #
    # **[Backend Test Use]** The form of posting an offer (from buyers to an owner)
    url(r'^offer-form/?$', offer.offer_form),
    # Post an offer (from buyers to an owner)
    url(r'^offer/?$', offer.offerCommodity),
    # Confirm an offer (from an owner to one buyer)
    url(r'^offer-confirm/?$', offer.offerConfirmation),
    # Search all offers of one commodity (with its ID)
    url(r'^offer-commodity/?$', offer.offerByCommodityID),
    # Search all offers of one buyer (with its ID)
    url(r'^offer-buyer/?$', offer.offerByBuyerID),
    # Search all offers of one buyer (with its Email)
    url(r'^offer-buyer-email/?$', offer.offerByBuyerEmail),

    url(r'^buying_bidding/?$', offer.offerStillBuying),
    url(r'^seller_bidding/?$', offer.offerStillSelling),
    url(r'^completed_bidding/?$', offer.offerCompleted),

    url(r'^update_bidding/?$', offer.offerCommodityUpdate),
    url(r'^select/?$', offer.offerConfirmationPost),

    # Recommendation functions in the following
    #
    url(r'^recommend/?$', recommend.recommendCommodity),


    # Register and Login functions in the following
    #
    url(r'^register/?$', views.user_register),
    url(r'^login/?$', views.user_login),


    # User Related functions in the following
    #
    url(r'^consumer/?$', user.getInfo),
    url(r'^manage_profile/?$', user.changeName),
    url(r'^change_avatar/?$', user.changeAvatar),
    url(r'^check_post_authentication/?$', user.checkAuth),

    url(r'^complete_order/?$', offer.offerComplete),

    url(r'^top_recommendation/?$', search.recommend),
    url(r'^change_phone/?$', user.changePhone),


]
