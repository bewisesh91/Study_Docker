from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

all_movie_star = [
    {
        'name': '공유',
        'img_url': 'https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2F76%2F201706081735556361.jpg&type=u77_96&quality=95',
        'recent': '서복',
        'url': 'https://movie.naver.com/movie/bi/pi/basic.nhn?code=8090',
        'like': 0
    },
    {
        'name': '김고은',
        'img_url': 'https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2Fportrait%2F201801%2F20180118105906522.jpg&type=u77_96&quality=95',
        'recent': '서복',
        'url': 'https://movie.naver.com/movie/bi/pi/basic.nhn?code=297957',
        'like': 0
    }
]


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_stars():
    all_movie_star.sort(key=lambda x: x["like"], reverse=True)
    return jsonify({'movie_stars': all_movie_star})


@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']

    target_star = [actor for actor in all_movie_star if actor["name"] == name_receive][0]
    target_star['like'] += 1

    return jsonify({'msg': '좋아요 완료!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']
    for actor in all_movie_star:
        if actor["name"] == name_receive:
            del actor
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)