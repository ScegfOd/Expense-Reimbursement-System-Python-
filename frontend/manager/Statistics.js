import React from 'react';

class Statistics extends React.Component{
	constructor(props){
		super(props);
		this.state = {"eid": props.eid, "stats": {}};
		this.fetch()
		this.stats = <p></p>
	}

	fetch(){
		let url = "http://localhost:5000/managers/" + this.state["eid"] + "/reimbursements/statistics";
		fetch(url, {
			method: "GET",
			mode: "cors",
		}).then(response =>{
			console.log("reply:")
			console.log(response)
			return response.json()
		}).catch(err =>{
			console.log("mistakes were made:")
			console.log(err)
		}).then(response_dict =>{
			console.log("final step:")
			console.log(response_dict)
			console.log(typeof(response_dict))
			if (typeof(response_dict) != "string"){
				this.stats = <section className="form">
					<label>Email of biggest spender:</label>
					<p>{response_dict["max_spend_employee"]["email"]}</p>
					<label>{"Mean request for " + response_dict["max_spend_employee"]["email"]}:</label>
					<p>{response_dict["max_spend_employee_mean_request"]/100}</p>
					<label>Mean request:</label>
					<p>{response_dict["all_request_mean_request"]/100}</p>
					<label>Largest request:</label>
					<p>{response_dict["all_request_max_request"]["rid"]/100}</p>
				</section>
			}
			this.setState({"eid": this.state["eid"], "stats": this.stats["stats"]})
		})
	}

	render(){
		let stats = this.stats
		return <main>
			<header><h1>Statistics:</h1></header>
			{stats}
		</main>
	}
}
export default Statistics;
