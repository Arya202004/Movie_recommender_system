from flask import Flask, render_template,request
import pickle
import numpy as np

popular = pickle.load(open('popular.pkl','rb'))
pivot = pickle.load(open('pivot.pkl','rb'))
data_with_title = pickle.load(open('data_with_title.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',
                           movie_name = list(popular['title'].values),
                           num_rating = list(popular['num_ratings'].values),
                           avg_rating = list(popular['avg_rating'].values),
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_movies',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pivot.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key = lambda x:x[1], reverse = True)[1:6]
    data = []
    for i in similar_items:
      item = []
      temp_df = data_with_title[data_with_title['title'] == pivot.index[i[0]]]
      item.extend(list(temp_df.drop_duplicates('title')['title'].values))
      data.append(item)

      print(data)

    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
