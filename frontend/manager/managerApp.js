import React from 'react';
import Oops from '../guest/Oops.js';
import Logout from '../employee/Logout.js';
import Reimbursements from './Reimbursements.js';
import Statistics from './Statistics.js';

class AdminApp extends React.Component{
	constructor(props){
		super(props);
		this.state = {view: 1};
		this.login_fn = props.logout;
		this.eid = props.eid;
	}
	render(){
		var main;
		switch(this.state.view){
			case 0:
				main = <Logout logout={this.login_fn} />;
				break;
			case 1:
				main = <Reimbursements eid={this.eid}/>;
				break;
			case 2:
				main = <Statistics eid={this.eid}/>;
				break;
			default:
				main = <Oops />;
		}

		//nav
		let navlist = [<p>&#x1F409; Logout</p>
				, <p className="active">&#x1F996; Reimbursements</p>
				, <p>&#x1F422; Statistics</p>
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
export default AdminApp;
