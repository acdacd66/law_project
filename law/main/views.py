from django.shortcuts import render
import requests, pprint
from bs4 import BeautifulSoup as BS

def home(request):
    count=0
    count1=0
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
        q_list=[]
        
        for q in question_list:
            question= q.text
            count+=1
            q_l.append(question)
            
        for a in answer_list:
            answer= a.a.get('href')
            answer='http://easylaw.go.kr/CSP/'+answer
            tmp1=requests.get(answer)
            html = BS(tmp1.text, 'html.parser')
            real=html.select('ul.question > li.qa > div.q > div.ans')
           
            for r in real:
                q_l[count1]=q_l[count1]+r.text
            count1+=1
        # print(*ul_list, sep='\n')
        
    
   
    # Create your views here.
    return render(request, 'home.html',{'q_l':q_l})

