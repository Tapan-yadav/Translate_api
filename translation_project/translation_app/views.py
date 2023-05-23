# Third party rest_framework import
from rest_framework.decorators import api_view
from rest_framework.response import Response

#third party google API import
from googletrans import Translator

# importing the inbuild app 
from translation_app.models import Translation

@api_view(['GET'])
def translate_text(request):
    # getting the query_param from the client side
    text = request.GET.get('text')
    target_language = request.GET.get('target_language')
    source_language = request.GET.get('source_language', 'auto')

    if not text:
        return Response({'error': 'No text provided.'})

    try:
        # for storing data into database
        translation = Translation.objects.get(text=text, target_language=target_language, source_language=source_language)
        return Response({'translation': translation.translated_text})
    except Translation.DoesNotExist:
        try:
            # translating the source file to target file 
            translator = Translator(service_urls=['translate.google.com'])
            translated_text = translator.translate(text, src=source_language, dest=target_language).text
            Translation.objects.create(text=text, target_language=target_language, source_language=source_language, translated_text=translated_text)
            return Response({'translation': translated_text})
        except Exception as e:
            return Response({'error': str(e)})

