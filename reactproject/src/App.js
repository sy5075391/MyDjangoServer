import React, { Component } from 'react';
import './App.css';
import {
  registerServer,
  loginServer,
  allUsersServer
} from './server';

import "./css/style.css";



class App extends Component {
  constructor (props) {
    super(props);

    this.state = {
      username: "",
      password: "",
      users: [],
      data:"",
    }



    this.handlerChange = this.handlerChange.bind(this);
    this.register = this.register.bind(this);
    this.login = this.login.bind(this);
    this.allUsers = this.allUsers.bind(this);
  }

  handlerChange (k, e) {
    this.setState({
      [k]: e.target.value
    });
  }

  async register () {
    let data = {
      username: this.state.username,
      password: this.state.password
    }
    let res = await registerServer(data);
    console.log(typeof(res));
      this.setState({
      data :JSON.stringify(res)
    })
  }

  async login () {
    let data = {
      username: this.state.username,
      password: this.state.password
    }
    let res = await loginServer(data);
    this.setState({
      data :JSON.stringify(res)
    })
  }

  async allUsers () {
    let res = await allUsersServer();
  this.setState({
      data :JSON.stringify(res)
    })
  }

  render() {
    return (
      <div className="App">
        <div>
          <input onChange={(e) => {this.handlerChange('username', e)}} placeholder="username" />
        </div>
        <div>
          <input onChange={(e) => {this.handlerChange('password', e)}} placeholder="password" />
        </div>
        <div>
          <button onClick={this.register}>register</button>
          <button onClick={this.login}>login</button>
        </div>
        <div>
          <button onClick={this.allUsers}>all users</button>
        </div>
        <h1>data:{this.state.data}</h1>
      </div>
    );
  }
}



export default App;