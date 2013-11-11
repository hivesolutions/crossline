import appier

class CrosslineApp(appier.App):

    def __init__(self):
        appier.App.__init__(self, name = "crossline")
        self.count = 0

    @appier.route("/", "GET")
    @appier.route("/counter", "GET")
    def counter(self):
        return dict(
            count = self.count
        )

    @appier.route("/cross", ("GET", "POST"))
    def cross(self, data = None):
        self.count += 1
        return "OK"

app = CrosslineApp()
app.serve(host = "0.0.0.0")
