import React from 'react';
import {
  Button,
  Collapse,
  Container,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  Badge
} from 'reactstrap';

import {
  Link,
  NavLink
} from 'react-router-dom'


import logo from './assets/HANDEL-Logo-Small-2.png'

export default class TopNav extends React.Component {
  constructor(props) {
    super(props)
    this.toggle = this.toggle.bind(this)
    this.state = {
      isOpen: false
    }
    this.state ={
      iids: JSON.parse(window.atob(this.props.favorites))
    }
  }
  
  componentDidUpdate(prevProps){
    if(prevProps.favorites !== this.props.favorites){
      this.setState({
        iids: JSON.parse(window.atob(this.props.favorites))
      })
    }
  }

  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }

  render() {
    return (
      <Navbar color="dark" dark expand="md">
        <Container fluid>
          <NavbarBrand><Link to="/"><img src={logo} alt={'HANDEL-P Logo'} /></Link></NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
          <Collapse isOpen={this.state.isOpen} navbar>
            <Nav className="ml-auto" navbar>
              <NavItem>
                <NavLink to="/handelp/diabetes">Diabetes</NavLink>
              </NavItem>
              {(this.state.iids !== undefined && this.state.iids.length > 0) &&
                <NavItem>
                  <UncontrolledDropdown>
                    <DropdownToggle nav caret>Image Atlas <Badge color="primary">{this.state.iids.length}</Badge></DropdownToggle>
                    <DropdownMenu right>
                        <Link className='dropdown-item' to={`/pancreatlas?iids=${this.props.favorites}`}>Image Atlas</Link>
                        <Link className='dropdown-item' to={`/pancreatlas/favorites?iids=${this.props.favorites}`}>Favorites <Badge color="primary">{this.state.iids.length}</Badge></Link>
                    </DropdownMenu>
                  </UncontrolledDropdown>
                </NavItem>}
              {(this.props.favorites === undefined || this.state.iids.length <= 0) &&
                <NavItem active={(window.location.pathname === '/pancreatlas') ? true : false}>
                  <NavLink to={`/pancreatlas?iids=${this.props.favorites}`}>Image Atlas</NavLink>
                </NavItem>
              }
              <NavItem active={(window.location.pathname === '/handelp/collaborators') ? true : false}>
                <NavLink to="/handelp/collaborators">Collaborators</NavLink>
              </NavItem>
              <NavItem active={(window.location.pathname === '/handelp/about') ? true : false}>
                <NavLink to="/handelp/about">About</NavLink>
              </NavItem>
              <NavItem>
                <NavLink to='https://webapp.mis.vanderbilt.edu/vumc-giving/landing?appealCode=J1001'><Button color="danger">Join Our Efforts</Button></NavLink>
              </NavItem>
            </Nav>
          </Collapse>
        </Container>
      </Navbar>

    )
  }
}