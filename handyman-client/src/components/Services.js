import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';

const Services = () => (
  <Container className="my-5">
    <Row>
      <Col md={4}>
        <Card>
          <Card.Body>
            <Card.Title>Plumbing</Card.Title>
            <Card.Text>Expert plumbing services for your home or business.</Card.Text>
          </Card.Body>
        </Card>
      </Col>
      <Col md={4}>
        <Card>
          <Card.Body>
            <Card.Title>Electrical</Card.Title>
            <Card.Text>Safe and reliable electrical work.</Card.Text>
          </Card.Body>
        </Card>
      </Col>
      <Col md={4}>
        <Card>
          <Card.Body>
            <Card.Title>Carpentry</Card.Title>
            <Card.Text>Quality carpentry services for all your needs.</Card.Text>
          </Card.Body>
        </Card>
      </Col>
    </Row>
  </Container>
);

export default Services;