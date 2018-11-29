import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import './Button.css';
import PersonList from './Datalist';
import ObjectHead from './ObjectHead';

import axios from 'axios';

class Table extends Component {
  
  
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
 
    createTableHead = () => {
      let array = [];
      let api = this.props.api;
      Object.values(api).forEach(function (value, i)  {
        array.push(<th className="text-left">Object.keys(value)[i]</th>);
       
      } )
      
        return array
        }
    
        
    
    //   //    }
    //   Object.keys(api).forEach(function(key) {
    //     arr.push(api[key]);
    //   });
        
    //     }

  

  render() {

    if(!this.props.api) {  return (
      <div>Select an option</div>
    ) } else {
      
    return (
      <table className="table-fill">
        <thead>
         <tr>
           { 
           this.createTableHead()
            }
            
         </tr>
       </thead>
      <tbody className="table-hover">
        <tr>
          {
            // this.createTableBody()
               }
        </tr>


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