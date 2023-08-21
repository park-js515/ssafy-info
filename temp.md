> Django의 작동 순서
1. 해당 url로 요청을 보낸다.
2. 해당 url에 대응되는 views.py의 메소드가 실행된다.
3. 해당 views.py의 메소드에서 해당 페이지에 대응되는 템플릿을 렌더링한다.  

> Django는 기본적인 구조  
1. Model: 데이터 저장 형태 정의  
2. Template: 유저에게 보여지는 화면  
3. View: 데이터를 처리해 보여지는 화면  
4. URLconf: 가공한 데이터를 유저가 보는 화면으로 넘겨준다.  

```Bash
python -m venv venv
source venv/Script/activate
pip install -r requirements.txt
python manage.py runserver
```