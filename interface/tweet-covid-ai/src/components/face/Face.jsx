import React from "react";
import "./Face.scss";

//<!-- Author: Ali Soueidan-->
//<!-- Author URI: https//: www.alisoueidan.com-->

const Face = ({emotion}) => {

	return (
		<div id="face">
			<div className="face-container">
				<ul className={emotion} id="head">
					<li className="slice">
						<div className="hair"></div>
						<div className="folds" id="fold-1"></div>
						<div className="folds" id="fold-2"></div>
					</li>
					<li className="slice">
						<div className="ears" id="ear-l"></div>
						<div className="ears" id="ear-r"></div>
						<div className="eyes" id="eye-l">
							<div className="eyelid"></div>
						</div>
						<div className="eyes" id="eye-r">
							<div className="eyelid"></div>
						</div>
					</li>
					<li className="slice">
						<div className="nose">
							<div className="hole"></div>
							<div className="hole"></div>
						</div>
					</li>
					<li className="slice">
						<div class="mouth">
							<div className="teeth top">
								<div className="tooth"></div>
								<div className="tooth"></div>
								<div className="tooth"></div>
								<div className="tooth"></div>
								<div className="tooth"></div>
							</div>
							<div className="teeth bottom">
								<div className="tooth"></div>
								<div className="tooth"></div>
								<div className="tooth"></div>
								<div className="tooth"></div>
								<div className="tooth"></div>
							</div>
						</div>
					</li>
				</ul>
				<div className="corpus">
					<div className="belly"></div>
					<div className="chain"></div>
				</div>

				<a
					className="reference"
					href="http://bit.ly/2JPuBjx"
					target="_blank"
					rel="noreferrer"
				>
					🔗 Ali Soueidan
				</a>
			</div>
		</div>
	);
};

export default Face;
