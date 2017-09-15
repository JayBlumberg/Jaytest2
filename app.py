    import datetime
    today = datetime.date.today()

def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    

    
    text = 'hello world app.py - ' + today
    response_body = text
    yield response_body.encode()



if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
