from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),

    # path('notice/', views.get_notice_list, name='get_notice_list'),
    # path('notice/<int:notice_id>', views.notice_detail, name='notice_detail'),
    path('notice/', views.notice_index, name='notice_index'),
    path('notice/<int:notice_id>/', views.notice_detail, name='notice_detail'),

    # path('qna/', views.get_question_list, name='get_question_list'),
    # path('qna/<int:question_id>', views.question_detail, name='question_detail'),
    path('qna/', views.qna_index, name='qna_index'),
    path('qna/<int:question_id>/', views.qna_detail, name='qna_detail'),
    path('qna/question/create/', views.qna_question_create, name='qna_question_create'),
    path('qna/question/modify/<int:question_id>/', views.qna_question_modify, name='qna_question_modify'),
    path('qna/question/delete/<int:question_id>/', views.qna_question_delete, name='qna_question_delete'),
    path('qna/answer/delete/<int:answer_id>/', views.qna_answer_delete, name='qna_answer_delete'),
    path('qna/answer/create/<int:question_id>/', views.qna_answer_create, name='qna_answer_create'),

    path('review/', views.get_review_list, name='get_review_list'),
    path('review/<int:review_id>', views.review_detail, name='review_detail'),

    path('product/', views.get_product_list, name='get_product_list'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),

    path('basket/', views.get_shopbasket_list, name='get_shopbasket_list'),
    path('basket/delete/', views.basket_delete, name='basket_delete'),
    path('basket/update/', views.basket_update, name='basket_update'),
    path('payment/result/', views.payment_result, name='payment_result'),
    path('mypage/', views.get_mypage, name='mypage'),
    path('ordered/', views.get_my_order, name='get_my_order'),
    path('myinfo/', views.get_my_info, name='get_my_info'),

]