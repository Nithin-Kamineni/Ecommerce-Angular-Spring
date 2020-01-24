from flask import Flask,request

app = Flask(__name__)

@app.route('/api',methods=['GET'])

def index():
    Query = str(request.args['Query'])
    word=Query+" "
    lst = []
    st=""
    for let in word:
        if(let==" "):
            lst.append(st)
            st=""
        else:
            st = st + let
    print(lst)
    return Query

if __name__ == '__main__':
    app.run()