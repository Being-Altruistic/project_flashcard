from django.shortcuts import HttpResponse,render, get_object_or_404, redirect
# Create your views here.

from .models import deck, flashcard


def index(request):
    return render(request, 'remembo/index.html')

def detail(request, question_id):
    deck_row = get_object_or_404(deck, pk= question_id)
    return render(request, 'remembo/cardshome.html', {'question': deck_row})

def studypage(request):
    card = {}
    count =0;
    if request.method == "POST":
        id = request.POST.get('selecttostudy')
        deck_row = get_object_or_404(deck, pk=id)
        #context = {'deck_row' : deck_row}
        #for i in get_object_or_404(flashcard, deck_key_id=id):
        card =  flashcard.objects.filter(deck_key_id=count)

        #context = {'context_val': card}
        return HttpResponse(card)

        #return render(request,'remembo/studypage.html',card)

def home(request):
    questions = deck.objects.order_by()
    context = {'get_questions': questions}
    if request.method == "POST":
        if request.POST.get('getbookmark'):
            get_id = request.POST.get('getbookmark')
            deck_row = get_object_or_404(deck, pk = get_id)
            deck_row.deck_bookmark = "MARK"
            deck_row.save()
            return HttpResponse("Bookmark Added! You can View that into the VIEW BOOKMARK PAGE!")
        else:
            return render(request, 'remembo/home.html', context)
    return render(request, 'remembo/home.html', context)

def createcard(request):
    return render(request,'remembo/createcard.html')

def search(request):
    if request.method == "POST":
        value = request.POST.get('searchval')
    count=0
    questions = deck.objects.order_by()
    context = {'all_questions': questions, 'searchdata':value, 'count': count}
    return render(request, 'remembo/search.html', context)

def viewbookmarks(request):
    decks = deck.objects.order_by()
    context={'get_decks': decks}
    if request.method == "POST":
        if request.POST.get('delbookmark'):
            get_id = request.POST.get('delbookmark')
            if get_id != 'All':
                deck_row = get_object_or_404(deck, pk = get_id)
                deck_row.deck_bookmark = ""
                deck_row.save()
                return render(request, 'remembo/viewbookmarks.html', context)
            else:
                for i in decks:
                    if i.deck_bookmark == "MARK":
                        i.deck_bookmark = ""
                        i.save()
                return render(request, 'remembo/viewbookmarks.html', context)
        else:
            return render(request, 'remembo/viewbookmarks.html', context)
