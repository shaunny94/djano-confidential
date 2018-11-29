import React, { Component } from 'react';
import logo from './logo.svg';
import Table from './Table';
import './App.css';
import PersonList from './Datalist';
import './Button.css';
import axios from 'axios';


class App extends Component {

  state = {
	  mock_data : ''
    }
    
  

  confidentialDataHandler = () => {
    fetch("http://localhost:8000/confidentialdata")
      .then(res => {
        const mock_data = res.json();
        this.setState({ mock_data });
      })
      .catch(error => {
        console.log(error.response)
    }) 
  }

  render() {
    console.log(typeof this.state.mock_data);
    // console.log(typeof this.state);
     console.log( this.state.mock_data);
    // console.log( this.state);
    return (
      <div className="table-title">
<h3>Data Table</h3>
<button className="button-two" onClick={this.confidentialDataHandler}><span>Confidential Data</span></button>
     
     <Table api={this.state.mock_data}/>
    </div>
    );
  }
}

export default App;
