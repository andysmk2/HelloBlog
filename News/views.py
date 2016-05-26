# -*- coding: UTF-8 -*-

from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'NBA'
    h1 = '【教學】吃蘿蔔！球場意外第一名　傷後處理，你做對了嗎？'
    content = '勇士打雷霆'
    text1 = '據《克里夫蘭老實人報》報導，自從進入NBA以來，LeBron James已經取得了巨大的成就，而且在很長一段時間內都被認為是聯盟裡最好的球員，但是前騎士隊總經理，在2003年NBA選秀大會上選擇James的Jim Paxson卻依然認為James被有所低估。'
    text2 = '根據美國媒體消息 本賽季的NBA已經進入到尾聲，在西區決賽中，此前不被人們看好的奧克拉荷馬雷霆竟然以總比分3-1領先奪冠大熱門金州勇士隊，除了Durant之外，雷霆陣中另一位大將Westbrook的表現可謂是令人眼前一亮，不過今天美國媒體卻曝光了一件有關韋少陳年舊事。'
    text3 = '今天小編給大家帶來的是快速處理手指戳傷的方法！一般來說，最容易戳傷手指的是球類運動，當我們手指與球垂直撞擊時，就有很大的可能發生手指戳傷。如何判斷自己是否被戳傷了呢？手指戳傷主要是在被戳後存在五個表現：'
    return render(request, 'index.html', locals())

