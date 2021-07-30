import React from "react";
import ReactDOM from "react-dom";
import GuestApp from './guest/guestApp.js';
import EmployeeApp from './employee/employeeApp.js';
import ManagerApp from './manager/managerApp.js';


class App extends React.Component {
	constructor(props) {
		super(props);
		this.state = {role: "guest"};
	}

	changeRole(new_role, member_info){
		this.setState({role: new_role, eid: member_info.eid});
		console.log(member_info);
		console.log(new_role);
	}

	render() {
		let app;
		if(this.state.role == "employee"){
			app = <EmployeeApp logout={this.changeRole.bind(this)} eid={this.state.eid} />;
		}else if(this.state.role == "manager"){
			app = <ManagerApp logout={this.changeRole.bind(this)} eid={this.state.eid} />;
		}else{
			app = <GuestApp login={this.changeRole.bind(this)} />;
		}

		//footer never changes:
		return <div>
			{app}
			<footer>all rights reserved</footer>
		</div>;
	}
}
ReactDOM.render(<App />, document.getElementById("root"));
