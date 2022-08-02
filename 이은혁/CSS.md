# CSS

### CSS(Cascading Style Sheets)

- HTML에 스타일을 지정하기 위한 언어
- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미

### CSS 문법

```css
h1 {
	color: blue;
	font-size: 15px;
}
```

- 선택자(Selector)
    - 요소 선택자 : HTML 태그를 직접 선택
    - 클래스(class) 선택자 : 마침표(.)로 시작하며, 해당 클래스가 적용된 항목을 선택
    - 아이디(id) 선택자 : #문자로 시작하며, 해당 아이디가 적용된 항목을 선택(단일 id 사용 권장)
- 선언(Declaration)
- 속성(Property) : 어떤 스타일 기능을 변경할지 결정
- 값(Value) : 어떻게 스타일 기능을 변경할지 결정

### CSS 정의 방법

- 인라인(inline)
- 내부 참조(embedding) - <style>
- 외부 참조(link file) - <head>내 <link>를 통해 CSS 파일 불러오기
    
    ```html
    <html>
    		<head>
    				<title>Page</title>
    				<link rel="stylesheet" href="style.css">
    		</head>
    		<body>
    				<h1>Hello World</h1>
    		</body>
    </html>
    ```
    
    ```css
    h1 {
    		color: blue;
    		font-size: 20px;
    }
    ```
    

### CSS 적용 우선순위(Cascading Order)

1. 중요도