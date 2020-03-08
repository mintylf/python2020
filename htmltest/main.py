from flask import Flask, render_template
app = Flask(__name__) #플라스크 객체 생성

@app.route('/info')
def index():
    return 'Hello Flask'

@app.route('/')
def info():
    return render_template('index.html')


if __name__ == "__main__": #파일이 자기자신에게 호출당했을경우
    app.run(host="0.0.0.0", port='8890',debug=True  )#run 매서드 실행 0.0.0.0 --> 어디서든 접근가능 8890 --> cmd에서 도커설정할때 열어놓은 포트번호

