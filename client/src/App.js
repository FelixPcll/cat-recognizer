import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App__header">
          <div className="App__header__icon"></div>
          <div className="App__header__text">Cat recognizer</div>
        </div>
        <div className="App__footer">
          <ul class="App__footer__button-group">
            <li></li>
            <li></li>
          </ul>
        </div>
      </div>
    );
  }
}

export default App;
