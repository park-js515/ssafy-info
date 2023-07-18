import {
	BrowserRouter as Router,
	Routes, // Switch -> Routes
	Route,
	// Link
} from "react-router-dom";

import Home from "./routes/Home.js"
import Detail from "./routes/Detail";

function App() {

  return (
		<Router>
			<Routes>
				<Route path="/hello" element={<h1>Hello!</h1>}></Route>
				<Route path="/movie/:id" element={<Detail/>}></Route>
				<Route path="/" element={<Home />}></Route>
			</Routes>
		</Router>
  );
}

export default App;
