from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Word
from .forms import AddWordForm
from django.utils.translation import gettext_lazy as _

def translate_word(word, translation_type):
    try:
        if translation_type == 'uz_to_en':
            translated_word = Word.objects.get(uzb_word__iexact=word).eng_word
        elif translation_type == 'en_to_uz':
            translated_word = Word.objects.get(eng_word__iexact=word).uzb_word
        else:
            translated_word = 'Tarjima topilmadi'
    except Word.DoesNotExist:
        translated_word = 'Tarjima topilmadi'
    return translated_word



def translate(request):
    counts=Word.objects.count()
    if request.method == 'POST':
        input_word = request.POST.get('input_word', '')
        translation_type = request.POST.get('translation_type', '')
        translation = translate_word(input_word, translation_type)
        return render(request, 'home.html', {'translation': translation,'counts':counts })
    return render(request, 'home.html')





def listword(request):
    words=Word.objects.all()
    context={
        'words':words
    }
    return render(request,'listwords.html',context)






def addwords(request):
    form = AddWordForm()
    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("So'z muvaffaqiyatli qo'shildi"), extra_tags='success')
            return redirect('addd')
    return render(request, 'wordadd.html', {'form': form})


