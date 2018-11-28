import React, { Component } from 'react';
import logo from './logo.svg';
import Table from './Table';
import './App.css';
import PersonList from './Datalist';


class App extends Component {


  render() {
    return (
      <div className="table-title">
<h3>Data Table</h3>
     <Table />
     </div>
    );
  }
}

export default App;
