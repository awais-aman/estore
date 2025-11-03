from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        request_url=request.META['PATH_INFO']
        print('Customerinsession: ',request.session.get('customer'))
        if not request.session.get('customer'):
           return redirect('http://127.0.0.1:8000/login/')

        response= get_response(request)
        return response
    return middleware