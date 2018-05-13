from django.shortcuts import render
from .models import UserMessage


# Create your views here.
def get_form(request):
    #查询
    user_messages = UserMessage.objects.all()
    if user_messages:
        user_message = user_messages[0]
    #删除
    # user_messages.delete()
    # #存储
    # user_message = UserMessage()
    # user_message.name = 'lily'
    # user_message.message = 'hello'
    # user_message.email = '2345@qq.com'
    # user_message.address = '云南财经大学'
    # user_message.message_id = 2
    #
    # user_message.save()
    #
    # #获取表单数据
    # if request.method == 'POST':
    #     user_message.name = request.POST.get('name','')
    #     user_message.message = request.POST.get('message', '')
    #     user_message.email = request.POST.get('email', '')
    #     user_message.address = request.POST.get('address', '')
    #     user_message.message_id = 3
    #
    #     user_message.save()
    #显示数据

    return render(request,'message_form.html',{'user_message':user_message})
