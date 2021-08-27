import React from "react";
import "./Tweets.scss";

import Tweet from "./Tweet";
const Tweets = () => {
	let tweets_list = [
		"Se ponen escogedores con la vacuna, por que no te van a dejar entrar a otros pa\u00edses, \ud83e\udd23\ud83e\udd23\ud83e\udd23 no viajan ni a un p\u00faeblito de mi lindo Ecuador y andan hechos los adefeciosos.\nVacunate se responsable.",
		"@LassoGuillermo @jcarreraandrade Lassito por favor por el pais ayudanos con las vacunas, vacuna a todo el Ecuador lo mas pronto posible. gracias totales Dios te bendiga.",
		"@EstebanOrtizMD @alferdez Por qu\u00e9 no traen a Ecuador est\u00e1 vacuna? Motivos pol\u00edticos, econ\u00f3micos o de salud?",
		"#Ecuador: Estos son los pasos para inscribirse en la plataforma para recibir la vacuna contra el covid-19 en Ecuador https://t.co/WCPttdbHv5",
		"#DesdeLasRedes| \u26bd Responde a nuestra encuesta de hoy \ud83e\udd14\u00bfEstar\u00edas de acuerdo con que retorne el p\u00fablico los estadios en #Ecuador a pesar de no contar con la vacuna a\u00fan ?  \ud83d\udcfa No te pierdas #LosProtagonistas \ud83c\udfc6 desde las 13h45 con @eduandinoe, @fabriciofloresm y @majogavilanesa",
		"#Internacionales | El gobierno de Ecuador anunci\u00f3 que comprar\u00e1 6 millones de dosis de la vacuna CanSino contra el coronavirus, medida con la que espera cumplir la meta de inmunizar a nueve millones de personas en 100 d\u00edas. https://t.co/knZPToY4JY",
		"Cada Municipio de Ecuador  @AMEcuador q pueda comprar vacunas AntiCovid debe hacerlo para contrarrestar la ineptitud del Gobierno.  Luego @Salud_Ec debe devolver los recursos ya que era obligaci\u00f3n de esa cartera del estado proporcionar la vacuna pero la corrupci\u00f3n lo impidi\u00f3",
		"#ATENCI\u00d3N | Ecuador y Rusia analizan establecer planta para la producci\u00f3n de la vacuna contra #covid19 Sputnik \u00bb https://t.co/OEF3tt3rqM https://t.co/9E6No4Xrsp",
	];

	return (
		<div className="tweets">
			{tweets_list.map((content) => (
				<Tweet content={content} />
			))}
		</div>
	);
};

export default Tweets;
