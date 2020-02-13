from flask import Flask, render_template, request, logging, Response, redirect, flash

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return """
        下に整数を入力してください。奇数か偶数か判定します
        <form action="/" method="POST">
        <input name="num"></input>
        </form>"""
    else:
        try:
            return """
            {}は{}です！
            <form action="/" method="POST">
            <input name="num"></input>
            </form>""".format(str(request.form["num"]), ["偶数", "奇数"][int(request.form["num"]) % 2])
        except:
            return """
                    有効な数字ではありません！入力しなおしてください。
                    <form action="/" method="POST">
                    <input name="num"></input>
                    </form>"""

# app.route部分を変えれば、その処理についての記述が出来る
# actionをそこへ向ければ、別処理へリクエスト送信が行える。
# リクエスト送信後、受信した内容をhtmlに投げれる。
# このあたりがすっごいわかりやすいかも。
# https://note.com/daikawai/n/n233ef9662323
# このサイト、お金になりそうやねんけど情報発信めんどうで・・・


if __name__ == '__main__':
    app.run(debug=True)
