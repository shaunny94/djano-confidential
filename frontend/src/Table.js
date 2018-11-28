import React, { Component } from 'react';
// import logo from './logo.svg';
// import './App.css';
import PersonList from './Datalist';

import axios from 'axios';

class Table extends Component {
  state = {
    persons: []
  }

  componentDidMount() {
    axios.get('http://localhost:8000/confidentialdata')
      .then(res => {
        const persons = res.data;
        this.setState({ persons });
      })
  }

  render() {
    return (
      <table className="table-fill">
      <thead>
      <tr>
      <th className="text-left">{this.state.persons.map(person => person.name)}</th>
      <th className="text-left">Sales</th>
      </tr>
      </thead>
      <tbody className="table-hover">
      <tr>
      <td className="text-left">January</td>
      <td className="text-left">$ 50,000.00</td>
      </tr>
      <tr>
      <td className="text-left">February</td>
      <td className="text-left">$ 10,000.00</td>
      </tr>
      <tr>
      <td className="text-left">March</td>
      <td className="text-left">$ 85,000.00</td>
      </tr>
      <tr>
      <td className="text-left">April</td>
      <td className="text-left">$ 56,000.00</td>
      </tr>
      <tr>
      <td className="text-left">May</td>
      <td className="text-left">$ 98,000.00</td>
      </tr>
      </tbody>
      </table>
     
    );
  }
}

export default Table;
