from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start Tag: ", tag)
        for attr in attrs:
            print("attr     :", attr)

    def handle_endtag(self, tag):
        print("End Tag      : ", tag)

    def handle_data(self, data):
        print("Data     : ", data)

    def handle_comment(self, data):
        print("Comment      :", data)

    def handle_entitiyref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)


    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Numb ent     :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
        '<body><h1>Parse me!</h1></body></html>')

