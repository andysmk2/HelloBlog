from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Good Night'
    h1 = 'HAHAHA'
    content = 'DEMO'
    text1 = '據《克里夫蘭老實人報》報導，自從進入NBA以來，LeBron James已經取得了巨大的成就，而且在很長一段時間內都被認為是聯盟裡最好的球員，但是前騎士隊總經理，在2003年NBA選秀大會上選擇James的Jim Paxson卻依然認為James被有所低估。'
    return render(request, 'index.html', locals())

