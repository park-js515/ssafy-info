### alert, prompt, comfirm을 이용한 상호 작용
 
 > 브라우저는 사용자와 상호작용할 수 있는 세 가지 함수를 제공합니다.

<a href="https://ko.javascript.info/alert-prompt-confirm">link</a>

```js
// alert
alert("Hello");
```

```js
// prompt
let age = prompt('나이를 입력해주세요.', 100);

alert(`당신의 나이는 ${age}살 입니다.`); // 당신의 나이는 100살입니다.
```

```js
// confirm
let isBoss = confirm("당신이 주인인가요?");

alert( isBoss ); // 확인 버튼을 눌렀다면 true가 출력됩니다.
```