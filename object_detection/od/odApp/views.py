from django.shortcuts import render

from gtts import gTTS

# Create your views here.


def index(request):
    word = ''

    if 'start' in request.GET:
        #from det import direct
        #dir=direct
        from .voice import main
        word, dire = main()
        
        print("===========================")
        print(word)
        print("===========================")
        print(dire)
        print("===========================")
        myText = f"there is a single {word} with {dire} direction"
        language = 'en'
        myobj = gTTS(text=myText, lang=language, slow=False)
        path = "F:\\PROJECT\\od\\static\\media\\word.mp3"
        myobj.save(path)
        return render(request, "index.html", {"path": 'word.mp3'})

    return render(request, "index.html")


def map(request):

    return render(request, "map.html")
