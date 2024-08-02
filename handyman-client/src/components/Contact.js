import React from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

const Contact = () => (
  <Container className="my-5">
    <Row>
      <Col>
        <h2>Contact Us</h2>
        <Form>
          <Form.Group controlId="formName">
            <Form.Label>Name</Form.Label>
            <Form.Control type="text" placeholder="Enter your name" />
          </Form.Group>
          <Form.Group controlId="formEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control type="email" placeholder="Enter your email" />
          </Form.Group>
          <Form.Group controlId="formMessage">
            <Form.Label>Message</Form.Label>
            <Form.Control as="textarea" rows={3} placeholder="Your message" />
          </Form.Group>
          <Button variant="primary" type="submit">Submit</Button>
        </Form>
      </Col>
    </Row>
  </Container>
);

export default Contact;