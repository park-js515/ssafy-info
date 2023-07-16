import { useState, useEffect } from "react";

function App() {
	const [loading, setLoading] = useState(true);
	const [movies, setMovies] = useState([]);
	const response = async () => {
		await fetch("https://yts.mx/api/v2/list_movies.json?minimum_rating=8.5&sort_by=year")		
	};
	const json = await response.json(); 

	setMovies(json.data.movies);
	setLoading(false);

  return (
    <div>
			{loading? <h1>Loading...</h1> : null}
    </div>
  );
}

export default App;
