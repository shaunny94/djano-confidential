import React from 'react';

import axios from 'axios';

 class PersonList extends React.Component {
  state = {
    persons: []
  }

  componentDidMount() {
    axios.get('http://localhost:8000/confidentialdata/')
      .then(res => {
          console.log('Hello there');
        const persons = res.json();
        this.setState({ persons });
      })
  }

  render() {
    return (
      <ul>
        { this.state.persons.map(person => <li>{person.name}</li>)}
      </ul>
    )
  }
}

export default PersonList;