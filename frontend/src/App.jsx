import { useEffect, useState } from "react";

function App() {
  let apiUrl = "http://127.0.0.1:8000/";
  let [movies, setMovies] = useState([]);
  let [loading, setLoading] = useState(false);
  let [query, setQuery] = useState("");
  let [filtered, setFiltered] = useState([]);
  let [selected, setSelected] = useState("");
  let [recs, setRecs] = useState([]);

  const handleSearch = (e) => {
    const q = e.target.value;
    setQuery(q);
    if (q.length > 1) {
      const results = movies.filter((movie) =>
        movie.title.toLowerCase().includes(q.toLowerCase())
      );
      setFiltered(results);
    } else {
      setFiltered([]);
    }
  };

  const handleSelect = (movie) => {
    setSelected(movie.title);
    setQuery(movie.title);
    setFiltered([]);
    getRecs(movie.title);
  };

  const getMoviesList = async () => {
    setLoading(true);
    const response = await fetch(apiUrl + "get_all_movies");
    const data = await response.json();
    if (data.success) {
      setMovies(data.movies);
    } else {
      console.error("Couldn’t fetch movies");
      console.log(data);
    }
    setLoading(false);
  };

  const getRecs = async (movieTitle) => {
    setLoading(true);
    const response = await fetch(apiUrl + "recommend/" + movieTitle);
    const data = await response.json();
    console.log(data);
    if (data.success) {
      setRecs(data.recommended_movies);
    } else {
      console.error("Couldn't get recommendations: " + data.error);
    }
    setLoading(false);
  };

  useEffect(() => {
    getMoviesList();
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center p-8">
      <div className="w-full max-w-[75%]">
        <h1 className="text-4xl font-extrabold text-center mb-8">
          🎬 Movie Recommender
        </h1>

        {/* input */}
        <form
          onSubmit={(e) => {
            e.preventDefault();
            if (query) getRecs(query);
          }}
          className="mb-6"
        >
          <input
            type="text"
            value={query}
            onChange={handleSearch}
            placeholder="Search for a movie..."
            className="w-full p-3 rounded-lg bg-gray-800 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-yellow-400"
          />
        </form>

        {/* loader */}
        {loading && (
          <div className="w-8 h-8 border-b-3 border-blue-500 rounded-full animate-spin"></div>
        )}

        {/* filtered movies */}
        {filtered.length > 0 && (
          <ul className="bg-gray-800 text-white w-full mt-1 rounded shadow max-h-80 overflow-y-auto">
            {filtered.map((movie) => (
              <li
                key={movie.id}
                onClick={() => handleSelect(movie)}
                className="px-4 py-2 hover:bg-gray-700 cursor-pointer"
              >
                {movie.title}
              </li>
            ))}
          </ul>
        )}

        {/* recommendation */}
        {!loading && selected && (
          <div className="bg-gray-800 p-6 rounded-lg">
            <h2 className="text-xl font-semibold mb-4">
              Recommended Movies for{" "}
              <span className="text-yellow-400">{selected}</span>
            </h2>
            {recs.length > 0 && (
              <div className="flex flex-wrap gap-6">
                {recs.map((r) => (
                  <a
                    key={r.title}
                    href={r.homepage}
                    target="_blank"
                    className="bg-gray-700 rounded-lg overflow-hidden shadow hover:scale-105 transition-transform duration-100 cursor-pointer"
                  >
                    <img
                      src={r.poster_path}
                      alt={r.title}
                      className="w-full h-70 object-cover"
                    />
                    <p className="p-2 text-center text-sm font-medium">
                      {r.title}
                    </p>
                  </a>
                ))}
              </div>
            )}
            {!loading && recs.length === 0 && (
              <p className="text-gray-400">No recommendations available.</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
