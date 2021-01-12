import React from 'react';
import { Router, Route, Switch } from 'react-router-dom';

import history from './History';
import Hello from './components/Hello'

const Routes = () => (
  <Router history={history}>
    <Route path='' component={Hello} />
  </Router>
);

export default Routes;