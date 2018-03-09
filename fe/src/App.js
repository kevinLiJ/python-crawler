import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";

import { Table } from "antd";

class App extends Component {
    constructor() {
        super();
        this.state = {
            thunderLinks: [],
            html: "123"
        };
    }
    componentDidMount() {
        fetch("/api/movies", {
            method: "GET"
        }).then(res => {
            res.json().then(data => {
                console.log(data.result[0].thunder_links.split(","));
                this.setState({
                    thunderLinks: data.result[0].thunder_links.split(",")
                });
            });
        });
    }
    render() {
        console.log(this.state.thunderLinks);
        return <div dangerousSetInnerHTML={{ __html: this.state.html }} />;
    }
}

export default App;
