import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';

const NavigationBar = () => (
  <Navbar bg="dark" variant="dark" expand="lg" sticky="top">
    <Navbar.Brand href="/">Best Hiting and Piping Inc.</Navbar.Brand>
    <Navbar.Toggle aria-controls="basic-navbar-nav" />
    <Navbar.Collapse id="basic-navbar-nav">
      <Nav className="ml-auto">
        <Nav.Link href="/">Home</Nav.Link>
        <Nav.Link href="/services">Services</Nav.Link>
        <Nav.Link href="/about">About</Nav.Link>
        <Nav.Link href="/contact">Contact</Nav.Link>
      </Nav>
    </Navbar.Collapse>
  </Navbar>
);

export default NavigationBar;