import React from "react";
import "./Tweets.scss";

const Tweet = ({ content }) => {
	const handleCopy = async (e) => {
		if ("clipboard" in navigator) {
			return await navigator.clipboard.writeText(content);
		} else {
			return console.log(`Dont copy ${content}`);
		}
	};

	return (
		<div className="tweet">
			<p className="content">
				{content.split(" ").map((str) => {
					if (
						str.startsWith("#") ||
						str.startsWith("@") ||
						str.startsWith("http")
					) {
						return (
							<a href={`/${str}`} className="">
								{str}{" "}
							</a>
						);
					}
					return str + " ";
				})}
			</p>
			<button onClick={handleCopy}>Copy</button>
		</div>
	);
};

export default Tweet;
