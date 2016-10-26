import web
from core import ldds

urls = (
"/","Index"
)


render = web.template.render("templates")


class Index(object):
    def GET(self):
        content = "Test"
        return render.index(content = content)


    def POST(self):
        inputs = web.input()
        user_txt = inputs.user_txt
        Parser = ldds.NLParse(text = user_txt)        
               
 
        return render.index(content = Parser.returnSolidity(inputs.title))



app = web.application(urls,globals())

if __name__ == "__main__":
    app.run()
