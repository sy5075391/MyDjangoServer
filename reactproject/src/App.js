import React, {Component} from 'react';
import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.headers.post['Content-Type'] = 'application/json';
const server = 'http://192.168.0.113:8000';


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "",
            age: 0,
            readData: []
        };
        this.change = this.change.bind(this);
        this.write = this.write.bind(this);
        this.read = this.read.bind(this);

    }

    change(key, e) {
        this.setState({
            [key]: e.target.value
        });
    }

    async write() {
        let data = {'name': this.state.name, 'age': this.state.age};
        let res = await axios.post(`${server}/write/`, data);
        console.log(res)
    }

    async read() {
        let res = await axios.get(`${server}/read/`);

        this.setState({readData: res.data.data})
    }

    render() {
        return (
            <div className="App">
                <input onChange={(e) => this.change("name", e)}/>
                <br/>
                <input onChange={(e) => this.change("age", e)}/>
                <br/>
                <button onClick={this.write}>write2</button>
                <button onClick={this.read}>read</button>
                <div className='read2'>
                    {
                        this.state.readData.map((number) =>
                            <li>{number.fields.name + '-----' + number.fields.age}</li>
                        )
                    }
                </div>
            </div>

        );
    }
}


export default App;

