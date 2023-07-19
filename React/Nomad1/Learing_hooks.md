# hook
- functional programming을 지원한다.  
- 과거의 코드는 class의 형식으로 사용했으나, hook이 지원된 후 함수형으로 코딩함으로써 효율성을 증진시킬 수 있었다.  




### 1. useState
- class에선 `setState`와 같은 것으로 사용했어야 한다.  

```js
// App.js

import { useState } from "react";

function App() {
	const [item, setItem] = useState(1);
	const incrementItem = () => setItem((current) => current + 1); // 이게 훅임!
  const decrementItem = () => setItem((current) => current - 1);
	
	return (
    <div>
			<h1>Hello {item}</h1>
			<button onClick={incrementItem}>incrementItem</button>
			<button onClick={decrementItem}>decrementItem</button>
    </div>
  );
}

export default App;

```

### 2. useInput  
- 기존에 `input` 태그를 사용하려면 value, onChange를 일일히 넣어주어야 했는데 그에 대한 불편함을 해소시켜준다.  

```js
// App.js

import { useState } from "react";

const useInput = (initialValue) => {
	const [value, setValue] = useState(initialValue);
	const onChange = (event) => {
		setValue(event.target.value);
		console.log(event.target);
	};

	return { value, onChange };
}

function App() {
	const name = useInput("Mr.");

	return (
    <div>
			<h1>Hello</h1>
			<input placeholder="Name" {...name} /> // desctruct로 value={value}, onChange={onChange}
    </div>
  );
}

export default App;

```

- 유효성을 검증하는 `validator function`?

```js
// App.js

import { useState } from "react";

const useInput = (initialValue, validator) => {
  const [value, setValue] = useState(initialValue);
  const onChange = (event) => {
		const {
			target: { value }
		} = event; // 이 부분이 이해가 잘 안됨; => 함수 스코프 때문에 이렇게 할 수 있는 건가?

    let willUpdate = true;

    if (typeof validator === "function") {
      willUpdate = validator(value);
    }

    if (willUpdate) {
      setValue(value);
    }
  };

  return { value, onChange };
};

function App() {
  const maxLength = (value) => value.length < 10;
  const name = useInput("Mr.", maxLength);

  return (
    <div>
      <h1>Hello</h1>
      <input placeholder="Name" {...name} />
    </div>
  );
}

export default App;
```