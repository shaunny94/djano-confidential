import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import './Button.css';
import PersonList from './Datalist';


import axios from 'axios';

class Table extends Component {
  
  
  getTableHead = () => {
    console.log('hello')
    console.log(this.props.endpoint)
    if (this.props.endpoint !== "languagedata") {
         return ( <tr>
                  <th className="text-left">Id</th>
                  <th className="text-left">Name</th>
                  <th className="text-left">TotalDocs</th>
                  </tr>
                  )
        }

    if (this.props.endpoint === "languagedata") {
      return ( <tr>
                <th className="text-left">Id</th>
                <th className="text-left">Name</th>
                <th className="text-left">TotalDocs</th>
                <th className="text-left">ShortName</th>

                </tr>
                )
      }
    } 



    getTableBody = () => {
      let arr = []
      console.log(this.props.api.id)
      if (this.props.endpoint !== "languagedata") {
            return (
                  this.props.api.map((data, i) => {
                 return(  <tr>
                    <td className="text-left">{data.id}</td>
                    <td className="text-left">{data.name}</td>
                    <td className="text-left">{data.total_docs}</td>
                     </tr> ) } ) )
                  
               }

      if (this.props.endpoint === "languagedata") {
        return (
              this.props.api.map((data, i) => {
              return(  <tr>
                <td className="text-left">{data.id}</td>
                <td className="text-left">{data.name}</td>
                <td className="text-left">{data.total_docs}</td>
                <td className="text-left">{data.short_name}</td>
                  </tr> ) } ) )
              
            }

                    
          }
      

  
//  createTableHead = () => {
//   let api = this.props.api ;
//   console.log(api);
//   var arr = [] ;
//   try {
//   Object.keys(api).forEach(function (value, i) {
//      arr.push(<ObjectHead obj={Object.keys(value)[i]} key={i}/>)
   
//   } )
// } catch (error){
//   console.log(error);
// }
//   return arr
// }
 
    
        
    


  

  render() {

    if(!this.props.api) {  return (
      <div className="option">Select an option</div>
    ) } else {
      
    return (
      <table className="table-fill">
        <thead>
         
           { 
           this.getTableHead()
            }
            
         
       </thead>
      <tbody className="table-hover">
        
          {
            this.getTableBody()
               }
        


      </tbody>
       </table>
  
     
    );

    
   
  }
}

}

export default Table;
{/* <thead>
        
<tr>
<th className="text-left">Id</th>
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
</tbody>  */}

// let array = [];
// console.log('hello');
// let api = this.props.api;
// try {
//  Object.values(api).map(function (value, i)  {
//  console.log('bye')
//  return  <th key={i} className="text-left">Object.keys(value)[i]</th>
//  } )
// } catch(error) {
//       console.log(error)
// }
