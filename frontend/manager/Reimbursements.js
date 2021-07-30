import React from 'react';

class Reimbursements extends React.Component{
	constructor(props){
		super(props);
		this.state = {"eid": props.eid, "reimbursements": []};
		this.fetch()
	}

	fetch(){
		this.state["reimbursements"] = []

		let url = 'http://localhost:5000/managers/' + this.state["eid"] + '/reimbursements';
		fetch(url, {
			method: 'GET',
			mode: 'cors',
		}).then(response =>{
			console.log('reply:')
			console.log(response)
			return response.json()
		}).catch(err =>{
			console.log('mistakes were made:')
			console.log(err)
		}).then(response_dict =>{
			console.log('final step:')
			console.log(response_dict)
			console.log(typeof(response_dict))
			if (typeof(response_dict) != 'string'){
				Object.keys(response_dict).forEach(x=>{
					this.state["reimbursements"].push(this.parse_request(response_dict[x]))
				})
			}
			this.update()
		})
	}

	parse_request(request){
		let y = {}
		y["rid"] = request["rid"]
		y["eid"] = request["eid"]
		y["pennies"] = request["pennies"]
		y["reason"] = request["reason"]
		y["response"] = request["response"]
		if(request["is_pending"]){
			y["status"] = "pending";
		}else if(request["is_approved"]){
			y["status"] = "approved";
		}else{
			y["status"] = "denied";
		}
		return y
	}

	new_request(){
		pennies = document.getElementById('pennies').value;
		let request = {}
		if (pennies > 0){
			request["rid"] = "?";
			request["eid"] = this.state["eid"];
			request["pennies"] = pennies;
			request["response"] = null;
			request["reason"] = document.getElementById('reason').value;
			request["status"] = "pending";
			this.state["reimbursements"].push(request);
			this.update();
			this.push_to_server({
				"pennies": request["pennies"]
				, "reason": request["reason"]
			});
		}
	}

	push_to_server(request){
		let main = null;
		let p = null;
		fetch('http://localhost:5000/employees/' + this.state["eid"] + '/reimbursements', {
    		method: 'POST',
    		mode: 'cors',
			headers: {
			  'Content-Type': 'application/json'
			},
			body: JSON.stringify(request),
		}).then(response =>{
			console.log('reply:')
			console.log(response)
			document.getElementById('pennies').value = "";
			document.getElementById('reason').value = "";
			main = document.getElementsByTagName('main')[0]
			p = document.createElement('p')
			p.innerText="request successful!"
			main.appendChild(p)
		}).catch(err =>{
			console.log('mistakes were made:')
			console.log(err)
			main = document.getElementsByTagName('main')[0]
			p = document.createElement('h1')
			p.innerText="...UH OH... server didn't get that request!"
			main.appendChild(p)
			this.state["reimbursements"].pop();
		})
	}

	update(){
		this.setState({"eid": this.state["eid"], "reimbursements": this.state["reimbursements"]});
	}

	approve(req, i){
		let request = {
			"is_approved": true
		}
		request["response"] = document.getElementById('reply'+i).value
		this.send_approval(request, i, "approved");
	}

	deny(req, i){
		let request = {
			"is_approved": false
		}
		request["response"] = document.getElementById('reply'+i).value
		this.send_approval(request, i, "denied");
	}

	send_approval(request, i, status){
		let main = null;
		let p = null;
		fetch('http://localhost:5000/employees/' + this.state["eid"] + '/reimbursements/' + request["rid"], {
    		method: 'POST',
    		mode: 'cors',
			headers: {
			  'Content-Type': 'application/json'
			},
			body: JSON.stringify(request),
		}).then(response =>{
			console.log('reply:')
			console.log(response)
			this.update()
			main = document.getElementsByTagName('main')[0]
			p = document.createElement('p')
			p.innerText="request approval/denial successful!"
			main.appendChild(p)
			this.state["reimbursements"][i]["status"] = status
		}).catch(err =>{
			console.log('mistakes were made:')
			console.log(err)
			main = document.getElementsByTagName('main')[0]
			p = document.createElement('h1')
			p.innerText="...UH OH... server didn't get that request!"
			main.appendChild(p)
		})
	}

	render(){
		let data_table = <tbody>
				{this.state.reimbursements.map(
					(request,i)=><tr key={"request"+i}>
						<td>{request["rid"]}</td>
						<td>{request["status"]}</td>
						<td>${request["pennies"]/100}</td>
						<td>{request["reason"]}</td>
						<td><input id={"reply"+i} maxlength="50" type="text" placeholder="everyone needs boots" value={request["response"]}/></td>
						<td><button id={"approve"+i} onClick={this.approve.bind(this, request, i)}>{"Approve"}</button></td>
						<td><button id={"deny"+i} onClick={this.deny.bind(this, request, i)}>{"Deny"}</button></td>
					</tr>
				)}
			</tbody>

		let new_request_form = <section className="form">
				<label>Reason:</label>
				<input maxlength="50" type="text" id="reason" placeholder="goblins stole my boots again" />
				<label>Amount in coppers:</label>
				<input maxlength="9" type="number" id="pennies" placeholder="9001" />
				<p></p>
				<button id="newrequest" onClick={this.new_request.bind(this)}>{"new request"}</button>
			</section>

		return <main>
			<header><h1>Reimbursement requests:</h1></header>
			{new_request_form}
			<table>
				<thead>
					<tr>
						<td>ID</td>
						<td>Status</td>
						<td>Amount</td>
						<td>Reason for reimbursement</td>
						<td>Response to request</td>
						<td>Approve</td>
						<td>Deny</td>
					</tr>
				</thead>
				{data_table}
			</table>
		</main>
	}
}
export default Reimbursements;
