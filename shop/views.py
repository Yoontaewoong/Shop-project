import datetime
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import ShopBasket, Notice, Question, Product, Review, MyPage, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def index(request):

    item_list = ShopBasket.objects.filter(s_ordered=True).order_by('-s_amount')[:10]
    new_list = Product.objects.order_by('-p_id')[:6]
    context = {
        "item": item_list,
        "new": new_list
    }
    return render(request, 'shop/index.html', context)


# def get_notice_list(request):
#
#     page = request.GET.get('page', '1')
#
#     notice_list = Notice.objects.order_by('-n_date')
#
#     paginator = Paginator(notice_list, 20)
#     page_obj = paginator.get_page(page)
#
#     context = {
#         'notice_list': page_obj
#     }
#
#     return render(request, 'shop/notice_list.html', context)
#
#
# def notice_detail(request, notice_id):
#     notice = get_object_or_404(Notice, pk=notice_id)
#     context = {
#         'notice': notice
#     }
#     return render(request, 'shop/notice_detail.html', context)
#
#
# def get_question_list(request):
#
#     page = request.GET.get('page', '1')
#
#     question_list = Question.objects.order_by('-q_date')
#
#     paginator = Paginator(question_list, 20)
#     page_obj = paginator.get_page(page)
#
#     context = {
#         'question_list': page_obj
#     }
#
#     return render(request, 'shop/question_list.html', context)
#
#
# def question_detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question
#     }
#     return render(request, 'shop/question_detail.html', context)
#
#
def get_review_list(request):
    page = request.GET.get('page', '1')
    review_list = Review.objects.order_by('-r_date')

    paginator = Paginator(review_list, 20)
    page_obj = paginator.get_page(page)

    context = {
        'review_list': page_obj
    }

    return render(request, 'shop/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {
        'review': review
    }
    return render(request, 'shop/review_detail.html', context)


def get_product_list(request):

    page = request.GET.get('page', '1')

    product_list = Product.objects.order_by('-p_id')

    paginator = Paginator(product_list, 18)
    page_obj = paginator.get_page(page)

    context = {
        'product_list': page_obj
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, product_id):
    if request.method == 'POST':
        user_id = request.user.id
        amount = request.POST.get('amount')
        if amount == '':
            ShopBasket.objects.create(user_id=user_id, product_id=product_id)
        else:
            ShopBasket.objects.create(user_id=user_id, product_id=product_id, s_amount=amount)

        return redirect('/basket/')

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)


def get_shopbasket_list(request):

    if request.method == 'POST':
        get_list = request.POST.getlist('basket_check[]')
        if get_list:
            buy_list = ShopBasket.objects.filter(id__in=get_list)

            context = {
                'buy_list': buy_list
            }
            return render(request, 'shop/payment_process.html', context)
        else:
            messages.info(request, '구매하실 상품을 체크해 주세요')
            return HttpResponseRedirect('/basket/')
    else:
        user_id = request.user.id

        if user_id:
            basket_list = ShopBasket.objects.filter(user_id=user_id)

            context = {
                'basket_list': basket_list
            }
            return render(request, 'shop/shopbasket_list.html', context)
        else:
            return render(request, 'shop/shopbasket_list.html')


def payment_result(request):
    if request.method == 'POST':
        get_list = request.POST.getlist('result_data[]')
        print(get_list)
        for get in get_list:
            ShopBasket.objects.filter(id=get).update(s_ordered=True)

        payment_list = ShopBasket.objects.filter(id__in=get_list)
        print(payment_list)
        context = {
            'payment_list': payment_list
        }
        return render(request, 'shop/payment_result.html', context)

    else:
        pass


def get_mypage(request):
    user_id = request.user.id

    if user_id:
        mypage_data = MyPage.objects.filter(user_id=user_id)

        context = {
            'data': mypage_data
        }
        return render(request, 'shop/mypage.html', context)


def get_my_order(request):
    user_id = request.user.id

    if user_id:
        basket_list = ShopBasket.objects.filter(user_id=user_id)

        context = {
            'basket_list': basket_list
        }
        return render(request, 'shop/order_list.html', context)


def get_my_info(request):
    user_id = request.user.id

    user_info = User.objects.get(id=user_id)

    if user_info.is_superuser:
        return redirect('/admin/')

    context = {
        'user_info': user_info,
        'last_login': user_info.last_login.strftime('%y-%m-%d %a %H:%M:%S'),
        'date_joined': user_info.date_joined.strftime('%y-%m-%d %a %H:%M:%S')
    }

    return render(request, 'shop/mypage_detail.html', context)


def basket_delete(request):
    if request.method == 'POST':
        delete_list = request.POST.getlist('data[]')
        for data in delete_list:
            ShopBasket.objects.filter(id=data).delete()

        return redirect('/')


def basket_update(request):
    if request.method == 'POST':
        update_id = request.POST.get('id')
        update_data = request.POST.get('data')
        print(update_data)
        ShopBasket.objects.filter(id=update_id).update(s_amount=update_data)
        return redirect('/')


def qna_index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    question_list = Question.objects.order_by('-q_date')
    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'shop/qna_list.html', context)


def qna_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'shop/qna_detail.html', context)


def qna_question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.q_author = request.user
            # question.q_date = timezone.now()
            question.save()
            return redirect('shop:qna_index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'shop/qna_form.html', context)


def qna_question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = datetime.datetime.now()  # 수정일시 저장
            question.save()
            return redirect('shop:qna_detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'shop/qna_form.html', context)


def qna_question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('shop:qna_index')


def qna_answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('shop:qna_detail', question_id=answer.question.id)


def qna_answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.q_author = request.user
            # answer.q_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('shop:qna_detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'shop/qna_detail.html', context)


def notice_index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    notice_list = Notice.objects.order_by('-n_date')
    # 페이징처리
    paginator = Paginator(notice_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'notice_list': page_obj}
    return render(request, 'shop/notice_list.html.bak', context)


def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    context = {'notice': notice}
    return render(request, 'shop/notice_detail.html', context)

