from django.http import HttpResponse

# Главная страница
def index(request):
    html_content = '''
    <!DOCTYPE html>
    <html lang="ru">
      <head>
        <title>ACME</title>
      </head>
      <body>
        <h1>Catalog</h1>
      </body>
    </html>
    '''
    return HttpResponse(html_content) 