import React from 'react';
import axios from 'axios';
import Tinct from 'tinct';
import Center from "./Center";
import Button from "./Button";

class App extends React.Component {
    state = {
        detecting: null,
        ch1: null,
        ch2: null
    };

    constructor(props) {
        super(props);
        this.updateSelf=this.updateSelf.bind(this);
    }


    componentDidMount() {
        axios.defaults.baseURL = 'http://192.168.43.139/';
        this.updateSelf();
    }

    updateSelf() {
        axios.get('/detection').then(response => this.setState({detecting: response.data.status}));
        axios.get('/gpio/1').then(response => this.setState({ch1: response.data.status}));
        axios.get('/gpio/2').then(response => this.setState({ch2: response.data.status}));
    }

    render() {
        let {detecting, ch1, ch2} = this.state;
        return (
            <Center>
                <Button
                    color={detecting ? Tinct.red : Tinct.green}
                    onClick={() => {
                        axios.get('/detection/' + (detecting ? 'off' : 'on')).then(this.updateSelf)
                    }}
                >{detecting ? "Stop" : "Start"} detection</Button>
                <Button
                    onClick={()=>axios.get('/gpio/1/pulse?duration=5')}
                >Ch1 pulse</Button>
                <Button
                    color={ch1 ? Tinct.red : Tinct.green}
                    onClick={() => {
                        axios.get('/gpio/1/' + (detecting ? 'off' : 'on')).then(this.updateSelf)
                    }}
                >Ch1 on/off</Button>
                <Button
                    onClick={()=>axios.get('/gpio/2/pulse?duration=5')}
                >Ch2 pulse</Button>
                <Button
                    color={ch2 ? Tinct.red : Tinct.green}
                    onClick={() => {
                        axios.get('/gpio/2/' + (detecting ? 'off' : 'on')).then(this.updateSelf)
                    }}
                >Ch2 on/off</Button>
            </Center>
        );
    }
}

export default App;
