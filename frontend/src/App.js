import React, { Component } from 'react';
import logo from './logo.svg';
import Table from './Table';
import './App.css';
import PersonList from './Datalist';
import './Button.css';
import axios from 'axios';


class App extends Component {

  state = {
    mock_data : '',
    endpoint: ''
    }
    
  

  confidentialDataHandler = () => {
    axios.get("http://localhost:8000/confidentialdata")
      .then(res => {
        const mock_data = res.data;
        this.setState({ mock_data });
        this.setState({ endpoint: 'confidentialdata' })
      })
      .catch(error => {
        console.log(error.response)
    }) 
  }

  confidentialLabelsHandler = () => {
    axios.get("http://localhost:8000/confidentiallabels")
      .then(res => {
        const mock_data = res.data;
        this.setState({ mock_data });
        this.setState({ endpoint: 'confidentiallabels' })
      })
      .catch(error => {
        console.log(error.response)
    }) 
  }


  docTypeDataHandler = () => {
    axios.get("http://localhost:8000/doctypedata")
      .then(res => {
        const mock_data = res.data;
        this.setState({ mock_data });
        this.setState({ endpoint: 'doctypedata' })
      })
      .catch(error => {
        console.log(error.response)
    }) 
  }

  languageDataHandler = () => {
    axios.get("http://localhost:8000/languagedata")
      .then(res => {
        const mock_data = res.data;
        this.setState({ mock_data });
        this.setState({ endpoint: 'languagedata' })
      })
      .catch(error => {
        console.log(error.response)
    }) 
  }

  render() {
    console.log(typeof this.state.mock_data);
    // console.log(typeof this.state);
     console.log( this.state.mock_data);
     console.log(this.state.endpoint)
    // console.log( this.state);
    return (
      <div className="table-title">
<h3>Data Table</h3>
<button className="button-two" onClick={this.confidentialDataHandler}><span>Confidential Data</span></button>
<button className="button-two" onClick={this.docTypeDataHandler}><span>Document Type Data</span></button>
<button className="button-two" onClick={this.languageDataHandler}><span>Language Data</span></button>
     <Table api={this.state.mock_data} endpoint={this.state.endpoint}/>
    </div>
    );
  }
}

export default App;
