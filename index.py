import web
render = web.template.render('templates/')

urls = (
    '/(.*)', 'home'
)

class home:
    def GET(self, results):
            return render.index(results)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
