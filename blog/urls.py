from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView, name='home'),
    path('article/<int:pk>', ArticleDetailView, name="article-detail"),
    path('article/all/',  ArticleListView, name="article-all"),
    path('author/<int:pk>', views.profile_view, name="author-detail"),
    path('category/<str:cats>/', CategoryView, name='category-detail'),
    path('category/', CategoryListView, name='category-all'),
    path('author/all/', ProfileListView, name='author-all'),

    path('contact/', ContactView, name='contact'),

    path('terms_and_conditions/', TermsConditionsView, name='terms_and_conditions'),
    path('privacy_policy/', PrivacyPolicyView, name='privacy_policy'),
    path('about/', AboutPageView, name='about_page'),
    
    path('newsletter/sign_up/', newsletter_signup_view, name='newsletter_signup'),
    path('newsletter/unsubscribe/', newsletter_unsubscribe_view, name='newsletter_unsubscribe'),
    path('newsletter/', newsletter_creation_view, name='newsletter_creation'),
    path('newsletter/add_user/', newsletter_add_user_view, name='newsletter_add_user'),
    path('newsletter/remove_user/', newsletter_remove_user_view, name='newsletter_remove_user'),
    path('newsletter/admin_panel/', newsletter_manage_admin_panel_view, name='newsletter_admin_panel'),
    path('newsletter/<int:pk>/', newsletter_detail_admin_panel_view, name='newsletter_detail_admin_panel'),
    path('newsletter/edit/<int:pk>/', newsletter_edit_admin_panel_view, name='newsletter_edit_admin_panel'),
    path('newsletter/delete/<int:pk>/', newsletter_delete_admin_panel_view, name='newsletter_delete_admin_panel'),
    path('newsletter/user/admin_panel/', newsletter_user_manage_admin_panel_view, name='newsletter_user_admin_panel'),
    path('newsletter/user/<int:pk>/', newsletter_user_detail_admin_panel_view,
         name='newsletter_user_detail_admin_panel'),
    path('newsletter/user/delete/<int:pk>/', newsletter_user_delete_admin_panel_view,
         name='newsletter_user_delete_admin_panel'),

    path('admin/', admin_panel_view, name='admin'),
    path('admin/newsletters/', newsletters_admin_panel_view, name='newsletters_admin'),
    path('admin/users/', users_admin_panel_view, name='users_admin'),
    path('admin/posts/', posts_admin_panel_view, name='posts_admin'),

    path('author/add_author/', author_add_view, name='author_add'),
    path('author/admin_panel/', author_manage_admin_panel_view, name='author_admin_panel'),
    path('author/<int:pk>/', author_detail_admin_panel_view, name='author_detail_admin_panel'),
    path('author/edit/<int:pk>', author_edit_admin_panel_view, name='author_edit_admin_panel'),
    path('author/delete/<int:pk>', author_delete_admin_panel_view, name='author_delete_admin_panel'),

    path('cateogry/add_category/', category_add_view, name='category_add'),
    path('category/manage/admin_panel/', category_manage_admin_panel_view, name='category_admin_panel'),
    path('category/detail/<int:pk>', category_detail_admin_panel_view, name='category_detail_admin_panel'),
    path('category/edit/<int:pk>', category_edit_admin_panel_view, name='category_edit_admin_panel'),
    path('category/delete/<int:pk>', category_delete_admin_panel_view, name='category_delete_admin_panel'),
    path('category/manage/admin_panel/posts/', category_post_in_category_panel_admin_panel_view,
         name='category_posts_in_category_panel_admin_panel'),
    path('category/manage/admin_panel/posts/<int:pk>', category_post_in_category_panel_detail_admin_panel_view,
         name='category_post_in_category_panel_detail_admin_panel'),

    path('article/add_article/', post_add_view, name='post_add'),
    path('article/admin_panel/', post_manage_admin_panel_view, name='post_admin_panel'),
    path('article/detail/<int:pk>', post_detail_admin_panel_view, name='post_detail_admin_panel'),
    path('article/edit/<int:pk>', post_edit_admin_panel_view, name='post_edit_admin_panel'),
    path('article/delete/<int:pk>', post_delete_admin_panel_view, name='post_delete_admin_panel'),
    path('article/publication/', post_publication_admin_panel_view, name='post_publication_admin_panel'),

    path('comment/add_comment/', comment_add_view, name='comment_add'),
    path('comment/admin_panel/', comment_manage_admin_panel_view, name='comment_admin_panel'),
    path('comment/detail/<int:pk>', comment_detail_admin_panel_view, name='comment_detail_admin_panel'),
    path('comment/edit/<int:pk>', comment_edit_admin_panel_view, name='comment_edit_admin_panel'),
    path('comment/delete/<int:pk>', comment_delete_admin_panel_view, name='comment_delete_admin_panel'),
    path('comment/post/',  comment_in_post_admin_panel_view, name='comment_in_post_admin_panel'),
    path('comment/post/<int:pk>',  comment_in_post_detail_admin_panel_view, name='comment_in_post_detail_admin_panel'),
    path('comment/user/admin_panel/', comment_users_admin_panel_view, name='comment_users_admin_panel'),
    path('comment/user/<int:pk>', comment_users_detail_admin_panel_view, name='comment_users_detail_admin_panel'),

    path('meetups_news/', meetups_news_add_view, name='meetups_news_add'),
    path('meetups_news/admin_panel/', meetups_news_manage_admin_panel_view, name='meetups_news_admin_panel'),
    path('meetups_news/detail/<int:pk>', meetups_news_detail_admin_panel_view, name='meetups_news_detail_admin_panel'),
    path('meetups_news/edit/<int:pk>', meetups_news_edit_admin_panel_view, name='meetups_news_edit_admin_panel'),
    path('meetups_news/delete/<int:pk>', meetups_news_delete_admin_panel_view, name='meetups_news_delete_admin_panel'),
    path('meetups_news/user/admin_panel/', meetups_news_user_manage_admin_panel_view, name='meetups_news_user_admin_panel'),
    path('meetups_news/user/detail/<int:pk>', meetups_news_user_detail_admin_panel_view, name='meetups_news_user_detail_admin_panel'),
    path('meetups_news/user/edit/<int:pk>', meetups_news_user_edit_admin_panel_view , name='meetups_news_user_edit_admin_panel'),

    path('auction_opportunities/', auction_opportunities_add_view, name='auction_opportunities_add'),
    path('auction_opportunities/admin_panel/', auction_opportunities_admin_panel_view, name='auction_opportunities_admin_panel'),
    path('auction_opportunities/detail/<int:pk>', auction_opportunities_detail_admin_panel_view, name='auction_opportunities_detail_admin_panel'),
    path('auction_opportunities/edit/<int:pk>', auction_opportunities_edit_admin_panel_view, name='auction_opportunities_edit_admin_panel'),
    path('auction_opportunities/delete/<int:pk>', auction_opportunities_delete_admin_panel_view, name='auction_opportunities_delete_admin_panel'),
    path('auction_opportunities/user/admin_panel/', auction_opportunities_user_manage_admin_panel_view, name='auction_opportunities_user_manage_admin_panel'),
    path('auction_opportunities/user/detail/<int:pk>', auction_opportunities_user_detail_admin_panel_view, name='auction_opportunities_user_detail_admin_panel'),
    path('auction_opportunities/user/edit/<int:pk>', auction_opportunities_user_edit_admin_panel_view, name='auction_opportunities_user_edit_admin_panel'),

    path('company_news/', company_news_add_view, name='company_news_add'),
    path('company_news/admin_panel/', company_news_admin_panel_view, name='company_news_admin_panel'),
    path('company_news/detail/<int:pk>', company_news_detail_admin_panel_view, name='company_news_detail_admin_panel'),
    path('company_news/edit/<int:pk>', company_news_edit_admin_panel_view, name='company_news_edit_admin_panel'),
    path('company_news/delete/<int:pk>', company_news_delete_admin_panel_view, name='company_news_delete_admin_panel'),
    path('company_news/user/admin_panel/', company_news_user_manage_admin_panel_view, name='company_news_user_manage_admin_panel'),
    path('company_news/user/detail/<int:pk>', company_news_user_detail_admin_panel_view, name='company_news_user_detail_admin_panel'),
    path('company_news/user/edit/<int:pk>', company_news_user_edit_admin_panel_view, name='company_news_user_edit_admin_panel'),

    path('replay_news/', replay_news_add_view, name='replay_news_add'),
    path('replay_news/admin_panel/', replay_news_admin_panel_view, name='replay_news_admin_panel'),
    path('replay_news/detail/<int:pk>', replay_news_detail_admin_panel_view, name='replay_news_detail_admin_panel'),
    path('replay_news/edit/<int:pk>', replay_news_edit_admin_panel_view, name='repaly_news_edit_admin_panel'),
    path('replay_news/delete/<int:pk>', replay_news_delete_admin_panel_view, name='replay_news_delete_admin_panel'),
    path('replay_news/user/admin_panel', replay_news_user_manage_admin_panel_view, name='replay_news_user_manage_admin_panel'),
    path('replay_news/user/detail/<int:pk>', replay_news_user_detail_admin_panel_view, name='replay_news_user_detail_admin_panel'),
    path('replay_news/user/edit/<int:pk>', replay_news_user_edit_admin_panel_view, name='replay_news_user_edit_admin_panel'),

    path('development_news/', development_news_add_view, name='development_news_add'),
    path('development_news/admin_panel/', development_news_admin_panel_view, name='development_news_admin_panel'),
    path('development_news/detail/<int:pk>', development_news_detail_admin_panel_view, name='development_news_detail_admin_panel'),
    path('development_news/edit/<int:pk>', development_news_edit_admin_panel_view, name='development_news_edit_admin_panel'),
    path('development_news/delete/<int:pk>', development_news_delete_admin_panel_view, name='development_news_delete_admin_panel'),
    path('development_news/user/admin_panel', development_news_user_manage_admin_panel_view, name='development_news_user_manage_admin_panel'),
    path('development_news/user/detail/<int:pk>', development_news_user_detail_admin_panel_view, name='development_news_user_detail_admin_panel'),
    path('development_news/user/edit/<int:pk>', development_news_user_edit_admin_panel_view, name='development_news_user_edit_admin_panel'),

    path('send_emails/', views.send_emails_view, name='send_emails'),
    path('skipped_posts/admin_panel/', views.skipped_posts_admin_panel, name='skipped_posts_admin_panel'),
    path('skipped_posts/detail/<int:pk>', views.skipped_posts_detail_admin_panel, name='skipped_posts_detail_admin_panel'),
    path('skipped_posts/user/admin_panel/', views.skipped_posts_user_admin_panel, name='skipped_posts_user_admin_panel'),
    path('skipped_posts/user/edit/<int:pk>', views.skipped_posts_user_edit_admin_panel, name='skipped_posts_user_edit_admin_panel'),

    path('create_user/', views.create_user, name='create_user')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
