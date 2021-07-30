import React from 'react';

function Logout(props) {
	return <main>
		<header><h1>Logout?</h1></header>
		<button onClick={props.logout.bind(this, "guest", {})}>Logout!</button>
	</main>;
}

export default Logout;
