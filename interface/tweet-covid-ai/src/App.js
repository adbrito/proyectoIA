import React, { useState, useEffect } from "react";
import "./App.scss";

//Importing Components
import Tweets from "./components/tweets/Tweets";
import Form from "./components/form/Form";
import Face from "./components/face/Face";

function App() {
	// Walkthrough emotions on start (sparing the last one for better thumbnail)
	let emotions = [
		"tired",
		"happy",
		"astonished",
		"feared",
		"anguished",
		"angry",
		"ondrugs",
	];
	const [emotion, setEmotion] = useState(emotions[0]);

	let n = 1;

	useEffect(() => {
		const interval = setInterval(() => {
			setEmotion(emotions[n]);
			console.log(emotions[n]);
			n++;
			if (n === emotions.length) {
				setEmotion(emotions[0]);
				console.log(emotions[0]);
				console.log("Clear Interval Emotions");
				clearInterval(interval);
			}
		}, 500);

		return () => clearInterval(interval);
	}, []);

	return (
		<div className="App">
			<header>
				<h1>Tweet Covid AI</h1>
			</header>
			<div className="main-secction">
				<div className="second-section">
					<Form setEmotion={setEmotion} />
					<Tweets />
				</div>
				<Face emotion={emotion} />
			</div>
		</div>
	);
}

export default App;
