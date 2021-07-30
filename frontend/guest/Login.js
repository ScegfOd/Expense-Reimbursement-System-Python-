import React from 'react';

class Login extends React.Component {
	constructor(props) {
		super(props);
		this.state = {callback: props.login};
	}

	LoginButton(){
		let role = "guest";
		let employee = {};
		let credentials = {
			email: document.getElementById('email').value,
			password: document.getElementById('password').value,
		}
		fetch('http://localhost:5000/login', {
    		method: 'POST',
    		mode: 'cors',
			headers: {
			  'Content-Type': 'application/json'
			},
			body: JSON.stringify(credentials),
		}).then(response =>{
			console.log('reply:')
			console.log(response)
			return response.json()
		}).catch(err =>{
			console.log('mistakes were made:')
			console.log(err)
		}).then(e =>{
			console.log('final step:')
			console.log(e)
			console.log(typeof(e))
			if (typeof(e) != 'string'){
				employee = e
				if (employee.is_manager){
					role = "manager"
				}else{
					role = "employee"
				}
			}
			this.state.callback(role, employee);
		})
	}

	// Renders component based on current state and props
	render() {
		return <main>
			<header><h1>Login</h1></header>
			<section className="form">
				<label>Email:</label>
				<input maxlength="30" type="text" id="email" placeholder="you@email.org" />
				<label>Password:</label>
				<input maxlength="20" type="password" id="password" placeholder="password" />
				<p></p>
				<button id="submit" onClick={this.LoginButton.bind(this)}>Login</button>
			</section>
		</main>;
	}
}

export default Login;
