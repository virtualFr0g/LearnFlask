from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/square', methods=['GET'])
def squarenumber():
    num=request.args.get('num')
    
    
if __name__=='__main__':
    app.run()