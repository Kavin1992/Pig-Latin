from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def translate(request):
    inputtext=request.GET['inputtext'].lower()
    vowel=['a','e','i','o','u']
    translate=''
    for word in inputtext.split():
        if word[0] in vowel:
            translate+=' ' + word+'way'
        else:
            cnt=0
            for i in word:
                cnt+=1
                if i in vowel:
                    translate+=' ' + word[word.index(i):] + word[:word.index(i)] + 'ay'
                    break
                elif cnt==len(word):
                    translate+=' ' + word
                    break
    return render(request,'translate.html',{'orig':inputtext,'trans':translate})
  #  return HttpResponse("Hello the string is " + request.GET['inputtext'] + " Translated String is "+ translate.strip())

def about(request):
    return render(request,'about.html')