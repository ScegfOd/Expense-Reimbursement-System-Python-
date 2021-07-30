import React from 'react';
import Login from './Login.js';
import Oops from './Oops.js';


class GuestApp extends React.Component{
    constructor(props){ 
		super(props);
		this.state = {view: 0, login_fn: props.login};
	}
	render(){
		let main;
		switch(this.state.view){
			case 0:
				main = <Login login={this.state.login_fn} />;
				break;
			default:
				main = <Oops />;
		}

		//nav
		let navlist = [<p className="active">&#x1F409; Login</p>
			].map((x,i)=>{
			return <li key={'nav'+i}
				onClick={x=>{
					x.target.parentElement.parentElement.childNodes.forEach(x=>{
						x.firstChild.classList.remove('active')
					});
					x.target.classList.add('active');
					this.setState({view: i});
				}}>{x}</li>;
			});
		let nav = <nav>
				<ul>
					{navlist}
				</ul>
			</nav>;


		return <div>
			{nav}
			{main}
		</div>;
	}
}
export default GuestApp;

