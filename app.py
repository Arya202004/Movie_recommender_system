from flask import Flask, render_template,request
import pickle
import numpy as np

popular = pickle.load(open('pkl_files\popular.pkl','rb'))
pivot = pickle.load(open('pkl_files\pivot.pkl','rb'))
data_with_title = pickle.load(open('pkl_files\data_with_title.pkl','rb'))
similarity_scores = pickle.load(open('pkl_files\similarity_scores.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def index():
    try:
        return render_template('index.html',
                               movie_name=list(popular['title'].values),
                               num_rating=list(popular['num_ratings'].values),
                               avg_rating=list(popular['avg_rating'].values))
    except Exception as e:
        return f"An error occurred while loading the index page: {e}"


@app.route('/recommend')
def recommend_ui():
    try:
        return render_template('recommend.html')
    except Exception as e:
        return f"An error occurred while loading the recommend page: {e}"

@app.route('/recommend_movies',methods=['post'])
def recommend():
    try:
        user_input = request.form.get('user_input')
        indices = np.where(pivot.index == user_input)[0]

        if len(indices) == 0:
            # Handle case where user_input is not found
            return render_template('index.html',
                                   movie_name=list(popular['title'].values),
                                   num_rating=list(popular['num_ratings'].values),
                                   avg_rating=list(popular['avg_rating'].values),
                                   message=f"Movie '{user_input}' not found. Please try again.")
        
        index = indices[0]

        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
        data = []
        for i in similar_items:
            item = []
            temp_df = data_with_title[data_with_title['title'] == pivot.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('title')['title'].values))
            data.append(item)

        return render_template('recommend.html', data=data)
    
    except Exception as e:
        return f"An error occurred while processing the recommendation: {e}"

if __name__ == '__main__':
    app.run(debug=True)
