import React, { useState } from "react";
import axios from "axios";
import "./Form.scss";

const Form = ({ setEmotion }) => {
	let url = "https://tweet-covid-api.herokuapp.com/";
	//let url = "http://127.0.0.1:8000/";

	const [inputText, setInputText] = useState("");
	const [predictionLabel, setPredictionLabel] = useState("");

	const inputTextHandler = (e) => {
		//console.log(e.target.value);
		setInputText(e.target.value);
	};

	const submitTweetHandler = (e) => {
		e.preventDefault();

		if (inputText !== "") {
			let tweet = inputText;
			postPredict(tweet);
			setEmotion("tired");
			//setInputText("");
			setPredictionLabel("");
		}
		else{
			setEmotion("tired");
			setPredictionLabel("");
		}
	};

	const postPredict = async (tweet) => {
		try {
			let body = { content: tweet };
			const options = {
				headers: {
					"Content-Type": "application/json",
				},
			};

			const response = await axios.post(url, body, options);

			console.log(response);

			const data = await response.data;
			// enter you logic when the fetch is successful
			console.log(data);

			if (data.label === "POSITIVE") {
				setEmotion("happy");
				setPredictionLabel("POSITIVE");
			} else if (data.label === "NEGATIVE") {
				setEmotion("angry");
				setPredictionLabel("NEGATIVE");
			} else if (data.label === "NEUTRAL") {
				setEmotion("anguished");
				setPredictionLabel("NEUTRAL");
			} else {
				setEmotion("tired");
				setPredictionLabel("");
			}
		} catch (error) {
			// enter your logic for when there is an error (ex. error toast)
			setEmotion("tired");
			setPredictionLabel("");
			console.log(error);
		}
	};

	return (
		<form>
			<textarea
				value={inputText}
				onChange={inputTextHandler}
				type="text"
				className="tweet-input"
				placeholder="Write your tweet to predict here..."
				rows="6"
				cols="40"
			/>
			{predictionLabel !== "" ? (
				<p className="label">{predictionLabel}</p>
			) : null}
			<button
				onClick={submitTweetHandler}
				className="tweet-button"
				type="submit"
			>
				Send
			</button>
		</form>
	);
};

export default Form;
