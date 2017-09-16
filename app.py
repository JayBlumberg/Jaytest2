def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    response_body = 'Hello World app-1'
    yield response_body.encode()



if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever() tkinter import *
root = Tk()
v = IntVar()
Label(root,
      text="""Choose a
Toolbox option:""",
      justify = LEFT,
      padx = 20).pack()
def ShowChoice():
    print(v.get())
    x = v.get()
    print(x)
Radiobutton(root,
            text="Amazon",
            indicatoron = 0,
            width = 20,
            padx = 20,
            variable=v,
            command=ShowChoice,
            value=1).pack(anchor=W)


Radiobutton(root,
            text="Zappos",
            indicatoron = 0,
            width = 20,
            padx = 20,
            variable=v,
            command=ShowChoice,
            value=2).pack(anchor=W),



mainloop()

