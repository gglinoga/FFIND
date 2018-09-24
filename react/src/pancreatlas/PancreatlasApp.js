import React, { Component } from 'react';
import './Pancreatlas.css';
import HomePage from './HomePage'
import PancreatlasNavbar from './PancreatlasNavbar'
import DatasetList from './DatasetList'
import Footer from './Footer'
import ImageDetail from './ImageDetail'
import MatrixView from './MatrixView'
import AgeBrowser from './AgeBrowser'
import Nomenclature from './Nomenclature'

import {
  Container,
  Row,
} from 'reactstrap'

import {
  Switch,
  Route
} from 'react-router'

class PancreatlasApp extends Component {
  render() {
    return (
      <div className="pancreatlas">
        <Container fluid>
          <Row className="pancreatlas-row">
            <PancreatlasNavbar />
          </Row>
        </Container>
        <div className='wrapper'>
          <div className='content'>
            <Container>
              <Switch>
                <Route exact path='/pancreatlas' component={HomePage} />
                {/* <Route path='/collections' component={CollectionList} /> */}
                <Route exact path='/pancreatlas/dataset' component={DatasetList} />
                <Route exact path='/pancreatlas/dataset/:did' component={AgeBrowser} />
                <Route path='/pancreatlas/image/:iid' component={ImageDetail} />
                <Route path='/pancreatlas/matrixview/:dsid' component={MatrixView} />
                <Route path='/pancreatlas/nomenclature' component={Nomenclature} />
              </Switch>
            </Container>
          </div>
          <Footer />
        </div>
      </div>
    );
  }
}

export default PancreatlasApp;
