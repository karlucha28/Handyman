import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';

const Home = () => (
  <Container className="my-5">
    <Row>
      <Col className="text-center">
        <h2>Welcome to Best Hiting and Piping Inc.</h2>
        <p>We offer top-notch handyman services in Pennsylvania.</p>
        <Button variant="primary" href="/services">Our Services</Button>
      </Col>
    </Row>
  </Container>
);

export default Home;