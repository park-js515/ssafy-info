from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def text_comparison(original, recorded):
    # 두 텍스트 파일을 불러와서 텍스트 데이터로 변환하는 함수
    def load_text(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    # 두 텍스트 파일의 코사인 유사도를 비교하는 함수
    def compare_cosine_similarity(text1, text2):
        vectorizer = CountVectorizer().fit_transform([text1, text2])
        vectors = vectorizer.toarray()
        similarity = cosine_similarity(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))
        return similarity[0][0]

    # 두 텍스트 파일을 불러옴
    file_path1 = f"{original}.txt"
    file_path2 = f"{recorded}.txt"
    text1 = load_text(file_path1)
    text2 = load_text(file_path2)

    # 코사인 유사도 계산
    similarity = compare_cosine_similarity(text1, text2)
    return similarity