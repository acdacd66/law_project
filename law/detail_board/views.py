from django.shortcuts import render,redirect
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

def traffic_board(request):
   
    if  len(Traffic_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=90&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(9):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Traffic_Board()
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
                
                
                F_board=Traffic_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Traffic_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def government_board(request):
   
    if  len(Government_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=95&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(4):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Government_Board()
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
                
                
                F_board=Government_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Government_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def army_board(request):
   
    if  len(Army_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=81&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(6):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Army_Board()
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
                
                
                F_board=Army_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Army_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def labor_board(request):
   
    if  len(Labor_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=82&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(17):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Labor_Board()
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
                
                
                F_board=Labor_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Labor_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def financial_board(request):
   
    if  len(Financial_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=92&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(11):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Financial_Board()
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
                
                
                F_board=Financial_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Financial_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def trade_board(request):
   
    if  len(Trade_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=100&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(10):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Trade_Board()
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
                
                
                F_board=Trade_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Trade_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def leisure_board(request):
   
    if  len(Leisure_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=87&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(6):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Leisure_Board()
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
                
                
                F_board=Leisure_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Leisure_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})


def lawsuit_board(request):
   
    if  len(Lawsuit_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=85&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(13):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Lawsuit_Board()
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
                
                
                F_board=Lawsuit_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Lawsuit_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def welfare_board(request):
   
    if  len(Welfare_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=97&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(18):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Welfare_Board()
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
                
                
                F_board=Welfare_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Welfare_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def estate_board(request):
   
    if  len(Estate_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=84&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(21):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Estate_Board()
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
                
                
                F_board=Estate_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Estate_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def business_board(request):
   
    if  len(Business_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=83&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(9):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Business_Board()
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
                
                
                F_board=Business_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Business_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def crime_board(request):
   
    if  len(Crime_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=86&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
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
              
                F_board=Crime_Board()
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
                
                
                F_board=Crime_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Crime_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def client_board(request):
   
    if  len(Client_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=88&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(8):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Client_Board()
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
                
                
                F_board=Client_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Client_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def children_board(request):
   
    if  len(Children_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=89&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(18):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Children_Board()
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
                
                
                F_board=Children_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Children_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def information_board(request):
   
    if  len(Information_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=94&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(5):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Information_Board()
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
                
                
                F_board=Information_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Information_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})

def startup_board(request):
   
    if  len(Startup_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=91&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(19):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Startup_Board()
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
                
                
                F_board=Startup_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Startup_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})


def eco_board(request):
   
    if  len(Eco_Board.objects.all())== 0: 
        
        
        url='http://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?pagingType=default&onhunqnaAstSeq=96&sortType=DEFAULT&REQUEST_DATA_SINGLE_MODE=true&targetRow='
        val=1
        q_l=[]

        for i in range(6):
            tmp=i*10
            tmp=str(tmp)
            req = requests.get(url+tmp)

            html = BS(req.text, 'html.parser')

            
            question_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ttl > a')
            answer_list=html.select('div.vote_list > ul.question > li.qa > div.q > div.ans')
            id_list=[]
            
            for q in question_list:
                question= q.text
              
                F_board=Eco_Board()
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
                
                
                F_board=Eco_Board.objects.get(id=id_list[i])
                F_board.answer=h
                F_board.save()
    F_boards=Eco_Board.objects.all()
   
        
    return render(request,'detailBoard_list.html',{'F_boards':F_boards})