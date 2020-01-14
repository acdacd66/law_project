from django.shortcuts import render
from .models import *
import requests, pprint
from bs4 import BeautifulSoup as BS
# Create your views here.

def family_board(request):
   
    if  len(Family_Board.objects.all())== 0: 
        
        
        url='http://easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?onhunqnaAstSeq=25&pagingType=default&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(14):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
                
                F_board=Family_Board()
                F_board.question=question
                F_board.save()
                id_list.append(F_board.id)

                
                
            for i in range(len(answer_list)):
                answer= answer_list[i].a.get('href')
                answer='http://easylaw.go.kr/CSP/'+answer
                tmp1=requests.get(answer)
                html = BS(tmp1.text, 'html.parser')
                real=html.select('ul.question > li.qa > div.q > div.ans')
                h=''
                for r in real:
                    h=r.text
                
                
                F_board=Family_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Family_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})
    